import turtle

turtle.shape('turtle')
turtle.speed(12)

for _ in range(100):
	turtle.forward(250)
	turtle.left(120)
	turtle.left(1)

turtle.exitonclick()