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
start_date = st.sidebar.date_input("Tanggal Mulai", orders["order_purchase_timestamp"].min().date())
end_date = st.sidebar.date_input("Tanggal Akhir", orders["order_purchase_timestamp"].max().date())

if start_date > end_date:
    st.sidebar.error("Tanggal mulai tidak boleh lebih besar dari tanggal akhir!")
else:
    orders_filtered = orders[
        (orders["order_purchase_timestamp"].dt.date >= start_date) &
        (orders["order_purchase_timestamp"].dt.date <= end_date)
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
    
    st.write(f"### 🔍 Data Produk (Periode: {start_date} - {end_date})")
    
    if filtered_sales.empty:
        st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")
    else:
        st.dataframe(filtered_sales.head(10))
        
        # Hitung selisih bulan antara tanggal mulai dan akhir
        months_range = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        
        # Visualisasi Kategori Produk Terlaris (6 Bulan)
        st.write("## 🏆 Kategori Produk dengan Penjualan Tertinggi Dalam 6 Bulan Terakhir")
        if months_range <= 6:
            category_sales = filtered_sales["product_category_name"].value_counts().head(10)
            
            if category_sales.empty:
                st.warning("Tidak ada data kategori produk yang tersedia dalam periode ini.")
            else:
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.barplot(x=category_sales.values, y=category_sales.index, ax=ax, errorbar=None)
                ax.set_xlabel("Jumlah Produk Terjual")
                ax.set_ylabel("Kategori Produk")
                ax.set_title("Kategori Produk Terlaris dalam Rentang Waktu yang Dipilih")
                st.pyplot(fig)
        else:
            st.info("Diagram untuk kategori produk dalam 6 bulan tidak ditampilkan karena rentang waktu lebih dari 6 bulan.")
        
        # Visualisasi Rata-rata Harga & Margin Keuntungan (12 Bulan)
        st.write("## 💰 Rata-rata Harga & margin keuntungan untuk setiap kategori produk dalam 12 bulan terakhir")
        if months_range <= 12:
            filtered_sales["margin"] = filtered_sales["price"] - filtered_sales["freight_value"]
            avg_metrics_per_category = filtered_sales.groupby('product_category_name')[['price', 'margin']].mean().sort_values(by='price', ascending=False).head(10)
            
            if avg_metrics_per_category.empty:
                st.warning("Tidak ada data harga dan margin keuntungan untuk kategori produk yang dipilih.")
            else:
                fig, ax = plt.subplots(figsize=(12, 6))
                sns.barplot(x=avg_metrics_per_category['price'], y=avg_metrics_per_category.index, ax=ax, color="blue", label="Harga Rata-rata")
                sns.barplot(x=avg_metrics_per_category['margin'], y=avg_metrics_per_category.index, ax=ax, color="red", alpha=0.6, label="Margin Keuntungan")
                ax.set_xlabel("Nilai (BRL)")
                ax.set_ylabel("Kategori Produk")
                ax.set_title("Rata-rata Harga & Margin Keuntungan per Kategori (Berdasarkan Rentang Waktu)")
                ax.legend()
                st.pyplot(fig)
        else:
            st.info("Diagram untuk rata-rata harga & margin keuntungan tidak ditampilkan karena rentang waktu lebih dari 12 bulan.")
