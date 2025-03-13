# **Analisis Data Penjualan E-Commerce**

## **Deskripsi Proyek**
Proyek ini bertujuan untuk menganalisis data penjualan dari sebuah platform e-commerce dalam beberapa bulan terakhir. Fokus utama dari analisis ini adalah mengidentifikasi kategori produk terlaris, pola penjualan, serta faktor-faktor yang mempengaruhi harga dan keuntungan. Data yang digunakan mencakup informasi pesanan, produk, dan kategori produk.

## **Dataset yang Digunakan**
Dataset yang digunakan dalam analisis ini meliputi:
- **orders.csv**: Data pesanan pelanggan beserta timestamp.
- **order_items.csv**: Detail produk dalam setiap pesanan.
- **products.csv**: Informasi produk termasuk kategori.

## **Instalasi dan Penggunaan**
Untuk menjalankan analisis ini, pastikan Anda memiliki Python dan pustaka berikut terinstal:

```bash
pip install -r requirements.txt
```

### **Menjalankan Notebook**
1. Buka file notebook: `notebook.ipynb`
2. Setiap sel sudah dijalankan dan siap untuk di analisis.

### **Menjalankan Dashboard (Opsional)**
Jika tersedia dashboard interaktif dengan Streamlit:

```bash
streamlit run dashboard.py
```
ataupun melalui link ini :  [Dashboard Saya](https://latihan-visualisasi-data-mkxd3axwwgpeekroy5ezbu.streamlit.app/)

## **Menggunakan `requirements.txt`**
File `requirements.txt` berisi daftar pustaka Python yang diperlukan untuk menjalankan proyek ini. Untuk memastikan semua dependensi terinstal dengan benar, jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

Jika ada perubahan pustaka yang digunakan dalam proyek, Anda dapat memperbarui `requirements.txt` dengan perintah:

```bash
pip freeze > requirements.txt
```

## **Hasil Analisis & Kesimpulan**
- **Kategori Produk Terlaris:** Kategori dengan jumlah penjualan tertinggi dalam 6 bulan terakhir adalah *beleza_saude* dengan lebih dari 4.500 produk terjual, diikuti oleh *cama_mesa_banho* dan *utilidades_domesticas*.
- **Pola Harga dan Keuntungan:** Produk dengan harga rata-rata tertinggi berasal dari kategori *pcs*, *portateis_casa_forno_e_cafe*, dan *eletrodomesticos_2*, dengan margin keuntungan yang juga relatif tinggi.
- **Implikasi Bisnis:** Kategori dengan volume penjualan tinggi perlu dipertahankan dengan strategi pemasaran yang agresif, sementara kategori dengan margin keuntungan tinggi bisa menjadi peluang untuk peningkatan profitabilitas.
