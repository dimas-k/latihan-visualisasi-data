import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data():
    data = pd.read_csv("dashboard/products_dataset.csv")
    return data

data = load_data()

# Dashboard Title
st.title("Dashboard Analisis Data")

# Menampilkan Data
st.write("### Data Produk")
items_per_page = 10 
max_pages = (len(data) // items_per_page) + 1

if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

start_idx = (st.session_state.page_number - 1) * items_per_page
end_idx = start_idx + items_per_page
st.write(f"Halaman {st.session_state.page_number} dari {max_pages}")
st.dataframe(data.iloc[start_idx:end_idx])

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Previous"):
        if st.session_state.page_number > 1:
            st.session_state.page_number -= 1

with col2:
    if st.button("Next"):
        if st.session_state.page_number < max_pages:
            st.session_state.page_number += 1


# Statistik Deskriptif
st.write("### Statistik Deskriptif")
st.write(data.describe())

# Pertanyaan 1: Produk apa yang memiliki berat terbesar ?
st.write("### Produk dengan Berat Terbesar")
if 'product_weight_g' in data.columns and 'product_category_name' in data.columns:
    weight_by_category = data.groupby('product_category_name')['product_weight_g'].max().sort_values(ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=weight_by_category.values, y=weight_by_category.index, ax=ax)
    ax.set_xlabel("Berat Terbesar (g)")
    ax.set_ylabel("Kategori Produk")
    ax.set_title("Rata-rata Berat Produk per Kategori")
    st.pyplot(fig)
else:
    st.write("Kolom 'product_weight_g' atau 'product_category_name' tidak ditemukan dalam dataset.")

# Pertanyaan 2: Produk apa yang memiliki panjang terbesar ?
st.write("### Produk dengan Panjang Terbesar")
if 'product_length_cm' in data.columns:
    top_long_products = data.groupby('product_category_name')['product_length_cm'].max().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_long_products.values, y=top_long_products.index, ax=ax, errorbar=None)
    ax.set_xlabel("Panjang Terbesar (cm)")
    ax.set_ylabel("Kategori Produk")
    st.pyplot(fig)
else:
    st.write("Kolom 'product_length_cm' tidak ditemukan dalam dataset.")



