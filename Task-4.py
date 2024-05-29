# Python Essentials for Business Analytics

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

weekly_sales_2 = weekly_sales.copy()

for i, x in weekly_sales_2.items():
    if i == "Week 2":
        for y in x:
            if y == "Electronics":
                x[y] = 18000

print(weekly_sales)
print(weekly_sales_2)