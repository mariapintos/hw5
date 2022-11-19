
# 2)Create a function named "safe_subtract" that takes two parameters and returns the result of the second value subtracted from the first.
# If the values cannot be subtracted due to its type, it returns None. If there is any other reason why it fails show the problem.

def safe_subtract(x,y):
    try:
        return x-y
    except TypeError:
        return None
        
safe_subtract(10,3)

# 5) Squash some bugs! Find the possible logical errors (bugs) in the code blocks below. Comment in each of them which 
# logical errors did you find and correct them:

### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double_elem = elem * 2
    total_double_sum += double_elem

## Comment: 
# 'total_double_sum' is adding the elements of the list without having doubled them, therefore, we can either add the 'double_elem' to
# the function or we can simply add to 'total_double_sum' elem*2.

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = strings+"_"+string

## Comment: 
# The second element of the equation, previously 'string' is missing an s, since it is referring to the 'strings', and not adding
# the individual 'string' twice.


### (c) Careful!
j=10
while j > 0:
   j -= 1

## Comment:
# If j has an initial value equal to 10, and we go on adding 1 to j, this will always be strictly higher than 0, and will go on until
# infinity. Therefore, we can change  the + to a -, so the loop will finish whenever j is equal to 0. 
# Also, we can put a limit to the loop: 

j=10
while j > 0:
   j += 1
   if j == 25:
    break

### (d)
productory = 1
for elem in [1, 5, 25]:
    productory *= elem

## Comment: 
# Multiplying the elements to productory, which was equal to 0 will always return 0. Therefore, we change it to 1, this way
# 'productory' = 'elem'


# 8) Create a function called "compute_distance" that takes a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance.

coord = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

def dist(list):
    dist_list = []
    for element in list:
        dist1 = element[0][0] - element[1][0]
        dist2 = element[0][1] - element[1][1]
        dist = (dist1**2 + dist2**2)**0.5
        dist_list.append(dist)
    return dist_list

dist(coord)












