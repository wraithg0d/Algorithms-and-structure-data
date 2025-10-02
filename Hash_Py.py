def show_hash_table():
    prices = {}
    
    prices["apple"] = 50
    prices["banana"] = 30  
    prices["orange"] = 25
    
    print("Список цен:")
    for fruit, price in prices.items():
        print(f"{fruit}: {price}")
    
    print(f"\nЯблоко стоит: {prices['apple']}")
    
    if "banana" in prices:
        print("Бананы в наличии!")
    
    del prices["orange"]
    print(f"\nБез апельсинов: {prices}")

show_hash_table()
