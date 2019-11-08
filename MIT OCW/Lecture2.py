position = input("****************\n : ) \n****************\nYou are in the lost forest; Left or Right?")
counter = 0

while position == "right":
    position = input("****************\n : ) \n****************\nYou are in the lost forest; Left or Right?")
    counter = counter + 1
    if position == "left":
        print("You escaped the lost forest!")
        break
    elif counter > 4:
        print("You are forever stuck in the lost forest")
        break