import matplotlib.pyplot as plt

if __name__ == '__main__':
	points = open("./points.txt") # open your input points
	n = int(points.readline())

	input_x = []
	input_y = []

	for i in range(n):
		inp = points.readline().split(" ")
		input_x.append(int(inp[0]))
		input_y.append(int(inp[1]))

	result_x = []
	result_y = []

	result = open("./result.txt") # open your result file generated by the application
	n = int(result.readline())

	result_x = []
	result_y = []

	for i in range(n):
		inp = result.readline().split(" ")
		result_x.append(int(inp[0]))
		result_y.append(int(inp[1]))

	# add the first point again to draw the line from last point to first point
	result_x.append(result_x[0])
	result_y.append(result_y[0])

	fig, ax = plt.subplots()
	ax.scatter(input_x, input_y, c='blue')

	for x, y in zip(input_x, input_y):
		plt.text(x+0.1, y, '({}, {})'.format(x, y))

	ax.plot(result_x, result_y, c='red')
	ax.grid()
	plt.show()