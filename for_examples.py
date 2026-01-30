# 'for' examples
# lets print the numbers 1 to 10

# for i in range(10): # displays numbers from 0 to 10. 0 is default
#    print(i)

# for i in range(-10,10): # this begins from -10 to 10 instead of 0 to 10
#     print(i)

for i in range(-10,10,2): # begin the range from -10 to 10, and skips 2 every time so -10, -8, etc to 10
    print(i)

# print multiplication table
for i in range(1,11):
    for j in range(i,11):
        print(f"{i}x{j}={i*j}")
    print()