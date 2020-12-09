import turtle


x = 50
y = 50
turtle.shape('turtle')
for i in range(1,11):
	for m in range(4):
		turtle.forward(100*i)
		turtle.left(90)
	turtle.penup()
	turtle.goto(-x, -y)
	turtle.pendown()
	x += 50
	y += 50