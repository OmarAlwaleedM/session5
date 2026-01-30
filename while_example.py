from random import randint
num = 0
while num < 10:
    print(num)
    num = num +1
    # num += 1

money = 1000000
it = 0
while money > 0:
    spend = randint(1, 10000)
    it = it + 1
    print(f"Iteration {it}: I am spending {spend}")
    money = money - spend


# infinite loop with escape clause
money = 100
it = 0
while True:
    # escape from while
    if money < 0:
        break # get out of the while
    it = it + 1
    spend = randint(-1, 1)
    print(f"Iteration {it}: I am spending {spend}")
    money = money - spend