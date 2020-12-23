color1 = (40, 255, 255, 255)
color2 = (255, 255, 255, 255)

step_tuple = (50, 50, 50, 50)
color1 = tuple(map(lambda i, j: i-j if i - j > 0 else 0, color1, step_tuple)) 
color2 = tuple(map(lambda i, j: i - j, color2, step_tuple)) 
print(color1)
print(color2)
