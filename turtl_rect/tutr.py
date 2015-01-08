import turtle

turtle.shape('turtle')

turtle.color(float(65/255),float(105/255),float(225/255))

box_len = 200
one_box_len = 20

num = int(box_len/one_box_len)

for _ in range(num):
	turtle.forward(box_len)
	turtle.backward(box_len)
	turtle.left(90)
	turtle.forward(one_box_len)
	turtle.right(90)

turtle.forward(box_len)
turtle.right(90)

for _ in range(num):
	turtle.forward(box_len)
	turtle.backward(box_len)
	turtle.right(90)
	turtle.forward(one_box_len)
	turtle.left(90)


turtle.exitonclick()