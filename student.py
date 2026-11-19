name = input("Enter your name")

m1 = int(input("Enter python marks:"))
m2 = int(input("Enter SQL marks:"))
m3 = int(input("Enter Excwlmarks:")) 

total = m1+m2+m3
percentage = total/3* 100

print(f"student Name{name}\n Total marks:{total}\n percentage:{percentage}")
