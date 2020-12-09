import turtle

turtle.shape('turtle')
n = int(input('n = '))
c = 360 / n
for i in range(n):
	turtle.forward(100)
	turtle.stamp()
	turtle.backward(100)
	turtle.right(c)