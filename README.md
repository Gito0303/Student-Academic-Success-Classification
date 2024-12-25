***

# <h1 align="center">STUDENT ACADEMIC SUCCESS CLASSIFICATION</h1>

---

<div align="center">
  <img src="https://www.timeshighereducation.com/sites/default/files/examination.jpg" alt="Gambar Utama" width="500" height="300">
  <p>
    <small>
      Sumber Image : <a href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.timeshighereducation.com%2Fnews%2Fresits-may-not-improve-academic-performance-says-study&psig=AOvVaw1mluvoCDrThnANFwtZHIJk&ust=1734925003299000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJD1z7e5uooDFQAAAAAdAAAAABAE">Access Here.....</a>
    </small>
  </p>
</div>

# <h1 align="center">TABLE OF CONTENT</h1>

---

1. [Deskripsi Project](#-deskripsi-project-)
      - [Latar Belakang](#latar-belakang)
      - [Tujuan Pengembangan](#tujuan-pengembangan)
2. [Sumber Dataset](#-sumber-dataset-)
3. [Preprocessing dan Pemodelan](#-preprocessing-dan-pemodelan-)
      - [Pemilihan Kolom/Atribut](#pemilihan-kolomatribut)
      - [Preprocessing Data](#preprocessing-data)
      - [Pemodelan](#pemodelan)
4. [Langkah Instalasi](#-langkah-instalasi-)
      - [Software Utama](#software-utama)
      - [Dependensi](#dependensi)
      - [Menjalankan Sistem Prediksi](#menjalankan-sistem-prediksi)
      - [Pelatihan Model](#pelatihan-model)

---


<h1 align="center">📚 Deskripsi Project 📚</h1>

Proyek ini bertujuan untuk **mengembangkan sistem klasifikasi kesuksesan akademik mahasiswa** berdasarkan berbagai faktor yang berkontribusi terhadap keberhasilan akademik. Sistem ini akan menggunakan beberapa model **Deep Learning** dan **Machine Learning** seperti **Feedforward Neural Network (FNN)**, **Deep Neural Network (DNN)**, dan **Random Forest** untuk memprediksi kategori keberhasilan mahasiswa.

---

### **Latar Belakang**

Klasifikasi ini didasarkan pada berbagai faktor yang mempengaruhi kesuksesan akademik mahasiswa, yang mencakup:

- 📊 **Faktor Demografis**
- 🎓 **Faktor Pendidikan**
- 🌍 **Faktor Geografis**
- 💰 **Faktor Keuangan**
- 📚 **Faktor Akademik**
- 🕒 **Faktor Kehadiran**

Tujuan utama dari klasifikasi ini adalah untuk memprediksi status akademik mahasiswa menjadi salah satu dari tiga kategori berikut:

#### 🔍 **Kategori Status Akademik:** 🔍

- **Dropout**: Mahasiswa yang berhenti kuliah sebelum menyelesaikan program studinya.
- **Enrolled**: Mahasiswa yang masih terdaftar aktif dan sedang melanjutkan proses perkuliahan.
- **Graduate**: Mahasiswa yang menyelesaikan program studi dan lulus.

---

### **Tujuan Pengembangan**

1. **Membangun Model Klasifikasi** untuk memprediksi status akademik mahasiswa (Dropout, Enrolled, Graduate) berdasarkan faktor-faktor yang tersedia.
   
2. **Evaluasi Performa Model**: Menguji beberapa model **Deep Learning** dan **Machine Learning**, seperti **Feedforward Neural Network (FNN)**, **Deep Neural Network (DNN)**, dan **Random Forest**, untuk mendapatkan hasil klasifikasi terbaik.
   
3. **Membangun Sistem Klasifikasi dengan Streamlit**: Menciptakan aplikasi berbasis web yang memudahkan pengguna untuk mengakses dan menggunakan model klasifikasi ini secara langsung.

---


<h1 align="center">📊 Sumber Dataset 📊</h1>


Dataset yang digunakan dalam proyek ini berasal dari satu sumber utama:

### 1. **Kaggle**

- **Judul Dataset**: *Classification with an Academic Success Dataset*
- **Link**: [Kaggle - Playground Series S4E6](https://www.kaggle.com/competitions/playground-series-s4e6)
- **Deskripsi**: Dataset ini berisi data pelatihan (train.csv) dengan total **76.518 entri** dan **37 kolom** (36 fitur dan 1 target). Dataset ini dibuat dari model pembelajaran mendalam yang dilatih menggunakan data asli, yaitu **Predict Students Dropout and Academic Success** dari **UC Irvine Machine Learning Repository**, dengan distribusi fitur yang hampir sama namun tidak identik.

#### **Data Asli** (seperti yang dijelaskan dalam deskripsi Kaggle):

- **Judul Dataset**: *Predict Students Dropout and Academic Success*
- **Link**: [UC Irvine - Predict Students Dropout and Academic Success](https://archive.ics.uci.edu/ml/datasets/Predict+Students+Dropout+and+Academic+Success)
- **Deskripsi**: Dataset ini mencakup data dari beberapa institusi pendidikan tinggi yang berisi informasi tentang mahasiswa dari berbagai jurusan seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi. Data mencakup faktor akademik, demografi, dan sosial-ekonomi yang diketahui saat pendaftaran, serta kinerja akademik mahasiswa pada semester pertama dan kedua.

---

<h1 align="center">🧑‍💻 Preprocessing dan Pemodelan 🧑‍💻</h1>


### Pemilihan Kolom/Atribut

Atribut yang digunakan dalam project ini adalah **24 Kolom** dari **37 Kolom** yang ada didalam Dataset yang digunakan. Kolom-kolom tersebut dijelaskan pada tabel dibawah ini.

| Kolom                                         | Tipe        | Deskripsi                                                                                   |
|-----------------------------------------------|-------------|---------------------------------------------------------------------------------------------|
| **Marital Status**                            | Integer     | Status pernikahan: 1 – single, 2 – married, dll.                                            |
| **Daytime/evening attendance**                | Integer     | Mode kehadiran: 1 – siang, 0 – malam.                                                       |
| **Previous qualification**                    | Integer     | Kualifikasi pendidikan sebelumnya (misal: pendidikan menengah, sarjana, magister, dll.).    |
| **Previous qualification (grade)**            | Continuous  | Nilai kualifikasi pendidikan sebelumnya (antara 0 hingga 200).                              |
| **Mother's qualification**                    | Integer     | Kualifikasi pendidikan ibu (misal: pendidikan menengah, sarjana, magister, dll.).           |
| **Father's qualification**                    | Integer     | Kualifikasi pendidikan ayah (misal: pendidikan menengah, sarjana, magister, dll.).          |
| **Mother's occupation**                       | Integer     | Pekerjaan ibu (misal: 0 – pelajar, 1 – perwakilan legislatif, 2 – ilmuwan, dll.).           |
| **Father's occupation**                       | Integer     | Pekerjaan ayah (misal: 0 – pelajar, 1 – perwakilan legislatif, 2 – ilmuwan, dll.).          |
| **Displaced**                                 | Integer     | Apakah mahasiswa berasal dari luar daerah? (1 - ya, 0 - tidak)                              |
| **Educational special needs**                 | Integer     | Apakah mahasiswa memiliki kebutuhan pendidikan khusus? (1 - ya, 0 - tidak)                 |
| **Debtor**                                    | Integer     | Apakah mahasiswa memiliki hutang? (1 - ya, 0 - tidak)                                       |
| **Gender**                                    | Integer     | Jenis kelamin mahasiswa (1 - laki-laki, 0 - perempuan)                                      |
| **Scholarship holder**                        | Integer     | Apakah mahasiswa penerima beasiswa? (1 - ya, 0 - tidak)                                      |
| **Age at enrollment**                         | Integer     | Usia mahasiswa saat pendaftaran                                                             |
| **International**                             | Integer     | Apakah mahasiswa internasional? (1 - ya, 0 - tidak)                                          |
| **Curricular units 1st sem (enrolled)**       | Integer     | Jumlah mata kuliah yang didaftarkan pada semester 1                                         |
| **Curricular units 1st sem (evaluations)**    | Integer     | Jumlah evaluasi mata kuliah pada semester 1                                                  |
| **Curricular units 1st sem (approved)**       | Integer     | Jumlah mata kuliah yang disetujui pada semester 1                                            |
| **Curricular units 1st sem (without evaluations)** | Integer  | Jumlah mata kuliah tanpa evaluasi pada semester 1                                           |
| **Curricular units 2nd sem (enrolled)**       | Integer     | Jumlah mata kuliah yang didaftarkan pada semester 2                                         |
| **Curricular units 2nd sem (evaluations)**    | Integer     | Jumlah evaluasi mata kuliah pada semester 2                                                  |
| **Curricular units 2nd sem (approved)**       | Integer     | Jumlah mata kuliah yang disetujui pada semester 2                                            |
| **Curricular units 2nd sem (without evaluations)** | Integer  | Jumlah mata kuliah tanpa evaluasi pada semester 2                                           |
| **Target**                                    | Categorical | Target. Masalah ini diformulasikan sebagai tugas klasifikasi tiga kategori (dropout, enrolled, graduate) |

### Preprocessing Data

1. **Transformasi Data**:
   - **Label encoding** dilakukan pada kolom **Target** untuk mengubah kategori menjadi angka.
   - **MinMax scaling** diterapkan pada kolom berikut untuk normalisasi:
     - `Previous qualification (grade)`
     - `Age at enrollment`
     - `Curricular units 1st sem (enrolled)`
     - `Curricular units 1st sem (evaluations)`
     - `Curricular units 1st sem (approved)`
     - `Curricular units 1st sem (without evaluations)`
     - `Curricular units 2nd sem (enrolled)`
     - `Curricular units 2nd sem (evaluations)`
     - `Curricular units 2nd sem (approved)`
     - `Curricular units 2nd sem (without evaluations)`

2. **Pembagian Data**:
   - Data dibagi menjadi **80%** untuk pelatihan dan **20%** untuk pengujian.

---

### Pemodelan

Model yang digunakan dalam proyek ini meliputi:

1. **Feedforward Neural Network (FNN)**:
   - Model jaringan saraf sederhana di mana data bergerak satu arah dari input ke output tanpa loop.
   - Digunakan untuk tugas klasifikasi atau regresi.

2. **Deep Neural Network (DNN)**:
   - Jaringan saraf dengan beberapa lapisan tersembunyi yang memungkinkan model menangkap pola yang lebih kompleks dalam data.

3. **TabNet**:
   - Model deep learning yang dirancang khusus untuk data tabular.
   - Menggunakan teknik perhatian (attention) untuk memproses fitur secara efisien.

4. **Random Forest**:
   - Algoritma ensemble yang menggunakan banyak pohon keputusan untuk meningkatkan akurasi.
   - Menggabungkan prediksi dari banyak model pohon yang dilatih pada data yang berbeda.

---

<h1 align="center">🔧 Langkah Instalasi 🔧</h1>

### Software Utama
Proyek ini dapat dijalankan menggunakan Google Colab dan VSCode. Pastikan Python 3.10.16 telah terinstal di sistem Anda.

### Dependensi
Dependensi yang diperlukan untuk menjalankan proyek ini telah disediakan dalam file [requirements.txt](requirements.txt) di direktori ini. Anda dapat menginstal seluruh dependensi dengan salah satu cara berikut:

#### Cara 1: Instalasi Langsung
Jalankan perintah berikut di terminal:
```bash
pip install -r requirements.txt
```

#### Cara 2: Instalasi Manual
Anda juga dapat menginstal dependensi satu per satu menggunakan perintah seperti berikut:
```bash
pdm add streamlit==1.37.0
```

> Lakukan hal yang sama untuk semua dependensi yang tersedia di [requirements.txt](requirements.txt)

### Menjalankan Sistem Prediksi
Untuk menjalankan sistem prediksi, buka terminal dan jalankan file [App.py](App.py) dengan perintah berikut:
```bash
streamlit run App.py
```

> Jika anda ingin lansung melihat penggunaan Sistem Prediksi dari project ini, Lihat bagian [Link Live Demo](#link-live-demo)

### Pelatihan Model
Model yang telah dilatih tersedia di direktori [Model](Model). Namun dalam hal ini, untuk Model Random Forest tidak dapat diupload kedalam direktori github karena keterbatasan ukuran file. Berikut disediakan Model Random Forest dalam bentuk link Google Drive.

> [Google Drive - Model Save Pelatihan Random Forest (klik)](https://drive.google.com/file/d/1RUcgZssSWjpJDrqSlsi22FPMO2JSEkTo/view?usp=sharing)

Jika Anda ingin melatih model dari awal, jalankan file [Notebook-Model.ipynb](Notebook-Model.ipynb) yang tersedia di direktori ini menggunakan Google Colab.


---

