name = input("Enter your name")

m1 = int(input("Enter python marks:"))
m2 = int(input("Enter SQL marks:"))
m3 = int(input("Enter Excwlmarks:")) 

total = m1+m2+m3
percentage = total/3* 100

print(f"student Name:{name}\n Total marks:{total}\n percentage:{percentage}")

print ("welcome to Grande System.")

if percentage >=90 and percentage <= 100:
    print("Grade A+")
elif percentage >=80 and percentage <= 90:
    print("Grade A")
elif percentage >=70 and percentage <= 80:
    print("Grade B+")
elif percentage >=60 and percentage <= 70:
    print("Grade B")
else:
    print("Grade F") 
    
print(f"student Name:{name}\n Total marks:{total}\n percentage:{percentage}") 

    
    