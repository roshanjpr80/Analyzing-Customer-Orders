# ----------------------------------------
# 1. Store Customer Data
# ----------------------------------------

# List of customer names
customer_names = [
    "Roshan", "Rupesh", "Karan", "Sytam", "Rahul",
    "Ravi", "Naha", "Sita", "Rubi", "Renu"
]

# Order details: (customer, product, price, category)
customer_order_detail = [
    ("Roshan", "Smartphone", 700, "Electronics"),
    ("Rupesh", "Jacket", 120, "Clothing"),
    ("Karan", "T-shirt", 25, "Clothing"),
    ("Sytam", "Jeans", 45, "Clothing"),
    ("Rahul", "Laptop", 1200, "Electronics"),
    ("Ravi", "Blender", 80, "Home Essentials"),
    ("Naha", "Microwave", 150, "Home Essentials"),
    ("Sita", "Headphones", 90, "Electronics"),
    ("Rubi", "Shirt", 40, "Clothing"),
    ("Renu", "Vacuum Cleaner", 180, "Home Essentials"),
    ("Roshan", "Shirt", 1700, "Clothing")
]

print("----- Customer Order Details -----")
for order in customer_order_detail:
    print(order)

# Organize orders in dictionary
customer_order_dict = {}
for name, product, price, category in customer_order_detail:
    customer_order_dict.setdefault(name, []).append((product, price, category))

print("\n----- Customer Orders (Grouped) -----")
for name, orders in customer_order_dict.items():
    print(f"{name}: {orders}")

# ----------------------------------------
# 2. Classify Products by Category
# ----------------------------------------

product_category_dict = {
    product: category
    for name, product, price, category in customer_order_detail
}

unique_categories = set(product_category_dict.values())

print("\nAvailable Product Categories:", unique_categories)

# ----------------------------------------
# 3. Customer Spending Analysis
# ----------------------------------------

customer_total_spent = {
    name: sum(price for product, price, category in orders)
    for name, orders in customer_order_dict.items()
}

customer_classification = {}
for name, total in customer_total_spent.items():
    if total > 100:
        customer_classification[name] = "High-Value"
    elif 50 <= total <= 100:
        customer_classification[name] = "Medium-Value"
    else:
        customer_classification[name] = "Low-Value"

# ----------------------------------------
# 4. Business Insights
# ----------------------------------------

# Revenue by category
category_revenue = {}
for name, orders in customer_order_dict.items():
    for product, price, category in orders:
        category_revenue[category] = category_revenue.get(category, 0) + price

# Unique products
unique_products = {product for name, product, price, category in customer_order_detail}

# Electronics buyers
electronics_customers = [
    name for name, orders in customer_order_dict.items()
    if any(category == "Electronics" for product, price, category in orders)
]

# Top 3 spenders
top_customers = sorted(
    customer_total_spent.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

# Customers buying from multiple categories
multi_category_customers = {
    name for name, orders in customer_order_dict.items()
    if len({category for product, price, category in orders}) > 1
}

# Customers buying Electronics & Clothing
electronics_and_clothing = {
    name for name, orders in customer_order_dict.items()
    if {"Electronics", "Clothing"}.issubset(
        {category for product, price, category in orders}
    )
}

# ----------------------------------------
# 5. Display Results
# ----------------------------------------

print("\nCustomer Spending and Classification:")
for name, total in customer_total_spent.items():
    print(f"{name}: ${total} ({customer_classification[name]})")

print("\nRevenue by Category:")
for category, revenue in category_revenue.items():
    print(f"{category}: ${revenue}")

print("\nTop 3 Highest-Spending Customers:")
for name, total in top_customers:
    print(f"{name}: ${total}")

print("\nCustomers with Multiple Categories:", multi_category_customers)
print("Bought Electronics & Clothing:", electronics_and_clothing)

# ----------------------------------------
# Business Insights Summary
# ----------------------------------------

print("\n----- Business Insights Summary -----\n")

print(f"Total Revenue: ${sum(category_revenue.values())}")
print(f"Most Profitable Category: {max(category_revenue, key=category_revenue.get)}")

# Most frequently purchased product
most_frequent_product = max(
    unique_products,
    key=lambda p: sum(1 for name, orders in customer_order_dict.items()
                      for prod, price, cat in orders if prod == p)
)
print(f"Most Frequently Purchased Product: {most_frequent_product}")

print(f"Most Active Customer: {max(customer_total_spent, key=customer_total_spent.get)}")
print(f"Unique Products Sold: {len(unique_products)}")

# Popular category among top customers
top_customer_names = {name for name, total in top_customers}
top_customer_fav_category = max(
    unique_categories,
    key=lambda c: sum(1 for name, orders in customer_order_dict.items()
                      if name in top_customer_names
                      for product, price, cat in orders if cat == c)
)

print(f"Most Popular Category Among Top Customers: {top_customer_fav_category}")
print(f"Customers Who Purchased Electronics: {electronics_customers}")

print(f"Average Spending per Customer: ${sum(customer_total_spent.values()) / len(customer_total_spent):.2f}")
print(f"Total Unique Customers: {len(customer_total_spent)}")
print(f"Total Orders: {len(customer_order_detail)}")

print(f"High-Value Customers: {sum(v == 'High-Value' for v in customer_classification.values())}")
print(f"Medium-Value Customers: {sum(v == 'Medium-Value' for v in customer_classification.values())}")
print(f"Low-Value Customers: {sum(v == 'Low-Value' for v in customer_classification.values())}")

# Order values
all_prices = [price for name, orders in customer_order_dict.items() for product, price, category in orders]

print(f"Highest Order Value: ${max(all_prices)}")
print(f"Lowest Order Value: ${min(all_prices)}")
print(f"Average Order Value: ${sum(all_prices) / len(all_prices):.2f}")

print("\n----- End of Business Insights -----")
