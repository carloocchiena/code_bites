# with input from user

space = 0
star = 1

while True:
    
    try:
        star_goal = int(input("How many stars do you want the tree to be at the base?\nEven numbers will be rounded to the nearest upper odd number.\nYou must enter a number:"))                   
    except ValueError:
        print("Please, enter a number.")
        continue
    if star_goal < 0:
        print("Sorry, no negative numbers allowed.")
    else:
        break

if star_goal % 2 == 0:
    star_goal +=1

space = star_goal // 2            
                
while star <= star_goal:
    print (f"{' '  * space}{'*' * star}")
    space -= 1
    star += 2

# with a function 
    
def py_pine_tree(pine_size=10):
    """Print a star-tree of a given size.
    Input base size, return a tree
    """
    space = 0
    star = 1
    
    if pine_size % 2 == 0:
        pine_size +=1

    space = pine_size // 2            
                
    while star <= pine_size:
        print (f"{' '  * space}{'*' * star}")
        space -= 1
        star += 2
