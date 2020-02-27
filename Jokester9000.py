import time
import random

JokeList = list([1, 2])

while True:
    Joke = random.choice(JokeList)
    input("Tell me a joke!\n")
    time.sleep(2)
    print("Hahahahahaha, that's so funny\n")
    time.sleep(1)
    print("Ok ok now let me tell you my joke\n")
    time.sleep(1)

    if Joke == 1:
        print("\nknock knock Who’s there Butter Butter who Butter let me in because it’s toasty out here\n")

    elif Joke == 2:
        print("\nknock knock Who’s there Lettuce Lettuce who lettuce in it’s cold out here\n")

    else:
        print("ERROR\n")
