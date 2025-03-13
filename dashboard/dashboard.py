import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    products = pd.read_csv("dashboard/products_dataset.csv")
    order_items = pd.read_csv("data/order_items_dataset.csv")
    orders = pd.read_csv("data/orders_dataset.csv")
    return products, order_items, orders

products, order_items, orders = load_data()


st.title("📊 Dashboard Analisis Data E-Commerce")

st.write("## 🔍 Data Produk")
items_per_page = 10 
max_pages = (len(products) // items_per_page) + 1

if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

start_idx = (st.session_state.page_number - 1) * items_per_page
end_idx = start_idx + items_per_page
st.write(f"Halaman {st.session_state.page_number} dari {max_pages}")
st.dataframe(products.iloc[start_idx:end_idx])

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.page_number > 1:
            st.session_state.page_number -= 1

with col2:
    if st.button("Next ➡️"):
        if st.session_state.page_number < max_pages:
            st.session_state.page_number += 1


st.write("## 📈 Statistik Deskriptif Produk")
st.write(products.describe())


st.write("## 🎯 Filter Produk Berdasarkan Harga")
if 'price' in order_items.columns:
    order_items = order_items.dropna(subset=['price'])
    price_min, price_max = st.slider("Pilih rentang harga:", 
        float(order_items['price'].min()), 
        float(order_items['price'].max()), 
        (float(order_items['price'].min()), float(order_items['price'].max())))
    filtered_data = order_items[(order_items['price'] >= price_min) & (order_items['price'] <= price_max)]
    st.dataframe(filtered_data.head(10))
else:
    st.write("❌ Kolom 'price' tidak ditemukan dalam dataset order items.")


st.write("## 🏆 Kategori Produk dengan Penjualan Tertinggi (6 Bulan Terakhir)")
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
six_months_ago = orders['order_purchase_timestamp'].max() - pd.DateOffset(months=6)
recent_orders = orders[orders['order_purchase_timestamp'] >= six_months_ago]
recent_order_items = order_items.merge(recent_orders[['order_id']], on='order_id')
recent_sales = recent_order_items.merge(products[['product_id', 'product_category_name']], on='product_id')
category_sales = recent_sales['product_category_name'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, ax=ax, errorbar=None)
ax.set_xlabel("Jumlah Produk Terjual")
ax.set_ylabel("Kategori Produk")
ax.set_title("Kategori Produk Terlaris dalam 6 Bulan Terakhir")
st.pyplot(fig)

st.write("## 💰 Rata-rata Harga & Margin Keuntungan per Kategori (12 Bulan Terakhir)")
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
one_year_ago = orders['order_purchase_timestamp'].max() - pd.DateOffset(months=12)
yearly_orders = orders[orders['order_purchase_timestamp'] >= one_year_ago]
yearly_order_items = order_items.merge(yearly_orders[['order_id']], on='order_id')
yearly_sales = yearly_order_items.merge(products[['product_id', 'product_category_name']], on='product_id', how='left')
yearly_sales['product_category_name'].fillna('Unknown', inplace=True)
yearly_sales['margin'] = yearly_sales['price'] - yearly_sales['freight_value']
avg_metrics_per_category = yearly_sales.groupby('product_category_name')[['price', 'margin']].mean().sort_values(by='price', ascending=False).head(10)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=avg_metrics_per_category['price'], y=avg_metrics_per_category.index, ax=ax, color="blue", label="Harga Rata-rata")
sns.barplot(x=avg_metrics_per_category['margin'], y=avg_metrics_per_category.index, ax=ax, color="red", alpha=0.6, label="Margin Keuntungan")

ax.set_xlabel("Nilai (BRL)")
ax.set_ylabel("Kategori Produk")
ax.set_title("Rata-rata Harga & Margin Keuntungan per Kategori dalam 12 Bulan Terakhir")
ax.legend()

st.pyplot(fig)