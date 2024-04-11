# Noah Hulett
# Cargill Period 2
# simulates turtle race

# imports
import turtle
import random
import time

# makes the race turtles
def make_turtle(color, x, y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.setpos(x, y)
    t.down()
    return t

# sets up window and the racetrack for the turtles
def set_up():
    wn = turtle.Screen()
    wn.setup(900, 525)
    wn.bgcolor("forestgreen")
    wn.title("Turtle Race")
    turtle.delay(0)
    turtle.speed(0)
    turtle.hideturtle()
    # actives the func to draw the track
    racetrack()

# draws the track and title
def racetrack():
    turtle.penup()
    turtle.setpos(-180, 200)
    turtle.color("white")
    turtle.write("Turtle Race", font=("Courier", 40, "bold"))
    # Draws the big old rectangle
    turtle.setpos(-350, 175)
    turtle.color("crimson")
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(650)
        turtle.rt(90)
        turtle.fd(350)
        turtle.rt(90)
    turtle.end_fill()
    turtle.color("white")
    # draws the lines and numbers
    turtle.penup()
    turtle.goto(-325, 160)
    for i in range(1, 31):
        turtle.write(str(i), font=('Courier', 6, 'bold'))
        turtle.fd(2)
        turtle.setheading(270)
        turtle.fd(10)
        turtle.pendown()
        turtle.fd(300)
        turtle.penup()
        turtle.sety(160)
        turtle.setheading(0)
        turtle.fd(17)
    # draws the finish line
    turtle.setheading(270)
    turtle.penup()
    turtle.setpos(250, 140)
    turtle.shape("square")
    turtle.pensize(5)
    color = ("black", "white")
    for i in range(30):
        turtle.color(color[i % 2])
        turtle.stamp()
        turtle.fd(20)
        # repositions the turtle after the first line
        if i == 14:
            for i in range(2):
                turtle.left(90)
                turtle.fd(20)


def race():
    # turtle data
    tcolor = ("purple", "royalblue", "darkorange", "darkred")
    tycor = (105, 35, -35, -105)
    finished = [False, False, False, False]
    placard = ("First!", "Second!", "Third!", "Fourth!")
    # makes the race turtles
    don = make_turtle(tcolor[0], -330, tycor[0])
    leo = make_turtle(tcolor[1], -330, tycor[1])
    mich = make_turtle(tcolor[2], -330, tycor[2])
    raph = make_turtle(tcolor[3], -330, tycor[3])
    turtles = (don, leo, mich, raph)
    # variables for the race
    place = 0
    finish_line = 255
    delay = .01
    # actives the race
    while (place < 4):
        for i in range(4):
            # moves the turtle
            if not finished[i]:
                turtles[i].fd(random.randint(0, 20))
            # updates the plac
            if turtles[i].xcor() >= finish_line and not finished[i]:
                place += 1
                # prints place and makes it big if first
                if place == 1:
                    turtles[i].turtlesize(4, 4, 4)
                finished[i] = True
                turtle.penup()
                turtle.color(tcolor[i])
                turtle.setpos(340, tycor[i]-10)
                turtle.write(placard[place - 1], font=('Courier', 15, 'bold'))
            time.sleep(delay)



def main():
    set_up()
    race()
    turtle.done()


if __name__ == "__main__":
    main()