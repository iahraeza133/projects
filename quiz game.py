# import random

# def questions():
#     score = 0
#     max_round = 5
#     # تعریف لیست سوالات با پاسخ‌های درست
#     question_list = [
#         {"question": "Is the Earth round?", "answer": "true"},
#         {"question": "Is the sky green?", "answer": "false"},
#         {"question": "Do fish live in water?", "answer": "true"},
#         {"question": "Is 2+2 equal to 5?", "answer": "false"},
#         {"question": "Is fire hot?", "answer": "true"}
#     ]
    
#     for i in range(max_round):
#         # انتخاب یک سوال به شکل تصادفی
#         question_data = random.choice(question_list)
#         question = question_data["question"]
#         correct_answer = question_data["answer"]
        
#         # دریافت پاسخ کاربر
#         user_answer = input(f"{question} (true/false): ").lower()
        
#         # بررسی پاسخ و افزایش امتیاز
#         if user_answer == correct_answer:
#             score += 1
#             print("Correct!")
#         else:
#             print("Wrong answer!")
    
#     # نمایش امتیاز نهایی
#     print(f"Your final score is: {score} out of {max_round}")

# # اجرای تابع
# questions()
import random

class QuizGame:
    def __init__(self):
        # تعریف ویژگی‌ها مانند سوالات، امتیاز و تعداد سوالات
        self.questions = [
            {"question": "Is the Earth round?", "answer": "true"},
            {"question": "Is the sky green?", "answer": "false"},
            {"question": "Do fish live in water?", "answer": "true"},
            {"question": "Is 2+2 equal to 5?", "answer": "false"},
            {"question": "Is fire hot?", "answer": "true"}
        ]
        self.score = 0
        self.max_round = 5

    def ask_question(self):
        # انتخاب و نمایش سوال به صورت تصادفی
        question_data = random.choice(self.questions)
        question = question_data["question"]
        correct_answer = question_data["answer"]
        
        # دریافت پاسخ کاربر
        user_answer = input(f"{question} (true/false): ").lower()
        
        # بررسی پاسخ
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        # بررسی صحت پاسخ و افزایش امتیاز
        if user_answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong answer!")

    def show_score(self):
        # نمایش امتیاز نهایی
        print(f"Your final score is: {self.score} out of {self.max_round}")

    def play(self):
        # اجرای بازی و پرسش سوالات
        for _ in range(self.max_round):
            self.ask_question()
        self.show_score()

# اجرای بازی
quiz_game = QuizGame()
quiz_game.play()
