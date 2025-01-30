def calculate_total_purchase():
#Sales Tax
    sales_tax_rate = 0.07
#Subtotal
    subtotal= 0.0
#Price of each item
    price1 = float(input("Enter the price of item 1: "))
    price2 = float(input("Enter the price of item 2: "))
    price3 = float(input("Enter the price of item 3: "))
    price4 = float(input("Enter the price of item 4: "))
    price5 = float(input("Enter the price of item 5: "))
#Subtotal Total
    subtotal = price1 + price2 + price3 + price4 + price5
#Sales Tax
    sales_tax = subtotal * sales_tax_rate
#Total
    total = sales_tax + subtotal
#Print stuff
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
calculate_total_purchase()
