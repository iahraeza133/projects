from prettytable import PrettyTable

def what_to_drink():
    water = 300  # مقدار اولیه آب (به میلی‌لیتر)
    milk = 200   # مقدار اولیه شیر (به میلی‌لیتر)
    coffee = 100 # مقدار اولیه قهوه (به گرم)
    money = 0.0  # مقدار اولیه پول (به دلار)

    while True:
        # پرسش از کاربر برای انتخاب نوشیدنی
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "espresso":
            price = 1.5
            required_water = 50
            required_milk = 0
            required_coffee = 20
        elif user_input == "latte":
            price = 2.5
            required_water = 200
            required_milk = 150
            required_coffee = 24
        elif user_input == "cappuccino":
            price = 3.0
            required_water = 250
            required_milk = 100
            required_coffee = 24
        else:
            print("Non ho capito")  # ورودی اشتباه
            continue

        # بررسی منابع کافی برای نوشیدنی انتخابی
        if water < required_water or milk < required_milk or coffee < required_coffee:
            print("Sorry, not enough resources.")
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
            continue  # اگر پول کافی نیست، بازگشت به حلقه و شروع دوباره

        # بروزرسانی منابع در صورت موفقیت تراکنش
        water -= required_water
        milk -= required_milk
        coffee -= required_coffee
        money += price  # افزودن پول به ماشین

        # محاسبه و نمایش پول خرد در صورت پرداخت بیش از حد
        if total_money > price:
            change = round(total_money - price, 2)
            print(f"Here is ${change} in change.")

        print(f"Transaction successful! Enjoy your {user_input}.")

        # استفاده از PrettyTable برای نمایش گزارش منابع
        table = PrettyTable()
        table.field_names = ["Resource", "Amount"]
        table.add_row(["Water", f"{water} ml"])
        table.add_row(["Milk", f"{milk} ml"])
        table.add_row(["Coffee", f"{coffee} g"])
        table.add_row(["Money", f"${money}"])

        # چاپ جدول
        print(table)

        # بررسی برای توقف
        if input("Do you want to continue? (yes/no): ").lower() == "no":
            print("Turning off the coffee machine. Goodbye!")
            break
what_to_drink()