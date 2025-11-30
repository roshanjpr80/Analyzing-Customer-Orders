# ======================================================
#                CUSTOMER ORDER ANALYTICS SYSTEM
# ======================================================

# -----------------------------
# 1. DATA INPUT
# -----------------------------

# List of customer names
customer_names = [
    "Roshan", "Rupesh", "Karan", "Sytam", "Rahul",
    "Ravi", "Naha", "Sita", "Rubi", "Renu"
]

# Customer order details
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
    ("Roshan", "Shirt", 1700, "Clothing"),
]


# -----------------------------
# 2. ORGANIZING DATA
# -----------------------------

def group_orders_by_customer(order_list):
    """Groups orders by customer name."""
    customer_dict = {}
    for name, product, price, category in order_list:
        customer_dict.setdefault(name, []).append((product, price, category))
    return customer_dict


customer_orders = group_orders_by_customer(customer_order_detail)


# -----------------------------
# 3. PRODUCT & CATEGORY ANALYSIS
# -----------------------------

# Create a map of product → category
product_category_map = {
    product: category for name, product, price, category in customer_order_detail
}

# Unique product categories
unique_categories = set(product_category_map.values())


# -----------------------------
# 4. CUSTOMER SPENDING ANALYSIS
# -----------------------------

def calculate_customer_totals(order_dict):
    """Calculates total amount spent by each customer."""
    return {
        name: sum(price for product, price, category in orders)
        for name, orders in order_dict.items()
    }


customer_total_spent = calculate_customer_totals(customer_orders)


def classify_customer(total):
    """Returns customer classification based on spending."""
    if total > 100:
        return "High-Value"
    elif total >= 50:
        return "Medium-Value"
    return "Low-Value"


customer_classification = {
    name: classify_customer(total)
    for name, total in customer_total_spent.items()
}


# -----------------------------
# 5. BUSINESS INSIGHTS
# -----------------------------

# Category revenue
category_revenue = {}
for name, orders in customer_orders.items():
    for product, price, category in orders:
        category_revenue[category] = category_revenue.get(category, 0) + price

# Unique products sold
unique_products = {product for _, product, _, _ in customer_order_detail}

# Customers who bought electronics
electronics_customers = [
    name for name, orders in customer_orders.items()
    if any(category == "Electronics" for _, _, category in orders)
]

# Top 3 spending customers
top_customers = sorted(
    customer_total_spent.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

# Customers purchasing multiple categories
multi_category_customers = {
    name for name, orders in customer_orders.items()
    if len({category for _, _, category in orders}) > 1
}

# Customers buying Electronics AND Clothing
electronics_and_clothing = {
    name for name, orders in customer_orders.items()
    if {"Electronics", "Clothing"}.issubset(
        {category for _, _, category in orders}
    )
}

# Order prices
order_prices = [
    price for orders in customer_orders.values() for _, price, _ in orders
]

# Most frequently purchased product
def get_product_frequency(product):
    return sum(
        1 for orders in customer_orders.values()
        for prod, _, _ in orders if prod == product
    )

most_frequent_product = max(unique_products, key=get_product_frequency)

# Most popular category among top customers
top_customer_names = {name for name, _ in top_customers}

top_category = max(
    unique_categories,
    key=lambda c: sum(
        1 for name, orders in customer_orders.items()
        if name in top_customer_names
        for _, _, category in orders if category == c
    )
)

# -----------------------------
# 6. DISPLAY REPORTS
# -----------------------------

print("\n================ CUSTOMER SUMMARY ================\n")
for name, total in customer_total_spent.items():
    print(f"Customer: {name:<10}  Total Spent: ${total:<6}  Category: {customer_classification[name]}")

print("\n================ CATEGORY REVENUE ================\n")
for category, revenue in category_revenue.items():
    print(f"{category:<20}: ${revenue}")

print("\n================ TOP CUSTOMERS ================\n")
for name, total in top_customers:
    print(f"{name}: ${total}")

print("\nCustomers Who Bought From Multiple Categories:", multi_category_customers)
print("Customers Who Bought Electronics & Clothing:", electronics_and_clothing)

print("\n================ BUSINESS INSIGHTS ================\n")
print(f"Total Revenue: ${sum(category_revenue.values())}")
print(f"Most Profitable Category: {max(category_revenue, key=category_revenue.get)}")
print(f"Most Frequently Purchased Product: {most_frequent_product}")
print(f"Most Active Customer: {max(customer_total_spent, key=customer_total_spent.get)}")
print(f"Total Unique Products Sold: {len(unique_products)}")
print(f"Most Popular Category Among Top Customers: {top_category}")
print(f"Electronics Customers: {electronics_customers}")
print(f"Average Spending Per Customer: ${sum(customer_total_spent.values()) / len(customer_total_spent):.2f}")
print(f"Highest Single Order Value: ${max(order_prices)}")
print(f"Lowest Single Order Value: ${min(order_prices)}")
print(f"Average Order Value: ${sum(order_prices) / len(order_prices):.2f}")

print("\n================ PROGRAM COMPLETED ================")
