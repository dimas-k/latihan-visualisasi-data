# Analisis Data 

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan data wrangling dan eksplorasi visualisasi data guna memahami pola, tren, dan distribusi dari dataset yang digunakan. Analisis ini mencakup pembersihan data, transformasi, serta visualisasi berbagai aspek penting dari data.

## Fitur Utama

1. Data Wrangling

   - Pembersihan data (handling missing values, duplicates, dll.)

   - Transformasi tipe data yang diperlukan

   - Normalisasi atau standarisasi fitur

2. Analisis Eksploratori Data (EDA)

   - Statistik deskriptif

   - Korelasi antar fitur numerik

   - Distribusi data

   - Distribusi berdasarkan kategori produk

3. Visualisasi Data

   - Heatmap untuk korelasi antar fitur numerik

   - Histogram dan boxplot untuk melihat distribusi data

   - Barplot untuk analisis berdasarkan kategori produk

4. Dashboard Interaktif (Streamlit)

   - Menampilkan ringkasan data dalam bentuk tabel dan grafik interaktif

   - Navigasi data dengan fitur pagination

   - Visualisasi kategori produk berdasarkan berat dan panjang produk

   - Statistik deskriptif yang dapat diakses langsung dari dashboard

## Instalasi dan Penggunaan

1. Instalasi Dependensi

Pastikan Python sudah terinstal di sistem Anda. Kemudian, instal dependensi yang diperlukan dengan perintah berikut:

`pip install -r requirements.txt`

2. Menjalankan Notebook

Buka Jupyter Notebook atau Google Colab, lalu jalankan skrip utama untuk melakukan analisis data:
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
3. Menjalankan Dashboard (Streamlit)

Untuk menjalankan dashboard interaktif berbasis Streamlit, jalankan perintah berikut:

`streamlit run dashboard/dashboard.py`

Kemudian buka browser dan akses http://localhost:8501/ untuk melihat dashboard.

Ataupun bisa diakses dari URL berikut : [Akses Streamlit]().

Struktur Proyek

├── dashboard/              # Folder untuk dashboard interaktif
│   ├── dashboard.py        # Script utama untuk Streamlit
│   ├── products_dataset.csv # Dataset yang digunakan dalam dashboard
├── data/                   # Folder untuk menyimpan dataset mentah
│   ├── order_items_dataset.csv
│   ├── order_reviews_dataset.csv
├── notebook.ipynb          # Notebook untuk analisis dan visualisasi data
├── readme.md               # Dokumentasi proyek
├── requirements.txt        # Daftar dependensi proyek
├── url.txt                 # File berisi sumber dataset

## Hasil Analisis

1. Dataset telah berhasil dibersihkan dan diubah ke format yang lebih sesuai.

2. Korelasi antar fitur menunjukkan adanya beberapa variabel yang memiliki hubungan erat.

3. Distribusi data menunjukkan beberapa fitur memiliki skewness yang perlu diperhatikan.

4. Analisis kategori produk memberikan wawasan tentang produk yang memiliki berat dan panjang terbesar.

5. Dashboard interaktif memungkinkan eksplorasi lebih lanjut secara visual.

## Deskripsi Dashboard

Dashboard ini dibangun menggunakan Streamlit untuk memvisualisasikan hasil analisis data. Beberapa fitur utama dari dashboard meliputi:

1. Tampilan Data Produk: Menampilkan tabel data dengan fitur navigasi halaman.

2. Statistik Deskriptif: Menampilkan ringkasan statistik dataset.

3. Visualisasi Produk Terberat: Menampilkan kategori produk dengan berat terbesar dalam bentuk bar chart.

4. Visualisasi Produk Terpanjang: Menampilkan kategori produk dengan panjang terbesar dalam bentuk bar chart.

5. Navigasi Interaktif: Pengguna dapat berpindah halaman data dengan tombol "Previous" dan "Next".

## Kesimpulan

Visualisasi data membantu dalam memahami pola dan distribusi yang ada dalam dataset. Hasil analisis ini dapat digunakan untuk pengambilan keputusan lebih lanjut, seperti strategi pemasaran atau optimasi model prediktif.

Dashboard interaktif berbasis Streamlit memberikan pengalaman eksplorasi data yang lebih baik dengan kemudahan navigasi dan analisis mendalam.