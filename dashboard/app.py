
import streamlit as st
import pandas as pd

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------
# 2. LOAD DATA
# --------------------------------

df = pd.read_csv("data/processed/cleaned_sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# --------------------------------
# 3. DASHBOARD TITLE
# --------------------------------

st.title("🛒 E-Commerce Sales Analytics Dashboard")

st.markdown(
    "### Business Intelligence | Sales Performance Analysis"
)

st.divider()

# --------------------------------
# 4. SIDEBAR FILTERS
# --------------------------------

st.sidebar.title("Dashboard Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["City"].dropna().unique().tolist())
)

selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + sorted(df["Product"].dropna().unique().tolist())
)

# --------------------------------
# 5. FILTER DATA
# --------------------------------

filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]

if selected_product != "All":
    filtered_df = filtered_df[
        filtered_df["Product"] == selected_product
    ]

# --------------------------------
# 6. KEY PERFORMANCE INDICATORS
# --------------------------------

total_revenue = filtered_df["Revenue"].sum()

total_orders = filtered_df["OrderID"].nunique()

total_quantity = filtered_df["Quantity"].sum()

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"₹{total_revenue:,.0f}"
)

col2.metric(
    "Total Orders",
    total_orders
)

col3.metric(
    "Quantity Sold",
    total_quantity
)

col4.metric(
    "Average Order Value",
    f"₹{average_order_value:,.0f}"
)

st.divider()

# --------------------------------
# 7. REVENUE BY PRODUCT
# --------------------------------

st.subheader("📦 Revenue by Product")

product_sales = (
    filtered_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

if not product_sales.empty:
    st.bar_chart(product_sales)
else:
    st.info("No product data available.")

st.divider()

# --------------------------------
# 8. REVENUE BY CITY
# --------------------------------

st.subheader("🏙️ Revenue by City")

city_sales = (
    filtered_df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

if not city_sales.empty:
    st.bar_chart(city_sales)
else:
    st.info("No city data available.")

st.divider()

# --------------------------------
# 9. PRODUCT QUANTITY ANALYSIS
# --------------------------------

st.subheader("📈 Product Quantity Analysis")

quantity_sales = (
    filtered_df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

if not quantity_sales.empty:
    st.bar_chart(quantity_sales)
else:
    st.info("No quantity data available.")

st.divider()

# --------------------------------
# 10. SALES DATA TABLE
# --------------------------------

st.subheader("📋 Detailed Sales Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# --------------------------------
# 11. DOWNLOAD REPORT
# --------------------------------

st.subheader("📥 Download Sales Report")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Sales Data",
    data=csv_data,
    file_name="sales_report.csv",
    mime="text/csv"
)

# --------------------------------
# 12. FOOTER
# --------------------------------

st.divider()

st.caption(
    "E-Commerce Sales Analytics Dashboard | "
    "Built with Python, Pandas and Streamlit"
)
