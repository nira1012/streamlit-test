import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Mini Sales Dashboard")

url = "https://raw.githubusercontent.com/nira1012/streamlit-test/main/sales.csv"
df = pd.read_csv(url)


# Show first few rows
st.write("### Sample Data", df.head())

# Select Region
region = st.selectbox("Select Region:", df['region'].unique())

# Filter data by region
filtered_df = df[df['region'] == region]

# Slider for filtering sales
max_sales = int(filtered_df['sales'].max())
sales_range = st.slider("Select Sales Range:", 0, max_sales, (0, max_sales))
filtered_df = filtered_df[(filtered_df['sales'] >= sales_range[0]) & (filtered_df['sales'] <= sales_range[1])]

st.write(f"### Filtered Data ({region} region)")
st.write(filtered_df)

# Plot sales by product
fig, ax = plt.subplots()
ax.bar(filtered_df['product'], filtered_df['sales'], color='skyblue')
ax.set_xlabel("Product")
ax.set_ylabel("Sales")
ax.set_title(f"Sales by Product in {region}")
plt.xticks(rotation=45)
st.pyplot(fig)


