def calculate_total_sales(sales_data):
    total = 0
    for item in sales_data:
        total += item["price"] * item["quantity"]
    return total


data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]


print("Total Revenue:", calculate_total_sales(data))  

numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)  
