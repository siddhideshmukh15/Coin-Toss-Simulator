import random
print("==== Coin Toss Simulator ====")

while True:
    input("press Enter to toss the coin....")

    result=random.choice(["Heads","Tails"])
    print("Result:",result)

    again=input("Toss again?(y/n):").lower()

    if again !="y":
        print("Thank for playing!")
        break