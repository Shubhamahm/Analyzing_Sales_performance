import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------# 1. Data Loading and cleaning--------------------------

df= pd.read_csv("C:\\Users\\shubh\\OneDrive\\Desktop\\All projects\\python codes\\retail_sales_data.csv")
#print(df)

df.drop_duplicates(inplace= True) #dropping duplicates rows
df.dropna(inplace=True) #dropping empty rows
#print(df)

df['Date']= pd.to_datetime(df['Date'], format='mixed') #converting date to datetime format
print(df.to_string())

#print(df.head())

# --------------2. Feature Engineering.----------------------------

df['Month']=df['Date'].dt.month #Extract Month from Date
#print(df)

Average_unit_price=df.groupby('Product')['Unit Price'].mean().reset_index()
#print(Average_unit_price)

#  If Cost Price assumed (eg. 70% of Unit Price), calculate profit
df['cost price']= df['Unit Price']*0.7
df['Profit']= (df['Unit Price']-df['cost price']*df['Units Sold'])

#print(df)

# ----------------3. Data Analysis & Aggregation--------------------

# total revenue by region
Total_Revenue_by_Region=df.groupby('Region')['Total Revenue'].sum().sort_values(ascending=False)
#print(Total Revenue_by_Region)

#  Monthly sales trend
Sales_trend=df.groupby('Month') ['Total Revenue'].sum()
#print(Sales_trend)

# Top 5 selling products.
Top_Selling_Products= df.groupby('Product')['Units Sold'].sum().sort_values(ascending=False)
#print(Top Selling_Products)

#Product with the highest unit price fluctuations.
price_std= df.groupby('Product') ['Unit Price'].std().sort_values(ascending=False)
print(price_std)

# -----------------4. Visualization-----------------------

#Sales trend over time (line plot)
monthly_revenue=df.groupby ("Month") ['Total Revenue'].sum()

plt.figure(figsize=(10,6))
sns.lineplot(x=monthly_revenue.index,y=monthly_revenue.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
#plt.show()

# Total revenue per region (bar chart).

plt.figure(figsize=(10,6))
Total_Revenue_by_Region.plot(kind="bar", color="green")
plt.title("Total revenue per region")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True) 
plt.show()

# Top 5 products by units sold (horizontal bar chart).
plt.figure(figsize=(10,6))
Top_Selling_Products.plot(kind='barh', color="green")
plt.title("Top 5 products by units sold")
plt.xlabel("Units Sold")
plt.ylabel("Product")
plt.grid(True)
plt.show()

#Revenue distribution per store (boxplot).

total_revenue_by_store=df.groupby('Store') ['Total Revenue'].sum()

plt.figure(figsize=(10,6))
total_revenue_by_store.plot(kind="box",color="green")
plt.title("Top 5 products by units sold")
plt.xlabel("store")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.show()

# ----------------------------5. Conclusion & Recommendations--------------------

# Region with highest revenue: North

 #Best-selling product: Toothpaste
 
 #store with highest avg revenue: Store B
 
 # Month with peak sales: June
 