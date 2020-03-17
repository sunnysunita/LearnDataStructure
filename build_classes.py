class Student:
    pass

s1= Student()
s2= Student()
s3= Student()

s1.name="sunny_kumar"
s2.rollnumber=123
s3.name="arun_kumar"
s2.name="deepak_kumar"
s1.rollnumber=789

print("name: ",getattr(s3,"name","No Name"))
print("rollnumber: ",getattr(s3,"rollnumber","XXX"))
delattr(s2,"rollnumber")
print(s2.__dict__)