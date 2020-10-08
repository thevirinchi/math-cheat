class Data: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

# Function to calculate 
# the inverse interpolation 
def inv_interpolate(d: list, n: int, 
					y: float) -> float: 

	# Initialize final x 
	x = 0

	for i in range(n): 

		# Calculate each term 
		# of the given formula 
		xi = d[i].x 
		for j in range(n): 
			if j != i: 
				xi = (xi * (y - d[j].y) /
					(d[i].y - d[j].y)) 

		# Add term to final result 
		x += xi 
	return x 

# Driver Code 
if __name__ == "__main__": 

	# Sample dataset of 4 points 
	# Here we find the value 
	# of x when y = 
	d = [Data(1, 1), 
		Data(2, 2), 
		Data(5, 5), 
		Data(7, 7)] 

	# Size of dataset 
	n = 4

	# Sample y value 
	y = 3

	print(f"Value of x at y = {y} :", 
		inv_interpolate(d, n, y))