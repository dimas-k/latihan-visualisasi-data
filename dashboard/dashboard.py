import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    products = pd.read_csv("dashboard/products_dataset.csv")
    order_items = pd.read_csv("data/order_items_dataset.csv")
    orders = pd.read_csv("data/orders_dataset.csv")
    return products, order_items, orders

products, order_items, orders = load_data()
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

st.sidebar.header("📌 Filter Data")
end_date = st.sidebar.date_input("Tanggal Akhir", orders["order_purchase_timestamp"].max().date())
end_date = pd.Timestamp(end_date) 

# Pilihan rentang waktu
time_range = st.sidebar.selectbox("Pilih Periode", ["6 Bulan Terakhir", "12 Bulan Terakhir", "Manual"])
if time_range == "6 Bulan Terakhir":
    start_date = end_date - pd.DateOffset(months=6)
elif time_range == "12 Bulan Terakhir":
    start_date = end_date - pd.DateOffset(months=12)
else:
    start_date = pd.Timestamp(st.sidebar.date_input("Tanggal Mulai", orders["order_purchase_timestamp"].min().date()))


orders_filtered = orders[
    (orders["order_purchase_timestamp"] >= start_date) &
    (orders["order_purchase_timestamp"] <= end_date)
]

product_categories = products["product_category_name"].dropna().unique()
selected_category = st.sidebar.multiselect("Pilih Kategori Produk", product_categories)

if not selected_category:
    selected_category = product_categories.tolist()

filtered_order_items = order_items.merge(orders_filtered[['order_id']], on='order_id', how='inner')
filtered_sales = filtered_order_items.merge(products[['product_id', 'product_category_name']], on='product_id', how='left')
filtered_sales = filtered_sales[filtered_sales["product_category_name"].isin(selected_category)]

# Dashboard Utama
st.title("📊 Dashboard Analisis Data E-Commerce")
st.write(f"### 🔍 Data Produk (Periode: {start_date.date()} - {end_date.date()})")

if filtered_sales.empty:
    st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")
else:
    st.dataframe(filtered_sales.head(10))

    # Visualisasi Kategori Produk Terlaris (6 Bulan Terakhir)
    st.write("## 🏆 Kategori Produk dengan Penjualan Tertinggi Dalam 6 Bulan Terakhir")
    six_months_ago = end_date - pd.DateOffset(months=6)
    filtered_sales_6m = filtered_sales[filtered_sales["order_id"].isin(
        orders[orders["order_purchase_timestamp"] >= six_months_ago]["order_id"]
    )]
    category_sales = filtered_sales_6m["product_category_name"].value_counts().head(10)

    if category_sales.empty:
        st.warning("Tidak ada data kategori produk yang tersedia dalam periode ini.")
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=category_sales.values, y=category_sales.index, ax=ax, errorbar=None)
        ax.set_xlabel("Jumlah Produk Terjual")
        ax.set_ylabel("Kategori Produk")
        ax.set_title("Kategori Produk Terlaris dalam 6 Bulan Terakhir")
        st.pyplot(fig)

    # Visualisasi Rata-rata Harga & Margin Keuntungan (12 Bulan Terakhir)
    st.write("## 💰 Rata-rata Harga & Margin Keuntungan untuk Setiap Kategori Produk dalam 12 Bulan Terakhir")
    twelve_months_ago = end_date - pd.DateOffset(months=12)
    filtered_sales_12m = filtered_sales[filtered_sales["order_id"].isin(
        orders[orders["order_purchase_timestamp"] >= twelve_months_ago]["order_id"]
    )]
    
    if "price" in filtered_sales_12m.columns and "freight_value" in filtered_sales_12m.columns:
        filtered_sales_12m["margin"] = filtered_sales_12m["price"] - filtered_sales_12m["freight_value"]
        avg_metrics_per_category = filtered_sales_12m.groupby('product_category_name')[['price', 'margin']].mean().sort_values(by='price', ascending=False).head(10)

        if avg_metrics_per_category.empty:
            st.warning("Tidak ada data harga dan margin keuntungan untuk kategori produk yang dipilih.")
        else:
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.barplot(x=avg_metrics_per_category['price'], y=avg_metrics_per_category.index, ax=ax, color="blue", label="Harga Rata-rata")
            sns.barplot(x=avg_metrics_per_category['margin'], y=avg_metrics_per_category.index, ax=ax, color="red", alpha=0.6, label="Margin Keuntungan")
            ax.set_xlabel("Nilai (BRL)")
            ax.set_ylabel("Kategori Produk")
            ax.set_title("Rata-rata Harga & Margin Keuntungan per Kategori (12 Bulan Terakhir)")
            ax.legend()
            st.pyplot(fig)
    else:
        st.warning("Kolom harga atau freight_value tidak ditemukan dalam data.")
