w=float(input("please enter your wieght in Kgs"))
h=float(input("please enter your hieght in M"))
bmi=w/h**2
if bmi<=18.5:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are overwieght")
elif bmi<=34.9:
    print("you are obese")
elif bmi<=39.9:
    print("you are sevierly obese")
else :
    print("you are extremly obese")