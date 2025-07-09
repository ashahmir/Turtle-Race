import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=600)
colors_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
y = - 250
for x in range(6):
    turtle_list.append(Turtle())
    turtle_list[x].shape("turtle")
    turtle_list[x].penup()
    turtle_list[x].color(colors_list[x])
    turtle_list[x].goto(x=-330, y=y)
    y += 100

user_bet = screen.textinput(title="Bet Screen", prompt="What color Do you want to place your bet on: ").lower()
run_game = True
winner = 0
while run_game:
    for x in range(6):
        random_speed = random.randint(0,10)
        turtle_list[x].forward(random_speed)
        if turtle_list[x].xcor() >= 330:
            run_game = False
            winner = x

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-140, 0)
 
if user_bet == colors_list[winner]:
    writer.write("Congratulations, You Won!", font=("Arial", 16, "normal"))
else:
    writer.write(f"You lost your bet, {colors_list[winner].title()} turtle won", font=("Arial", 16, "normal"))

screen.exitonclick()
