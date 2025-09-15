# Model yang Digunakan

Proyek ini menggunakan beberapa model pembelajaran mesin untuk melakukan klasifikasi kesuksesan akademik mahasiswa. Berikut adalah model-model yang digunakan dalam proyek ini:

## 1. Feedforward Neural Network (FNN)

Feedforward Neural Network (FNN) adalah jaringan saraf yang sederhana di mana data bergerak satu arah dari input ke output tanpa loop. Ini adalah model jaringan saraf yang paling dasar dan digunakan untuk tugas klasifikasi atau regresi.

### Arsitektur:
- **Lapisan input**: Menyusun data fitur mahasiswa.
- **Lapisan tersembunyi**: Menggunakan fungsi aktivasi seperti ReLU untuk menangkap pola kompleks.
- **Lapisan output**: Menghasilkan prediksi tentang status akademik mahasiswa (Dropout, Enrolled, Graduate).

### Link Resmi:
- **Website**: `https://www.tensorflow.org/`

### Instalasi:
```bash
pip install tensorflow==2.16.2
```

## 2. Deep Neural Network (DNN)

Deep Neural Network (DNN) adalah jaringan saraf dengan banyak lapisan tersembunyi, yang memungkinkan model untuk menangkap pola yang lebih kompleks dalam data. DNN sering digunakan untuk masalah yang melibatkan data yang sangat besar dan kompleks.

### Arsitektur:
- **Lapisan input**: Menyusun data mahasiswa.
- **Beberapa lapisan tersembunyi**: Menggunakan fungsi aktivasi untuk menangkap representasi data yang lebih abstrak.
- **Lapisan output**: Menyajikan prediksi status akademik mahasiswa.

### Link Resmi:
- **Website**: `https://www.tensorflow.org/`

### Instalasi:
```bash
pip install tensorflow==2.16.2
```

## 3. Random Forest

Random Forest adalah algoritma ensemble yang menggunakan banyak pohon keputusan untuk meningkatkan akurasi model. Random Forest menggabungkan prediksi dari banyak model pohon yang dilatih pada data yang berbeda untuk menghasilkan hasil yang lebih stabil dan akurat.

### Proses:
- Banyak pohon keputusan dibangun dengan menggunakan sampel acak dari data.
- Hasil prediksi dari masing-masing pohon digabungkan untuk membuat prediksi akhir.

### Link Resmi:
- **Website**: `https://scikit-learn.org/`

### Instalasi:
```bash
pip install scikit-learn==0.24.0
```
