name = input("Please type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, and it has come to an end. You can either go left or right. Which way do you dare to travel?: ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim ")

    if answer == "swim":
        print("You swam across and got eaten by an alligator")

    if answer == "walk":
        print("You walked for many miles, ran out of water and you died.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly and insecure. Do you want to cross it or go back? (cross/back) ")

    if answer == "back":
        print("You go back and die like a coward.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no)")

        if answer == "Yes":
            print("You talked to the stranger and you have been given gold. You win!")

        elif answer == "No":
            print("Since you are terminally online, you refuse to talk the stranger. The Stranger, being someone who loves to talk to strangers, is greatly offended and he straight up kills you.")

else:
    print("Not a valid option, you have died!")

print("Thank you for trying,", name)