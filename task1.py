dict1={"Alice":85,"Robert":90,"Sam":66,"Tom":95}
name=input("Enter a student's name:")

if name in dict1:
    b = dict1[name]
    print(name,"Marks:",b)
else:
    print("Student not found")
