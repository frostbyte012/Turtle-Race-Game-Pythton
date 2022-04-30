from turtle import Turtle,Screen
import random
race_is_on=True
y_height=-150
screen=Screen()
winner_bet=screen.textinput(title="the winner name",prompt="What colored turtle would win? ")
colors=["red","green","violet","indigo","blue","yellow","orange"]
turtles=[]
screen.setup(width=600,height=500)
for turtle_creator_index in range(0,7):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_height)
    y_height+=50
    new_turtle.color(colors[turtle_creator_index])
    turtles.append(new_turtle)

while race_is_on:
    for turtLe in turtles:
        turtLe.forward(random.randint(0,10))
        if turtLe.xcor() > 250:
            winner_turtle=turtLe
            race_is_on=False

if winner_turtle.pencolor() == winner_bet.lower():
    print(f"You've Won the bet! The winner is {winner_turtle.pencolor()} !")
else:
    print(f"You've Lost the bet! The winner is {winner_turtle.pencolor()} !")

screen.exitonclick()