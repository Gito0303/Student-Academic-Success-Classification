# Panduan Penggunaan

Berikut adalah cara menggunakan aplikasi prediksi kesuksesan akademik mahasiswa yang dibangun menggunakan **Streamlit**.

## 1. Menjalankan Aplikasi

Setelah mengikuti langkah-langkah instalasi dan menjalankan aplikasi dengan perintah:
```bash
streamlit run App.py
```
Aplikasi akan muncul di browser Anda.

## 2. Input Data

Pada aplikasi, pengguna akan diminta untuk mengisi beberapa informasi terkait mahasiswa, seperti:
- **Status pernikahan**
- **Mode kehadiran**
- **Kualifikasi pendidikan sebelumnya**
- **Pekerjaan orang tua**
- **Faktor keuangan**
- **Usia pada saat pendaftaran**

## 3. Menjalankan Prediksi

Setelah memasukkan semua data, pengguna dapat mengklik tombol **Prediksi** untuk mendapatkan hasil klasifikasi status akademik mahasiswa.

### Hasil Prediksi
Hasil prediksi akan menunjukkan salah satu dari tiga kategori status akademik:
- **Dropout**: Mahasiswa berisiko keluar.
- **Enrolled**: Mahasiswa masih terdaftar.
- **Graduate**: Mahasiswa berhasil lulus.

Skor **confidence** akan ditampilkan di bawah setiap kategori.

### 4. Melihat Visualisasi

Aplikasi ini juga menampilkan visualisasi dari distribusi prediksi serta metrik terkait.
