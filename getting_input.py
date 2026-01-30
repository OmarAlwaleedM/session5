prompt = "what is your name? "
name = input(prompt)
# id name == "Bob":
#      print ("FU Bob")
# else:
#   print("nice to meet you,", name)

prompt2 = "how old are you," + name + "? "
age = input(prompt2)
# convert to int
age = int(age)
print("you were born in,", 2025 - age)
