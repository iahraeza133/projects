def what_to_drink():
    water = 300  # مقدار اولیه آب (به میلی‌لیتر)
    milk = 200   # مقدار اولیه شیر (به میلی‌لیتر)
    coffee = 100 # مقدار اولیه قهوه (به گرم)
    money = 0.0  # مقدار اولیه پول (به دلار)
    
    while True:
        # پرسش از کاربر برای انتخاب نوشیدنی
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if user_input == "espresso":
            if water >= 50 and coffee >= 20:
                price = 1.5
                print("Here is your espresso. Enjoy!")
                water -= 50
                coffee -= 20
            else:
                print("Sorry, not enough resources.")
                continue
        
        elif user_input == "latte":
            if water >= 200 and milk >= 150 and coffee >= 24:
                price = 2.5
                print("Here is your latte. Enjoy!")
                water -= 200
                milk -= 150
                coffee -= 24
            else:
                print("Sorry, not enough resources.")
                continue
        
        elif user_input == "cappuccino":
            if water >= 250 and milk >= 100 and coffee >= 24:
                price = 3.0
                print("Here is your cappuccino. Enjoy!")
                water -= 250
                milk -= 100
                coffee -= 24
            else:
                print("Sorry, not enough resources.")
                continue
        
        elif user_input == "report":
            # چاپ گزارش منابع
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")
            continue
        
        elif user_input == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        
        else:
            # پیغام خطا برای ورودی اشتباه
            print("Non ho capito")  # "متوجه نشدم"
            continue

        # پردازش سکه‌ها
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))  # مقدار کوارترها
        dimes = int(input("How many dimes? "))      # مقدار دایم‌ها
        nickels = int(input("How many nickels? "))  # مقدار نیکل‌ها
        pennies = int(input("How many pennies? "))  # مقدار پنی‌ها

        total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        print(f"Total money inserted: ${total_money}")

        # بررسی موفقیت تراکنش
        if total_money < price:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            money += price  # افزودن پول به ماشین
            if total_money > price:
                change = round(total_money - price, 2)
                print(f"Here is ${change} in change.")
            print(f"Transaction successful! Enjoy your drink.")
what_to_drink()