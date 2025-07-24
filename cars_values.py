import pandas as pd
import matplotlib.pyplot as plt
# Create some sample data
data = {
    'years': [2018, 2019, 2020, 2021, 2022],
    'prices': [450000, 470000, 500000, 520000, 550000]
}
df = pd.DataFrame(data)

# ✅ Save to Excel file (file name should be in quotes)
df.to_excel("cars_price.xlsx", index=False)
print("Excel file 'cars_price.xlsx' is created.")

# ✅ Read back from the Excel file
df = pd.read_excel("cars_price.xlsx")

# ✅ Print the data

print("years\t\tprices")
print("-"*30)
for _, row in df.iterrows():
    print(f"{row['years']}\t\t{row['prices']}")

# ✅ Extract values from DataFrame
years = df['years']
prices = df['prices']

# ✅ Plot Bar Chart
#add plot
plt.bar(years, prices, color='blue')
plt.title('Car Prices Over the Years')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid(True)
plt.show()
#this is
plt.plot(years, prices, color='blue')
plt.title('Car Prices Over the Years')
plt.xlabel('Year')
plt.ylabel('Price (INR)')
plt.grid(True)
plt.show()
