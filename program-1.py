print("     Melanie Dental Clinic")
print("*--------------------------------*")


x=input("Enter Patient's Name:")
print("Reciept For Patient's Name:", x)

h=int(input("Enter patient's Height:"))
print("Patient's Height:",h,"cm")

z=int(input("Enter patient's previous weight:"))
print("Patient's Weight Loss:",z,"kg")

w=int(input("Enter Patient's Weight:"))
print("Patient's Weight:",w,"kg")

d=input("Enter days since the pateient's last visit:")
print("No. of day's since patient's last visit:",d,"days")

print("-----------------------------------")

bmi=(w/(h*h))*10000
bmi=round(bmi,2)
print("BMI:",bmi)

if bmi>=30:
    print("The patient's body is obese.",)
    print("Intermediate Health Score:0")
elif 25<=bmi<=29.9:
    print("The patient's body is overweight.")
    print("Intermediate Health Score:3")
elif 18.5<=bmi<=24.9:
    print("The patient's body is healthy.")
    print("Intermediate Health Score:5")
elif 17<=bmi<=18.4:
    print("The patient's body is underweight.")
    print("Intermediate Health Score:3")
elif 17>bmi:
    print("The patient's body is too thin.")
    print("Intermediate Health Score:0")

wc=w-z
print("Patient's Weight Change:", wc,"kg")





