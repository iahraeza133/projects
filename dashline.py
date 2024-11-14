import turtle
import random

# تنظیم پنجره Turtle
screen = turtle.Screen()
screen.bgcolor("white")

# ایجاد شی Turtle
t = turtle.Turtle()
t.speed(0)  # تنظیم سرعت برای سریع‌تر بودن نقاشی
t.hideturtle()  # پنهان کردن نشانگر Turtle

# لیستی از رنگ‌ها برای استفاده در دایره‌ها
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "black"]

# تابع برای رسم دایره با رنگ و اندازه تصادفی
def draw_spot():
    t.penup()  # قلم را بلند کن تا موقعیت عوض نشود
    x = random.randint(-300, 300)  # انتخاب موقعیت تصادفی در محور x
    y = random.randint(-300, 300)  # انتخاب موقعیت تصادفی در محور y
    t.goto(x, y)  # حرکت به موقعیت تصادفی
    t.pendown()  # قلم را پایین بیاور تا دایره رسم شود
    t.color(random.choice(colors))  # انتخاب رنگ تصادفی
    t.begin_fill()  # شروع رنگ آمیزی دایره
    t.circle(random.randint(10, 50))  # رسم دایره با شعاع تصادفی بین 10 تا 50 واحد
    t.end_fill()  # پایان رنگ آمیزی دایره

# رسم چندین دایره
for _ in range(50):  # 50 دایره به صورت تصادفی
    draw_spot()

# پایان برنامه
turtle.done()
