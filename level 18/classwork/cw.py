


usernumber = int(input("Enter a number: ")) 


if usernumber % 2 == 1:
    print("odd")
else:
    print("even")
  

#2

age = int(input("Enter your age: "))


if age >= 18:
    print("You are enable to vote.")
else:
    print("You are not enable to vote.") 

#3
temperature = float(input("Enter the temperature in degrees Celsius: "))

temperature=26
if temperature<=15:
    print("It's cold.")
elif temperature >15:
    print("It's warm.")
elif temperature>=25:
    print("hits hot")

    #4
password = "python123"


user_password = input("Enter the password: ")


if user_password == password:
    print("Access Granted")
else:
    print("Access Denied")