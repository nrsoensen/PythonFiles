import time
# This is a comment
print("Hello, World!")
time.sleep(1)
print("Goodbye :)")
answer = input("Who inspires you?")
print(answer, "inspires you!")
i = 0
while i < 5:
    print(i)
    i += 1
for i in range(5):
    print(i)
i = 10
while i > -1:
    print(i)
    i -= 1
for i in range(6,11):
    print(i)
for i in range(5):
    i += 6
    print(i)

i = -1
while True:
    i += 1

    if(i > 20):
        break

    # if i is odd
    if(i % 2 != 0):
        continue

    print(i)
