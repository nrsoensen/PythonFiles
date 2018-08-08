def electric():
    for i in range(5):
        print("electric")

electric()
print("boogaloo")
electric()


def something():
    for i in range(11):
        for j in range(i):
            print("*", end="")
        print()

something()
