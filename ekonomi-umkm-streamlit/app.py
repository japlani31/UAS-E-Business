# -*- coding: utf-8 -*-
"""
UMKM & E-Business Digital Learning Hub
Aplikasi pembelajaran Ekonomi UMKM / E-Business.
Ardiansyah Japlani, S.E., M.B.A. - FEB Universitas Muhammadiyah Metro.

Menu: Beranda, Materi (Baca + Latihan), Tugas, UAS.
Fokus rilis ini: modul UAS daring dengan pengaman anti-contek.
"""

import time
import hashlib
import random
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components

# ---- Impor bank soal UAS (wajib) ----
import uas_soal

# ---- Impor modul opsional (tidak boleh membuat aplikasi gagal) ----
try:
    import sheets
    _SHEETS_ADA = True
except Exception:
    _SHEETS_ADA = False

try:
    import bank_soal
    _BANK_TUGAS_ADA = True
except Exception:
    _BANK_TUGAS_ADA = False

try:
    import content
    _CONTENT_ADA = True
except Exception:
    _CONTENT_ADA = False


st.set_page_config(page_title="E-Business Learning Hub - UM Metro",
                   page_icon="📘", layout="centered")


# ============================================================
#  UTILITAS
# ============================================================
def seed_dari_npm(npm):
    """Mengubah NPM menjadi angka acak stabil (sama di semua perangkat)."""
    h = hashlib.md5(str(npm).strip().encode("utf-8")).hexdigest()
    return int(h, 16) % (2 ** 32)


def ambil_soal_uas(npm):
    """
    Mengambil paket soal unik untuk satu NPM.
    - Memilih JUMLAH_SOAL_PER_MAHASISWA soal acak dari bank 250.
    - Mengacak urutan opsi tiap soal (bila ACAK_OPSI True).
    Struktur tiap item: {"q": teks, "opts": [(indeks_asli, teks_opsi), ...], "a_asli": indeks_benar}
    """
    rnd = random.Random(seed_dari_npm(npm))
    idx = list(range(len(uas_soal.UAS_BANK)))
    rnd.shuffle(idx)
    pilih = idx[: uas_soal.JUMLAH_SOAL_PER_MAHASISWA]

    paket = []
    for i in pilih:
        q = uas_soal.UAS_BANK[i]
        opts = list(enumerate(q["o"]))  # [(0,'A'),(1,'B'),...]
        if uas_soal.ACAK_OPSI:
            rnd.shuffle(opts)
        paket.append({"q": q["q"], "opts": opts, "a_asli": q["a"]})
    return paket


def suntik_anti_contek():
    """
    Mencegah seleksi teks, salin-tempel, klik kanan, dan pintasan papan ketik,
    baik di desktop MAUPUN di HP (perbaikan callout iOS/Android).
    """
    # 1) CSS: berlaku pada dokumen utama (mematikan seleksi & long-press di HP)
    st.markdown(
        """
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] * {
            -webkit-user-select: none !important;
            -moz-user-select: none !important;
            -ms-user-select: none !important;
            user-select: none !important;
            -webkit-touch-callout: none !important;   /* mematikan menu long-press HP */
            -webkit-tap-highlight-color: transparent !important;
        }
        /* Kotak input tetap boleh diketik */
        input, textarea { -webkit-user-select: text !important; user-select: text !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # 2) JS: memblokir event salin/klik-kanan/pintasan + menghitung pindah tab
    components.html(
        """
        <script>
        const d = window.parent.document;
        const blok = ['contextmenu','copy','cut','paste','selectstart','dragstart'];
        blok.forEach(function(ev){
            d.addEventListener(ev, function(e){ e.preventDefault(); return false; }, {capture:true});
        });
        d.addEventListener('keydown', function(e){
            const k = (e.key||'').toLowerCase();
            if ((e.ctrlKey || e.metaKey) && ['c','x','v','a','u','s','p'].indexOf(k) !== -1){
                e.preventDefault(); return false;
            }
            if (e.key === 'PrintScreen'){ e.preventDefault(); }
        }, {capture:true});

        // Hitung berapa kali mahasiswa meninggalkan halaman (pindah tab / minimize)
        if (!window.parent.__vtHook){
            window.parent.__vtHook = true;
            d.addEventListener('visibilitychange', function(){
                if (d.hidden){
                    try{
                        const u = new URL(window.parent.location);
                        let c = parseInt(u.searchParams.get('vt') || '0') + 1;
                        u.searchParams.set('vt', c);
                        window.parent.history.replaceState({}, '', u);
                    }catch(err){}
                }
            });
        }
        </script>
        """,
        height=0,
    )


def baca_pindah_tab():
    """Membaca jumlah pindah tab dari parameter URL (diisi oleh JS)."""
    try:
        return int(st.query_params.get("vt", 0))
    except Exception:
        return 0


# ============================================================
#  HALAMAN: BERANDA
# ============================================================
def halaman_beranda():
    st.title("📘 E-Business Digital Learning Hub")
    st.caption("Program Studi S1 Manajemen · Konsentrasi Bisnis · FEB Universitas Muhammadiyah Metro")
    st.write("Assalamualaikum. Selamat datang di ruang belajar E-Business.")
    st.markdown(
        """
        **Menu yang tersedia:**
        - **Materi** — bahan bacaan tiap pertemuan dan latihan mandiri.
        - **Tugas** — kuis pilihan ganda bernilai.
        - **UAS** — ujian akhir semester daring (Pertemuan 10–15).

        Kerjakan dengan **jujur (shiddiq)** dan **amanah**. Nilai yang benar
        lahir dari usaha yang benar.
        """
    )
    with st.expander("ℹ️ Info teknis singkat"):
        online = "Tersambung" if (_SHEETS_ADA and "gcp_service_account" in st.secrets) else "Belum diatur (mode offline)"
        st.write(f"- Penyimpanan Google Sheet: **{online}**")
        st.write(f"- Bank soal UAS: **{len(uas_soal.UAS_BANK)} soal**")
        st.write(f"- Tiap mahasiswa: **{uas_soal.JUMLAH_SOAL_PER_MAHASISWA} soal**, "
                 f"durasi **{uas_soal.DURASI_UAS_MENIT} menit**")


# ============================================================
#  HALAMAN: MATERI (Baca + Latihan)
# ============================================================
def halaman_materi():
    st.header("📚 Materi Pembelajaran")
    if not _CONTENT_ADA or not getattr(content, "PERTEMUAN", None):
        st.info("Modul materi (content.py) belum tersedia pada rilis ini.")
        return

    daftar = content.PERTEMUAN
    label = [f"Pertemuan {p.get('id','?')} — {p.get('judul','')}" for p in daftar]
    pilih = st.selectbox("Pilih pertemuan:", range(len(daftar)), format_func=lambda i: label[i])
    p = daftar[pilih]

    tab_baca, tab_latih = st.tabs(["📖 Baca", "✍️ Latihan"])
    with tab_baca:
        if p.get("ayat_text"):
            st.info(f"**{p.get('ayat','')}** — {p['ayat_text']}")
        st.markdown(p.get("baca", "_Materi belum tersedia._"))
    with tab_latih:
        kuis = p.get("kuis", [])
        if not kuis:
            st.write("Belum ada soal latihan untuk pertemuan ini.")
        else:
            jawab = {}
            for i, s in enumerate(kuis):
                jawab[i] = st.radio(f"{i+1}. {s['q']}", s["o"], index=None, key=f"lat_{p['id']}_{i}")
            if st.button("Periksa jawaban", key=f"cek_lat_{p['id']}"):
                benar = sum(1 for i, s in enumerate(kuis)
                            if jawab[i] is not None and s["o"].index(jawab[i]) == s["a"])
                st.success(f"Benar {benar} dari {len(kuis)}. Latihan ini tidak dinilai, teruslah berlatih.")


# ============================================================
#  HALAMAN: TUGAS
# ============================================================
def halaman_tugas():
    st.header("📝 Tugas Pilihan Ganda")
    if not _BANK_TUGAS_ADA or not getattr(bank_soal, "TUGAS", None):
        st.info("Bank soal Tugas belum tersedia pada rilis ini.")
        return
    _mesin_ujian(
        judul="Tugas",
        jenis="tugas",
        durasi_menit=getattr(bank_soal, "DURASI_TUGAS_MENIT", 15),
        paket_fn=lambda npm: _paket_dari_bank(bank_soal.TUGAS, npm, len(bank_soal.TUGAS)),
    )


def _paket_dari_bank(bank, npm, jumlah):
    """Membuat paket soal dari bank sederhana (format {'q','o','a'})."""
    rnd = random.Random(seed_dari_npm(npm))
    idx = list(range(len(bank)))
    rnd.shuffle(idx)
    paket = []
    for i in idx[:jumlah]:
        q = bank[i]
        opts = list(enumerate(q["o"]))
        rnd.shuffle(opts)
        paket.append({"q": q["q"], "opts": opts, "a_asli": q["a"]})
    return paket


# ============================================================
#  HALAMAN: UAS
# ============================================================
def halaman_uas():
    st.header("🎓 Ujian Akhir Semester (UAS) E-Business")
    _mesin_ujian(
        judul="UAS",
        jenis="uas",
        durasi_menit=uas_soal.DURASI_UAS_MENIT,
        paket_fn=ambil_soal_uas,
    )


# ============================================================
#  MESIN UJIAN (dipakai Tugas & UAS)
# ============================================================
def _mesin_ujian(judul, jenis, durasi_menit, paket_fn):
    ns = f"{jenis}_"  # namespace session_state

    # ---------- Tahap 1: identitas ----------
    if not st.session_state.get(ns + "mulai"):
        st.markdown(
            f"""
            **Ketentuan {judul}:**
            - Jumlah soal: **{uas_soal.JUMLAH_SOAL_PER_MAHASISWA if jenis=='uas' else 'sesuai bank'}**, setiap mahasiswa berbeda.
            - Waktu: **{durasi_menit} menit**, tidak ada waktu tambahan.
            - Ujian **tidak dapat diulang**. Satu NPM satu kesempatan.
            - Salin-tempel dan klik kanan dinonaktifkan. Perpindahan tab dicatat.
            - Kerjakan sendiri dengan jujur. Allah Maha Melihat.
            """
        )
        nama = st.text_input("Nama lengkap", key=ns + "nama_in")
        npm = st.text_input("NPM", key=ns + "npm_in")
        setuju = st.checkbox("Saya mengerjakan sendiri dengan jujur dan amanah.", key=ns + "setuju")

        if st.button(f"Mulai {judul}", type="primary", key=ns + "btn_mulai"):
            if not nama.strip() or not npm.strip():
                st.error("Nama dan NPM wajib diisi.")
                return
            if not setuju:
                st.error("Centang pernyataan kejujuran terlebih dahulu.")
                return
            # Cek satu NPM satu kesempatan (bila Sheet tersambung)
            if _SHEETS_ADA and sheets.npm_sudah_mengerjakan(npm, jenis=jenis):
                st.error("NPM ini sudah pernah mengerjakan. Ujian tidak dapat diulang.")
                return
            st.session_state[ns + "mulai"] = True
            st.session_state[ns + "nama"] = nama.strip()
            st.session_state[ns + "npm"] = npm.strip()
            st.session_state[ns + "paket"] = paket_fn(npm.strip())
            st.session_state[ns + "start_ts"] = time.time()
            st.session_state[ns + "selesai"] = False
            st.query_params["vt"] = "0"  # reset penghitung pindah tab
            st.rerun()
        return

    # ---------- Tahap 3: hasil ----------
    if st.session_state.get(ns + "selesai"):
        _tampilkan_hasil(ns, judul, jenis)
        return

    # ---------- Tahap 2: pengerjaan ----------
    suntik_anti_contek()
    paket = st.session_state[ns + "paket"]
    durasi_detik = durasi_menit * 60
    sisa = int(durasi_detik - (time.time() - st.session_state[ns + "start_ts"]))

    # Waktu habis -> submit otomatis
    if sisa <= 0:
        _finalisasi(ns, jenis, otomatis=True)
        st.rerun()

    menit, detik = divmod(max(sisa, 0), 60)
    warna = "red" if sisa <= 60 else ("orange" if sisa <= 120 else "green")
    st.markdown(
        f"<div style='position:sticky;top:0;background:#111;padding:8px 12px;border-radius:8px;"
        f"z-index:999;text-align:center;font-size:20px;color:{warna};'>"
        f"⏱️ Sisa waktu: <b>{menit:02d}:{detik:02d}</b></div>",
        unsafe_allow_html=True,
    )
    st.caption(f"Peserta: {st.session_state[ns+'nama']} · NPM {st.session_state[ns+'npm']}")

    with st.form(ns + "form_ujian"):
        jawaban = {}
        for i, s in enumerate(paket):
            st.markdown(f"**{i+1}. {s['q']}**")
            teks_opsi = [o[1] for o in s["opts"]]
            pilih = st.radio("", teks_opsi, index=None, key=f"{ns}soal_{i}",
                             label_visibility="collapsed")
            jawaban[i] = pilih
            st.divider()
        kirim = st.form_submit_button("✅ Selesai & Kirim", type="primary")

    if kirim:
        st.session_state[ns + "jawaban_final"] = jawaban
        _finalisasi(ns, jenis, otomatis=False)
        st.rerun()

    # Rerun tiap detik untuk memperbarui timer & menegakkan batas waktu
    time.sleep(1)
    st.rerun()


def _finalisasi(ns, jenis, otomatis):
    """Menghitung nilai, menyimpan ke Sheet, mengunci sesi."""
    paket = st.session_state[ns + "paket"]
    jawaban = st.session_state.get(ns + "jawaban_final", {})
    # Bila submit otomatis, ambil jawaban terakhir dari widget
    if not jawaban:
        jawaban = {}
        for i, s in enumerate(paket):
            teks = st.session_state.get(f"{ns}soal_{i}")
            jawaban[i] = teks

    benar = 0
    for i, s in enumerate(paket):
        teks_pilih = jawaban.get(i)
        if teks_pilih is None:
            continue
        # cocokkan teks pilihan -> indeks asli opsi
        for orig_idx, teks in s["opts"]:
            if teks == teks_pilih:
                if orig_idx == s["a_asli"]:
                    benar += 1
                break

    total = len(paket)
    nilai = round(benar / total * 100, 1) if total else 0
    durasi = int(time.time() - st.session_state[ns + "start_ts"])
    pindah = baca_pindah_tab()

    st.session_state[ns + "hasil"] = {
        "benar": benar, "total": total, "nilai": nilai,
        "durasi": durasi, "pindah": pindah, "otomatis": otomatis,
    }

    # Simpan ke Google Sheet
    status, pesan = False, "Mode offline."
    if _SHEETS_ADA:
        catatan = "Waktu habis (auto submit)" if otomatis else "Selesai normal"
        if pindah > 0:
            catatan += f"; pindah tab {pindah}x"
        status, pesan = sheets.simpan_hasil(
            st.session_state[ns + "nama"], st.session_state[ns + "npm"],
            nilai, benar, total, pindah_tab=pindah, durasi_detik=durasi,
            catatan=catatan, jenis=jenis,
        )
    st.session_state[ns + "simpan_status"] = status
    st.session_state[ns + "simpan_pesan"] = pesan
    st.session_state[ns + "selesai"] = True


def _tampilkan_hasil(ns, judul, jenis):
    h = st.session_state[ns + "hasil"]
    st.success(f"{judul} selesai. Terima kasih, {st.session_state[ns+'nama']}.")
    if h["otomatis"]:
        st.warning("Waktu habis. Jawaban dikirim otomatis.")

    c1, c2, c3 = st.columns(3)
    c1.metric("Nilai", h["nilai"])
    c2.metric("Benar", f"{h['benar']}/{h['total']}")
    c3.metric("Waktu", f"{h['durasi']//60}m {h['durasi']%60}d")

    if h["pindah"] > 0:
        st.warning(f"Tercatat berpindah tab / meninggalkan halaman **{h['pindah']} kali**.")

    if st.session_state.get(ns + "simpan_status"):
        st.info("✅ " + st.session_state.get(ns + "simpan_pesan", ""))
    else:
        st.error("⚠️ " + st.session_state.get(ns + "simpan_pesan", "Hasil belum tersimpan online."))
        st.caption("Screenshot halaman ini sebagai bukti dan laporkan ke dosen bila diminta.")

    st.caption("Halaman ini terkunci. Ujian tidak dapat diulang.")


# ============================================================
#  NAVIGASI
# ============================================================
def main():
    st.sidebar.title("Navigasi")
    menu = st.sidebar.radio("Menu", ["Beranda", "Materi", "Tugas", "UAS"])
    st.sidebar.divider()
    st.sidebar.caption("E-Business · UM Metro\nArdiansyah Japlani, S.E., M.B.A.")

    if menu == "Beranda":
        halaman_beranda()
    elif menu == "Materi":
        halaman_materi()
    elif menu == "Tugas":
        halaman_tugas()
    elif menu == "UAS":
        halaman_uas()


if __name__ == "__main__":
    main()
