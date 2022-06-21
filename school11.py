import pandas as pd
num = int(input("Enter number of students = "))
student_info = {}
for i in range(num):
    Roll_no = int(input("Enter roll no = "))
    Name = input("Enter name = ")
    Contact_number = int(input("Enter contact number = "))
    Section = input("Enter section = ")
    student_info[Roll_no] = [Name, Contact_number, Section]
print(student_info)
df = pd.DataFrame(student_info )
print(df)
df.to_csv(r'C:\Users\Neha\Documents\Project 1 Basic school administration tool.csv')
