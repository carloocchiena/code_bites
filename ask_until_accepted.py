while True:
    try:
        num = int(input("Please enter a positive number: "))
    except ValueError:
        print("Sorry, it doesn't seem to be a number.")
        continue

    if num < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        #num was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break
if age >= 100: 
    print("Wow big number")
else:
    print("Ok thank you!")
