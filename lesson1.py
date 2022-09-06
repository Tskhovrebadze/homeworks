from turtle import *



# build wall
speed(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

# go face to face

forward(80)

# build door
color("blue")
begin_fill()
left(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
end_fill()

# go to build window
left(90)
forward(70)
left(90)
forward(120)

# build right window
color("yellow")
begin_fill()
left(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()

# go to build roof
left(90)
forward(30)


# build roof
color("red")
begin_fill()
left(45)
forward(150)
left(95)
forward(150)
# left(80)
# forward(120)
end_fill()

# go to build second left window

goto(0, 200)
left(40)
forward(30)

# build left window
color("yellow")
begin_fill()
left(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()


# build left window
# forward(30)
# right(90)



exitonclick()


# exitonclick()

