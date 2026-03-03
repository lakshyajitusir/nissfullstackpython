class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student("Rahul", 85)
s2 = Student("Anita", 85)

print(s1 == s2)     # Uses __eq__

students = {s1, s2}   # Try to use set