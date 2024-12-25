import streamlit as st  # type: ignore
import pandas as pd # type: ignore
import tensorflow as tf
from tensorflow.keras.models import load_model  # type: ignore
import numpy as np
import matplotlib.pyplot as plt # type: ignore
from sklearn.preprocessing import MinMaxScaler # type: ignore
import seaborn as sns # type: ignore
import joblib # type: ignore


# -----------FUNCTION-----------
def load_fnn_model():
    model = load_model('Model/FNN_Model.h5')
    return model

def load_dnn_model():
    model = load_model('Model/DNN_Model.h5')
    return model

def load_rf_model():
    model = joblib.load('Model/RF_Model.pkl')  
    return model

def predict_fnn(model, input_data):
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def predict_dnn(model, input_data):
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def predict_rf(model, input_data):
    input_data = np.array(input_data).reshape(1, -1)
    probability = model.predict_proba(input_data)
    prediction = model.predict(input_data)
    return prediction, probability

# -----------FUNCTION-----------


# -----------CSS SISTEM-----------

st.set_page_config(page_title="Student Academic Success Classification", page_icon="✨", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #1e3c72, #2a5298, #3b6978, #607d8b);
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stSlider > div > div > div > input {
        background-color: orange !important; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------CSS SISTEM-----------



# -----------SIDEBAR-----------

st.sidebar.title('Pilih Model untuk Prediksi')
model_option = st.sidebar.selectbox(
    'Pilih model yang ingin digunakan :',
    ['Feedforward Neural Network (FNN)', 'Deep Neural Network (DNN)', 'Random Forest'],
    help="Pilih model yang ingin digunakan untuk prediksi (Feedforward Neural Network (FNN), Deep Neural Network (DNN)) atau Random Forest."
)

st.sidebar.markdown("---")

st.sidebar.title("ℹ️ Tentang Sistem ℹ️")
st.sidebar.info(
    """
    Dibangun menggunakan :
    - **[Streamlit](https://streamlit.io/)** untuk antarmuka.
    - Terdapat 3 (Tiga) Pilihan Model antara lain ; **Feedforward Neural Network (FNN)**, **Deep Neural Network (DNN)** dan **Random Forest** untuk Klasifikasi Kesuksesan Akademik Mahasiswa.
    - Python untuk prediksi/klasifikasi.
    
    🚀 Jelajahi potensi analisis dalam memprediksi kesuksesan akademik mahasiswa!!
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("Dikembangkan oleh Fathul Agit Darmawan ❤️")


# -----------SIDEBAR-----------


# -----------ANTARMUKA INPUTAN-----------

st.markdown(
    """
    <h1 style="text-align: center; color: white;">SISTEM KLASIFIKASI KESUKSESAN AKADEMIK MAHASISWA</h1>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: justify; color: white;">
    Sistem ini bertujuan untuk mengklasifikasikan kesuksesan akademik mahasiswa berdasarkan berbagai faktor, seperti lokasi geografis, latar belakang pribadi, dan aktivitas akademik lainnya. 
    Dengan memanfaatkan model klasifikasi deep learning dan machine learning, sistem ini akan memprediksi tingkat kesuksesan akademik mahasiswa selama proses perkuliahan.
    </div>

    <div style="margin-top: 20px; color: white; font-size: 14px; font-weight: bold; text-align: justify;">
        <p>Tata Cara Menjalankan Sistem:</p>
        <ul style="text-align: justify;">
            <li>Silakan gulir ke bawah pada bagian <b>Input Data</b>, lalu isi semua data yang diperlukan 🔽</li>
            <li>Setelah data diinputkan, sebelum menekan/mengklik tombol <b>Prediksi</b>, silakan pilih model yang akan digunakan. Pemilihan model tersedia pada bagian <b>sidebar</b> di sebelah kiri layar Anda 🔧</li>
            <li>Setelah memilih model, Anda dapat mengklik tombol <b>Prediksi</b> untuk melihat hasil prediksinya ▶️</li>
            <li>Setelah hasil prediksi model keluar, Anda juga dapat mengganti model lain untuk melakukan prediksi hanya dengan cara memilih model yang berbeda dan mengklik kembali tombol prediksi 🔄</li>
            <li><b>Selamat mencoba</b> 🎉</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    """
    <h1 style="text-align: center; color: white;">INPUT DATA</h1>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h3 style="font-size: 20px; text-align: justify; color: white;">Silakan masukkan data anda di bawah ini untuk melakukan prediksi kesuksesan akademik.</h3>
    <p style="font-size: 14px; text-align: justify; color: white;">
        <small>Untuk melihat detail pertanyaan, klik ikon <span style="font-size: 12px; border: 2px solid white; border-radius: 50%; padding: 3px; background-color: transparent; margin-left: 3px; margin-right: 3px; display: inline-flex; justify-content: center; align-items: center; width: 15px; height: 15px;">?</span> di sebelah kanan.</small>
    </p>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    div[data-testid="stExpander"] {
        color: white !important;
        background-color: transparent !important;
    }
    div[data-testid="stExpander"]:hover {
        color: orange !important;
    }

    /* Kecualikan expander di sidebar */
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        color: initial !important; /* Warna bawaan sidebar */
        background-color: initial !important; /* Warna bawaan sidebar */
    }
    label {
        color: white !important; 
    }
    .st-cf {
        color: white !important; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.expander("Informasi Pribadi"):
    gender = st.selectbox('Jenis Kelamin', [1, 0], help="1 - Pria, 0 - Wanita")
    marital_status_options = {
        'Lajang': 1,
        'Menikah': 2,
        'Duda': 3,
        'Bercerai': 4,
        'Bersatu Secara Hukum': 5,
        'Berpisah Secara Hukum': 6
    }
    marital_status = marital_status_options[st.selectbox('Status Pernikahan', list(marital_status_options.keys()))]
    debtor = ['Tidak', 'Iya'].index(st.selectbox('Memiliki Hutang', ['Iya', 'Tidak']))
    education_needs = ['Tidak Memiliki Kebutuhan', 'Memiliki Kebutuhan'].index(st.selectbox('Kebutuhan Pendidikan Khusus', ['Memiliki Kebutuhan', 'Tidak Memiliki Kebutuhan']))
    
with st.expander("Pendidikan & Kualifikasi Sebelumnya"):
    previous_qualification_options = {
        "Pendidikan menengah": 1,
        "Pendidikan tinggi - sarjana": 2,
        "Pendidikan tinggi - gelar": 3,
        "Pendidikan tinggi - magister": 4,
        "Pendidikan tinggi - doktor": 5,
        "Frekuensi pendidikan tinggi": 6,
        "12 tahun sekolah - tidak tamat": 9,
        "11 tahun sekolah - tidak tamat": 10,
        "Lainnya - 11 tahun sekolah": 12,
        "10 tahun sekolah": 14,
        "10 tahun sekolah - tidak tamat": 15,
        "Pendidikan dasar siklus ke-3 (tahun ke-9/10/11) atau setara": 19,
        "Pendidikan dasar siklus ke-2 (tahun ke-6/7/8) atau setara": 38,
        "Kursus spesialisasi teknologi": 39,
        "Pendidikan tinggi - gelar (siklus pertama)": 40,
        "Kursus teknis profesional yang lebih tinggi": 42,
        "Pendidikan tinggi - master (siklus ke-2)": 43
    }
    previous_qualification = previous_qualification_options[st.selectbox('Kualifikasi Pendidikan Sebelumnya', list(previous_qualification_options.keys()))]
    previous_qualification_grade = st.slider('Nilai Kualifikasi Sebelumnya', min_value=80, max_value=200, help="Nilai kualifikasi sebelumnya (antara 0 hingga 200)")

with st.expander("Kualifikasi & Pekerjaan Orang Tua"):
    mothers_qualification_options = {
        "Pendidikan Menengah - Tahun Sekolah ke-12 atau Persamaan": 1,
        "Pendidikan Tinggi - Sarjana": 2,
        "Pendidikan Tinggi - Gelar": 3,
        "Pendidikan Tinggi - Magister": 4,
        "Pendidikan Tinggi - Doktor": 5,
        "Frekuensi Pendidikan Tinggi": 6,
        "Tahun ke-12 Sekolah - Tidak Tamat Sekolah": 9,
        "Tahun ke-11 Sekolah - Tidak Tamat": 10,
        "Kelas 7 (Lama)": 11,
        "Lainnya - Kelas 11 Sekolah": 12,
        "Kelas 10 Sekolah": 14,
        "Kursus Perdagangan Umum": 18,
        "Pendidikan Dasar Siklus 3 (Tahun 9/10/11) atau Setara": 19,
        "Kursus teknis-profesional": 22,
        "Tahun sekolah ke 7": 26,
        "Kursus sekolah menengah umum siklus ke 2": 27,
        "Tahun sekolah ke 9 - Tidak Tamat": 29,
        "Tahun ke 8 sekolah": 30,
        "Tidak diketahui": 34,
        "Tidak bisa membaca atau menulis": 35,
        "Dapat membaca tanpa harus bersekolah tahun ke-4": 36,
        "Pendidikan dasar siklus ke-1 (tahun ke-4/5) atau setara": 37,
        "Pendidikan Dasar Siklus 2 (Tahun 6/7/8) atau Setara": 38,
        "Kursus peminatan teknologi": 39,
        "Pendidikan tinggi - gelar (siklus 1)": 40,
        "Kursus studi tinggi khusus": 41,
        "Kursus teknik tinggi profesional": 42,
        "Pendidikan Tinggi - Magister (siklus ke-2)": 43,
        "Pendidikan Tinggi - Doktor (siklus ke-3)": 44
    }
    mothers_qualification = mothers_qualification_options[st.selectbox('Kualifikasi Ibu', list(mothers_qualification_options.keys()))]
    fathers_qualification_options = {
        "Pendidikan Menengah - Tahun Sekolah ke-12 atau Persamaan": 1,
        "Pendidikan Tinggi - Sarjana": 2,
        "Pendidikan Tinggi - Gelar": 3,
        "Pendidikan Tinggi - Magister": 4,
        "Pendidikan Tinggi - Doktor": 5,
        "Frekuensi Pendidikan Tinggi": 6,
        "Tahun ke-12 Sekolah - Tidak Tamat Sekolah": 9,
        "Tahun ke-11 Sekolah - Tidak Tamat": 10,
        "Kelas 7 (Lama)": 11,
        "Lainnya - Kelas 11 Sekolah": 12,
        "Kursus Komplementer Kelas 2": 13,
        "10 Tahun Sekolah": 14,
        "Kursus Perdagangan Umum": 18,
        "Pendidikan Dasar Siklus 3 (Tahun 9/10/11) atau Setara": 19,
        "Kursus Pelengkap SMA": 20,
        "Kursus Teknis-profesional": 22,
        "Kursus Pelengkap Sekolah Menengah Atas - belum selesai": 25,
        "7 tahun sekolah": 26,
        "Siklus 2 kursus sekolah menengah umum": 27,
        "9 Tahun Sekolah - Belum Tamat": 29,
        "8 tahun sekolah": 30,
        "Kursus Umum Administrasi dan Tata Niaga": 31,
        "Akuntansi dan Administrasi Tambahan": 33,
        "Tidak Diketahui": 34,
        "Tidak bisa membaca atau menulis": 35,
        "Bisa membaca tanpa harus bersekolah tahun ke-4": 36,
        "Pendidikan dasar siklus 1 (tahun ke-4/5) atau setara": 37,
        "Pendidikan Dasar Siklus 2 (Tahun 6/7/8) atau Setara": 38,
        "Kursus peminatan teknologi": 39,
        "Pendidikan tinggi - gelar (siklus 1)": 40,
        "Kursus studi tinggi khusus": 41,
        "Kursus teknik tinggi profesional": 42,
        "Pendidikan Tinggi - Magister (siklus ke-2)": 43,
        "Pendidikan Tinggi - Doktor (siklus ke-3)": 44
    }
    fathers_qualification = fathers_qualification_options[st.selectbox('Kualifikasi Ayah', list(fathers_qualification_options.keys()))]
    mothers_occupation_options = {
        "Mahasiswa": 0,
        "Perwakilan Kekuasaan Legislatif dan Badan Eksekutif, Direktur, Direktur dan Manajer Eksekutif": 1,
        "Spesialis dalam Kegiatan Intelektual dan Ilmiah": 2,
        "Teknisi dan Profesi Tingkat Menengah": 3,
        "Staf Administrasi": 4,
        "Pekerja dan Penjual Layanan Pribadi, Keamanan dan Keselamatan": 5,
        "Petani dan Tenaga Kerja Terampil di Bidang Pertanian, Perikanan dan Kehutanan": 6,
        "Tenaga Kerja Terampil di Bidang Industri, Konstruksi dan Pengrajin": 7,
        "Operator Instalasi dan Mesin dan Pekerja Perakitan": 8,
        "Pekerja Tidak Terampil": 9,
        "Profesi Angkatan Bersenjata": 10,
        "Situasi Lainnya": 90,
        "(kosong)": 99,
        "Tenaga kesehatan": 122,
        "Guru": 123,
        "Spesialis teknologi informasi dan komunikasi (TIK)": 125,
        "Teknisi dan profesi sains dan teknik tingkat menengah": 131,
        "Teknisi dan profesional, dengan tingkat kesehatan menengah": 132,
        "Teknisi tingkat menengah dari bidang hukum, sosial, olah raga, budaya dan jasa serupa": 134,
        "Pekerja kantor, sekretaris umum dan operator pengolahan data": 141,
        "Operator data, akuntansi, statistik, jasa keuangan dan pencatatan": 143,
        "Staf pendukung administrasi lainnya": 144,
        "Pekerja layanan pribadi": 151,
        "Penjual": 152,
        "Pribadi pekerja perawatan dan sejenisnya": 153,
        "Pekerja terampil konstruksi dan sejenisnya, kecuali tukang listrik": 171,
        "Pekerja terampil di bidang percetakan, pembuatan instrumen presisi, pembuat perhiasan, perajin dan sejenisnya": 173,
        "Pekerja di bidang pengolahan makanan, pengerjaan kayu, pakaian dan industri serta kerajinan lainnya": 175,
        "Pekerja kebersihan": 191,
        "Pekerja tidak terampil di bidang pertanian, produksi hewan, perikanan dan kehutanan": 192,
        "Pekerja tidak terampil di industri ekstraktif, konstruksi, manufaktur dan transportasi": 193,
        "Asisten penyiapan makanan": 194
    }
    mothers_occupation = mothers_occupation_options[st.selectbox('Pekerjaan Ibu', list(mothers_occupation_options.keys()))]
    fathers_occupation_options = {
        "Mahasiswa": 0,
        "Perwakilan Badan Legislatif dan Eksekutif, Direktur, Direktur dan Manajer Eksekutif": 1,
        "Spesialis dalam Kegiatan Intelektual dan Ilmiah": 2,
        "Teknisi dan Profesi Tingkat Menengah": 3,
        "Staf Administrasi": 4,
        "Pekerja dan Penjual Layanan Pribadi, Keamanan dan Keselamatan": 5,
        "Petani dan Pekerja Terampil di Pertanian, Perikanan dan Kehutanan": 6,
        "Pekerja Terampil di Industri, Konstruksi dan Pengrajin": 7,
        "Operator Instalasi dan Mesin dan Pekerja Perakitan": 8,
        "Pekerja Tidak Terampil": 9,
        "Profesi Angkatan Bersenjata": 10,
        "Situasi Lainnya": 90,
        "(kosong)": 99,
        "Perwira Angkatan Bersenjata": 101,
        "Sersan Angkatan Bersenjata": 102,
        "Personel Angkatan Bersenjata lainnya": 103,
        "Direktur layanan administrasi dan komersial": 112,
        "Direktur hotel, katering, perdagangan dan layanan lainnya": 114,
        "Spesialis dalam ilmu fisika, matematika, teknik dan teknik terkait": 121,
        "Profesional kesehatan": 122,
        "Guru": 123,
        "Spesialis dalam keuangan, akuntansi, organisasi administrasi, hubungan masyarakat dan komersial": 124,
        "Teknisi dan profesi sains dan teknik tingkat menengah": 131,
        "Teknisi dan profesional, dari tingkat kesehatan menengah": 132,
        "Teknisi tingkat menengah dari layanan hukum, sosial, olahraga, budaya dan sejenisnya": 134,
        "Teknisi teknologi informasi dan komunikasi": 135,
        "Pekerja kantor, sekretaris jenderal dan operator pemrosesan data": 141,
        "Operator data, akuntansi, statistik, layanan keuangan dan terkait pendaftaran": 143,
        "Staf pendukung administrasi lainnya": 144,
        "Pekerja layanan pribadi": 151,
        "Penjual": 152,
        "Pekerja perawatan pribadi dan sejenisnya": 153,
        "Personel layanan perlindungan dan keamanan": 154,
        "Petani berorientasi pasar dan pekerja pertanian dan produksi hewan yang terampil": 161,
        "Petani, pemelihara ternak, nelayan, pemburu dan pengumpul, subsisten": 163,
        "Pekerja konstruksi terampil dan sejenisnya, kecuali teknisi listrik": 171,
        "Pekerja terampil dalam metalurgi, pengerjaan logam dan sejenisnya": 172,
        "Pekerja terampil di bidang listrik dan elektronik": 174,
        "Pekerja di industri pengolahan makanan, pertukangan kayu, pakaian dan industri serta kerajinan lainnya": 175,
        "Operator mesin dan pabrik tetap": 181,
        "Pekerja perakitan": 182,
        "Pengemudi kendaraan dan operator peralatan bergerak": 183,
        "Pekerja tidak terampil di bidang pertanian, produksi hewan, perikanan dan kehutanan": 192,
        "Pekerja tidak terampil di industri ekstraktif, konstruksi, manufaktur dan transportasi": 193,
        "Asisten persiapan makanan": 194,
        "Penjual kaki lima (kecuali makanan) dan penyedia layanan kaki lima": 195
    }
    fathers_occupation = fathers_occupation_options[st.selectbox('Pekerjaan Ayah', list(fathers_occupation_options.keys()))]

with st.expander("Informasi Akademik Personal"):
    age_at_enrollment = st.slider('Usia Saat Pendaftaran', min_value=17, max_value=100, help="Pilih usia saat pendaftaran.")
    attendance = ['Evening', 'Daytime'].index(st.selectbox('Kehadiran Perkuliahan (Daytime/Evening)', ['Daytime', 'Evening']))
    international = ['Domestik', 'Internasional'].index(st.selectbox('Jenis Mahasiswa (Internasional/Domestik)', ['Internasional', 'Domestik']))
    displaced = ['Tidak', 'Iya'].index(st.selectbox('Mahasiswa Luar Daerah', ['Iya', 'Tidak']))
    scholarship_holder = ['Bukan Penerima Beasiswa', 'Penerima Beasiswa'].index(st.selectbox('Beasiswa', ['Penerima Beasiswa', 'Bukan Penerima Beasiswa']))

with st.expander("Unit Kurikulum"):
    curricular_units_1st_sem_enrolled = st.slider('Unit Kurikulum Semester 1 (Terdaftar)', min_value=0, max_value=50, help="Jumlah mata kuliah yang didaftarkan pada semester 1")
    curricular_units_1st_sem_evaluations = st.slider('Unit Kurikulum Semester 1 (Evaluasi)', min_value=0, max_value=50, help="Jumlah evaluasi mata kuliah pada semester 1")
    curricular_units_1st_sem_approved = st.slider('Unit Kurikulum Semester 1 (Disetujui)', min_value=0, max_value=50, help="Jumlah mata kuliah yang disetujui pada semester 1")
    curricular_units_1st_sem_without_evaluations = st.slider('Unit Kurikulum Semester 1 (Tanpa Evaluasi)', min_value=0, max_value=50, help="Jumlah mata kuliah tanpa evaluasi pada semester 1")
    curricular_units_2nd_sem_enrolled = st.slider('Unit Kurikulum Semester 2 (Terdaftar)', min_value=0, max_value=50, help="Jumlah mata kuliah yang didaftarkan pada semester 2")
    curricular_units_2nd_sem_evaluations = st.slider('Unit Kurikulum Semester 2 (Evaluasi)', min_value=0, max_value=50, help="Jumlah evaluasi mata kuliah pada semester 2")
    curricular_units_2nd_sem_approved = st.slider('Unit Kurikulum Semester 2 (Disetujui)', min_value=0, max_value=50, help="Jumlah mata kuliah yang disetujui pada semester 2")
    curricular_units_2nd_sem_without_evaluations = st.slider('Unit Kurikulum Semester 2 (Tanpa Evaluasi)', min_value=0, max_value=50, help="Jumlah mata kuliah tanpa evaluasi pada semester 2")

yes_standarisasi = [
    previous_qualification_grade, age_at_enrollment, 
    curricular_units_1st_sem_enrolled, curricular_units_1st_sem_evaluations,
    curricular_units_1st_sem_approved, curricular_units_1st_sem_without_evaluations,
    curricular_units_2nd_sem_enrolled, curricular_units_2nd_sem_evaluations, 
    curricular_units_2nd_sem_approved, curricular_units_2nd_sem_without_evaluations
]

no_standarisasi = [
    marital_status, attendance, previous_qualification, mothers_qualification, 
    fathers_qualification, mothers_occupation, fathers_occupation, displaced, 
    education_needs, debtor, gender, scholarship_holder, international
]

scaler = joblib.load('Normalisasi/scaler.pkl')
yes_standarisasi_standardized = scaler.transform([yes_standarisasi])[0]

marital_status = marital_status
attendance = attendance
previous_qualification = previous_qualification
previous_qualification_grade = yes_standarisasi_standardized[0]
age_at_enrollment = yes_standarisasi_standardized[1]
curricular_units_1st_sem_enrolled = yes_standarisasi_standardized[2]
curricular_units_1st_sem_evaluations = yes_standarisasi_standardized[3]
curricular_units_1st_sem_approved = yes_standarisasi_standardized[4]
curricular_units_1st_sem_without_evaluations = yes_standarisasi_standardized[5]
curricular_units_2nd_sem_enrolled = yes_standarisasi_standardized[6]
curricular_units_2nd_sem_evaluations = yes_standarisasi_standardized[7]
curricular_units_2nd_sem_approved = yes_standarisasi_standardized[8]
curricular_units_2nd_sem_without_evaluations = yes_standarisasi_standardized[9]

input_data = [
    marital_status, attendance, previous_qualification, previous_qualification_grade,
    mothers_qualification, fathers_qualification, mothers_occupation, fathers_occupation,
    displaced, education_needs, debtor, gender, scholarship_holder, age_at_enrollment,
    international, curricular_units_1st_sem_enrolled, curricular_units_1st_sem_evaluations,
    curricular_units_1st_sem_approved, curricular_units_1st_sem_without_evaluations, 
    curricular_units_2nd_sem_enrolled, curricular_units_2nd_sem_evaluations, 
    curricular_units_2nd_sem_approved, curricular_units_2nd_sem_without_evaluations
]

columns = [
    'marital_status', 'attendance', 'previous_qualification', 'previous_qualification_grade',
    'mothers_qualification', 'fathers_qualification', 'mothers_occupation', 'fathers_occupation',
    'displaced', 'education_needs', 'debtor', 'gender', 'scholarship_holder', 'age_at_enrollment',
    'international', 'curricular_units_1st_sem_enrolled', 'curricular_units_1st_sem_evaluations',
    'curricular_units_1st_sem_approved', 'curricular_units_1st_sem_without_evaluations',
    'curricular_units_2nd_sem_enrolled', 'curricular_units_2nd_sem_evaluations',
    'curricular_units_2nd_sem_approved', 'curricular_units_2nd_sem_without_evaluations'
]

input_data_standardized_df = pd.DataFrame([input_data], columns=columns)

# -----------ANTARMUKA INPUTAN-----------


# -----------PREDICTION-----------

if st.button("Prediksi"):
    if model_option == 'Feedforward Neural Network (FNN)':
        model = load_fnn_model()
        prediction = predict_fnn(model, input_data)
    
    elif model_option == 'Deep Neural Network (DNN)':
        model = load_dnn_model()
        prediction = predict_dnn(model, input_data)

    elif model_option == 'Random Forest':
        model = load_rf_model()
        prediction, probability = predict_rf(model, input_data)

    labels = ['Dropout', 'Enrolled', 'Graduate']
    
    if model_option == 'Random Forest':
        result_index = np.argmax(probability)  
        result_label = labels[result_index]
        confidence_scores = probability[0]
    else:
        result_index = np.argmax(prediction) 
        result_label = labels[result_index]
        confidence_scores = prediction[0] if len(prediction.shape) > 1 else prediction

    if len(confidence_scores) == 1:
        confidence_scores = np.repeat(confidence_scores, len(labels))  
    
    label_colors = {
        'Graduate': 'green',
        'Dropout': 'red',
        'Enrolled': 'gray'
    }
    label_color = label_colors[result_label]

    st.markdown("### Hasil Input Data")
    st.table(input_data_standardized_df)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("---")
        st.markdown(
            f"""
            <h2 style='text-align: center; color:rgb(246, 244, 244);'>Hasil Prediksi</h2>
            <h3 style='text-align: center; color: {label_color}; font-weight: bold;'>
                <strong>{result_label}</strong>
            </h3>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"Confidence untuk label yang diprediksi: **{confidence_scores[result_index] * 100:.2f}%**", unsafe_allow_html=True)

    with col2:
        st.markdown("---")
        fig, ax = plt.subplots()
        sns.barplot(x=labels, y=confidence_scores, ax=ax)
        ax.set_title('Confidence Score untuk Setiap Label')
        ax.set_ylabel('Confidence')
        ax.set_xlabel('Label')
        st.pyplot(fig)

    st.markdown("---")
    st.markdown("### Confidence Score untuk Semua Label")
    prediction_df = pd.DataFrame({
        'Label': labels,
        'Confidence': confidence_scores
    })
    
    prediction_df['Confidence'] = prediction_df['Confidence'].apply(lambda x: f"{x*100:.2f}%")
    prediction_df = prediction_df.style.apply(
        lambda x: [
            f'background: linear-gradient(to right, #1e3c72, #2a5298, #3b6978, #607d8b)' if i == result_index else ''
            for i in range(len(x))
        ],
        axis=1
    )
    
    st.table(prediction_df)
    st.markdown("---")

    
# -----------PREDICTION-----------
