import string
import random
char = list(string.ascii_letters+string.digits+"!@#$%^&*()~?")
def generate():
    length = int(input("Enter a length of your password you would like: "))
    random.shuffle(char)
    password = []
    for i in range(length):
        password.append(random.choice(char))
    random.shuffle(password)
    password = "".join(password)
    print(password)

o = input("do you want to generate password yes or no ")
if o == "Yes":
    generate()
elif o == "No":
    print("program terminated")
    quit()
else:
    print("Inavalid input.Please make sure your input")

