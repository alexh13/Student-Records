#  Assignment calls for Write a program that the college Admissions office can use to manage the records of students.
#  1. Create an object specification with these seven data fields: name, address, city, state, zip, student id, and gpa.
#  2. In main, declare 3 uninitialized student objects, using either a fixed size array or individual objects --
#     your choice. 
#  3. Write a value-returning function to create and return a single student object. Design console prompts and input
#     statements in the function for the eight data fields. Call the function three times – once to initialize each of
#     main’s student objects. 
#  4. Write a void function to output nicely formatted labels and values for a single student object’s data fields.
#     Call the function three times – once for each student object.
#
#  Program I/O.
#  Input: from the console keyboard, the personal information for each of 3 students, one student at a time.
#  Output: a labeled summary of the personal information as entered for each of 3  students.

class Student:  # Creating class Student
    name = None  # Data field 1
    address = None  # Data field 2
    city = None  # Data field 3
    state = None  # Data field 4
    zip = None  # Data field 5
    id = None  # Data field 6
    gpa = None  # Data field 7
    def studentvalue(self): #  function created for gathering input in the class
        self.name = input("Enter student name ") # Gather input for name
        self.address = input("Enter student address ") #  Gather input for address
        self.city = input("Enter student city ") #  Gather input for city
        self.state = input("Enter student state ") #  Gather input for state
        self.zip = input("Enter student zip ")  #  Gather input for zip
        self.id = input("Enter student id ")  #  Gather input for id
        self.gpa = float(input("Enter student gpa "))  #  Gather input for gpa converted to a float
        return  #  Return function

def outputrecord(studentrecord):  #  function for outputting studentvalue function created
    print("Name =", studentrecord.name)  #  output name
    print("Address =", studentrecord.address)  #  output address
    print("City =", studentrecord.city)  #  output city
    print("State =", studentrecord.state)  #  output state
    print("ZIP =", studentrecord.zip)  #  output ZIP
    print("ID =", studentrecord.id)  #  output ID
    print("GPA =", studentrecord.gpa)  #  output GPA
    # No return for void function! Had to look this up, drove me crazy

a = Student()  # a is now a student object
b = Student()  # b is now a separate student object
c = Student()  # c is now a separate student object

a.studentvalue()  #  gives a to stored data in studentvalue function
b.studentvalue()  #  gives b to stored data in studentvalue function
c.studentvalue()  #  gives c to stored date in studentvalue function

outputrecord(a)  #  calls function to output input data for Student object a
print()  #  Space between output records looks clean
outputrecord(b)  #  calls function to output input data for student object b
print()  #  Space between output records looks clean
outputrecord(c)  #  calls function to output input data for student object c


