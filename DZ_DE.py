purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    return sum(map(lambda x: x['price'] * x['quantity'], purchases))
def items_by_category(purchases):
    category_dict = {}
    for item in purchases:
        category = item['category']
        if category not in category_dict:
            category_dict[category] = set()
        category_dict[category].add(item['item'])
    return {category: list(items) for category, items in category_dict.items()}


def expensive_purchases(purchases, min_price):
    return [item for item in purchases if item['price'] >= min_price]


def average_price_by_category(purchases):
    category_prices = {}
    category_counts = {}

    for item in purchases:
        category = item['category']
        if category not in category_prices:
            category_prices[category] = 0
            category_counts[category] = 0

        category_prices[category] += item['price'] * item['quantity']
        category_counts[category] += item['quantity']

    return {category: round(category_prices[category] / category_counts[category], 2) for category in category_prices}


def most_frequent_category(purchases):
    category_quantities = {}

    for item in purchases:
        category = item['category']
        category_quantities[category] = category_quantities.get(category, 0) + item['quantity']

    return max(category_quantities, key=category_quantities.get)

print('Общая выручка:',total_revenue(purchases))
print('Товары по категориям:',items_by_category(purchases))
print('Покупки дороже 1.0',expensive_purchases(purchases, 1.0))
print('Средняя цена по категориям:',average_price_by_category(purchases))
print('Категория с наибольшим количеством проданных товаров:',most_frequent_category(purchases))

