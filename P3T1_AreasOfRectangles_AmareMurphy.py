# Finding which rectangle has the greatest area
# 092319
# CTI-110 - Areas of Rectangles
# Amare Murphy

# Dimensions of Rectangle 1
length1 = int(input('enter the length of rectangle 1: '))
width1 = int(input('enter the width of rectangle 1: '))

# Dimensions of Rectangle 2
length2 = int(input('enter the length of rectangle 2: '))
width2 = int(input('enter the width of rectangle 2: '))

# Calculate the areas of the rectangles
area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area
if area1 > area2:
    print('Rectangle 1 has the greater area.' )
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
