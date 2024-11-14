import turtle
import random

class Snake:
    def __init__(self):
        self.segments = []  # List to store the segments of the snake
        self.create_snake()  # Call method to create the snake
        self.head = self.segments[0]  # The head of the snake
        self.head.setheading(0)  # Set initial direction to right

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
        for position in starting_positions:
            new_segment = turtle.Turtle()  # Create a new turtle object for each segment
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()  # Prevent drawing lines between segments
            new_segment.goto(position)  # Set the initial position of the segment
            self.segments.append(new_segment)  # Add the segment to the list of segments

    def move(self):
        # Move the segments of the snake from the last one to the second
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            y_pos = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(x_pos, y_pos)  # Move the current segment to the position of the previous one

        # Move the head of the snake forward
        self.head.forward(20)

    def set_direction(self, direction):
        # Set the direction of the snake's head
        if direction == "up":
            self.head.setheading(90)
        elif direction == "down":
            self.head.setheading(270)
        elif direction == "left":
            self.head.setheading(180)
        elif direction == "right":
            self.head.setheading(0)

class Food:
    def __init__(self):
        self.food = turtle.Turtle()  # Create a turtle object for the food
        self.food.shape("circle")  # Set the shape of the food
        self.food.color("red")  # Set the color of the food
        self.food.penup()  # Prevent drawing lines when moving
        self.refresh()  # Call the refresh method to place food randomly

    def refresh(self):
        # Random position for the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.food.goto(random_x, random_y)  # Move the food to the new random position

# Create game screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Zahra's Snake Game")
 # Disable automatic screen updates

# Create snake and food objects
snake = Snake()
food = Food()

# Set up keyboard controls for snake movement
screen.listen()  # Listen for keyboard events
screen.onkey(lambda: snake.set_direction("up"), "Up")  # Move up
screen.onkey(lambda: snake.set_direction("down"), "Down")  # Move down
screen.onkey(lambda: snake.set_direction("left"), "Left")  # Move left
screen.onkey(lambda: snake.set_direction("right"), "Right")  # Move right

# Main game loop
game_is_on = True
while game_is_on:
    snake.move()  # Move the snake
    screen.update()  # Update the screen manually after the snake moves

# Keep the screen open
turtle.done()
