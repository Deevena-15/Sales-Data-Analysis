# project-1
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


file_df=pd.read_csv("amazon_sales_2025.csv")
print(file_df)
print("|                        MODULE_2                                     |")

print("***********************************************************************")
print("                      FRIST 5 ROWS                                     ")
print("***********************************************************************")
print(file_df.head(5))


print("***********************************************************************")
print("                      LAST 5 ROWS                                      ")
print("***********************************************************************")
print(file_df.tail(5))

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                    NUMBER OF ROWS &COLUMNS                            ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(file_df.info())

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                    STATISTICAL SUMMARY                            ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(file_df.describe())


print("|               MODULE-3               |")
print("........................................")
print("            SALES OVERVIEW              ")
print("........................................")
sales=file_df["Sales"]
print(sales.describe())

print("|              MODULE-4                |")
print("........................................")
print("           PRODUCT ANALYSIS             ")
print("........................................")
product=file_df["Product"]
print(product)
print("Highest selling product:",max(product))
print("Lowest selling product:",min(product))
print("PRODUCT WISE REVENUE:")
#print(file_df[["Quantity"]* file_df["UnitPrice"]])
print("PRODUCT WISE QUANTITY SOLD:")
print(file_df[["Product","Quantity"]])


print("|                    MODULE-5                         |")
print("''''''''''''''''''CATEGORY ANALYSIS''''''''''''''''''''")
cat=file_df.groupby("Category")["Quantity"].sum()
print(cat)


print("|             MODULE-6                |")
print("=======================================")
print("            MONTHLY SALES              ")
print("=======================================")
month=file_df.groupby("Month")
print(month.sum())
print(month.idxmax().head(1))
print(month.idxmin().head(1))
print(month.idxmin().tail(1))



print("|              MODULE-7               |")
print("=======================================")
print("            FILTERING DATA             ")
print("=======================================")
print("SALES GREATER THAN 5000:",sales>5000)
print("ELECTRONICS PRODUCTS:",product=="Electronics")
print("FURNITURE PRODUCTS:",product=="Furniture")
quant=file_df["Quantity"]
print("QUANTITY GREATER>3:",quant>3)


print("|         MODULE-8       |")
print("==========================")
print("         SORTING          ")
print("==========================")
print("Highest sales:",sales.sort_values(ascending=False).head(1))
print("lowest sales:",sales.sort_values().tail(1))
quant=file_df["Quantity"]
print(" Highest Quantity sale:",quant.sort_values().head(1))


print("|           MODULE-9               |")
print("~~~~~~~~~NUMPY STATISTICS~~~~~~~~~~~")
SALE=np.array(sales)
print("Minimum sales",np.min(SALE))
print("Maximum sales",np.max(SALE))
print("Total sales",np.sum(SALE))
print("Avarage sales",np.mean(SALE))
print("standard deviation:",np.std(SALE))


print("|                  MODULE-10                   |")
print("~~~~~~~~~~~~~~~~SALES DASHBOARD~~~~~~~~~~~~~~~~~")

plt.plot(file_df["Month"] , file_df["Sales"])
plt.xlabel('Months')
plt.ylabel('sales')
plt.title("Monthly Sales Line Chart")
plt.show()



plt.bar(file_df["Category"] , file_df["Sales"])
plt.xlabel('category')
plt.ylabel('sales')
plt.title("Product Sales Bar chart")
#plt.legend()
plt.show()
 
#print("3.category Distribution pie Chart")
catdis=file_df["Category"].value_counts()
plt.pie(catdis, labels=catdis.index , autopct='%1.1f%%')
plt.title("3.category Distribution pie Chart")
plt.show()


print("4.Sales Histogram")
plt.hist(file_df["Sales"])
plt.title("4.Sales Histogram ")
plt.show()


#print("5.Quantity vs Sales Scatter Plot")
plt.scatter(file_df["Quantity"] , file_df["Sales"])
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.title("5.Quantity vs Sales Scatter plot")

plt.show()
