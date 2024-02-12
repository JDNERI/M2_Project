#1. LONGITUD DE UNA FRASE.

word = input("Enter a word: ")

# Check if the length of the word is greater than 8
if len(word) > 8:
    print(f"Letters to spare. It has {len(word)} letters.")
# Check if the length of the word is less than 4
elif len(word) < 4:
    print(f"Letters are missing. It only has {len(word)} letters.")
# If the length of the word is between 4 and 8, it is considered correct
else:
    print(f"The word is correct, it falls within the range.")



#2. ENCUENTRA EL CUADRANTE.

axis_x = int(input("Enter the x-axis: "))
axis_y = int(input("Enter the y-axis: "))

# Check if the point is in the first quadrant
if axis_x > 0 and axis_y > 0:
    print("The point is in the quadrant I.")
# Check if the point is in the second quadrant
elif axis_x < 0 and axis_y > 0:
    print("The point is in the quadrant II.")
# Check if the point is in the third quadrant
elif axis_x < 0 and axis_y < 0:
    print("The point is in the quadrant III.")
# Check if the point is in the fourth quadrant
elif axis_x > 0 and axis_y < 0:
    print("The point is in the quadrant IV.")
# If the point is on the x-axis
elif axis_x != 0 and axis_y == 0:
    print("The point is on the x-axis.")
# If the point is on the y-axis
elif axis_x == 0 and axis_y != 0:
    print("The point is on the y-axis.")
# If the point is at the origin
elif axis_x == 0 and axis_y == 0:
    print("The point is at the origin.")
# If the point is not in any quadrant
else:
    print("The point is not in any quadrant.")