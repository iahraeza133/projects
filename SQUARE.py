import turtle

# ایجاد شیء Turtle
t = turtle.Turtle()



# رسم مربع
for _ in range(4):
    t.forward(100)  # حرکت به جلو به اندازه 100 واحد
    t.left(90)  # چرخش به سمت چپ 90 درجه

# پایان دادن به رسم
turtle.done()
