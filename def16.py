def h():
    secret=2
    for i in range(3):
        a=int(input("guess the number"))

        if a==secret:
            print("you win")
        else:
            print("wrong")

h()
