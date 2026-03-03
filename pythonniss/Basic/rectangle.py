"""wap take rectangle length and breadth form keyboard
display length breadth area and perimeter"""
print("enter rectangle length")
L=int(input())
print("enter rectangle breadth")
B=int(input())
ar=L*B
pr=2*(L+B)
print("length=",L)
print("breadth=",B)
print("area=",ar)
print("perimetr=",pr)

"""
o/p:
enter rectangle length 
3
enter rectangle breadth
4
length=3
breadth=4
area=12
perimeter=24
"""






🔷 PROGRAM 1: Area of Rectangle
Question:

Write a Python program to calculate the area of a rectangle.

Program:
print("enter rectangle length")
L=int(input())
print("enter rectangle breadth")
B=int(input())
ar=L*B
print("area=",ar)
Sample Output:
enter rectangle length
3
enter rectangle breadth
4
area= 12
🔷 PROGRAM 2: Perimeter of Rectangle
Question:

Write a Python program to calculate the perimeter of a rectangle.

Program:
print("enter length")
L=int(input())
print("enter breadth")
B=int(input())
pr=2*(L+B)
print("perimeter=",pr)
Sample Output:
enter length
3
enter breadth
4
perimeter= 14
🔷 PROGRAM 3: Area of Circle
Question:

Write a Python program to calculate the area of a circle.

Program:
print("enter radius")
r=float(input())
area=3.14*r*r
print("area=",area)
Sample Output:
enter radius
5
area= 78.5
🔷 PROGRAM 4: Circumference of Circle
Question:

Write a Python program to calculate circumference of a circle.

Program:
print("enter radius")
r=float(input())
c=2*3.14*r
print("circumference=",c)
Sample Output:
enter radius
5
circumference= 31.400000000000002
🔷 PROGRAM 5: Area of Triangle
Question:

Write a Python program to calculate area of a triangle.

Program:
print("enter base")
b=float(input())
print("enter height")
h=float(input())
area=0.5*b*h
print("area=",area)
Sample Output:
enter base
10
enter height
5
area= 25.0
🔷 PROGRAM 6: Volume of Cube
Question:

Write a Python program to calculate volume of a cube.

Program:
print("enter side")
s=float(input())
v=s*s*s
print("volume=",v)
Sample Output:
enter side
3
volume= 27.0
🔷 PROGRAM 7: Surface Area of Sphere
Question:

Write a Python program to calculate surface area of a sphere.

Program:
print("enter radius")
r=float(input())
area=4*3.14*r*r
print("surface area=",area)
Sample Output:
enter radius
2
surface area= 50.24
🔷 PROGRAM 8: Square and Cube
Question:

Write a Python program to find square and cube of a number.

Program:
print("enter number")
n=int(input())
sq=n**2
cb=n**3
print("square=",sq)
print("cube=",cb)
Sample Output:
enter number
4
square= 16
cube= 64
🔷 PROGRAM 9: Average of Three Numbers
Question:

Write a Python program to calculate average of three numbers.

Program:
print("enter first number")
a=int(input())
print("enter second number")
b=int(input())
print("enter third number")
c=int(input())
avg=(a+b+c)/3
print("average=",avg)
Sample Output:
enter first number
10
enter second number
20
enter third number
30
average= 20.0
🔷 PROGRAM 10: Power Calculation
Question:

Write a Python program to calculate power of a number.

Program:
print("enter base")
b=int(input())
print("enter exponent")
e=int(input())
res=b**e
print("result=",res)
Sample Output:
enter base
2
enter exponent
3
result= 8


🔷 PROGRAM 11: Quotient and Remainder
Question:

Write a Python program to find quotient and remainder.

Program:
print("enter first number")
a=int(input())
print("enter second number")
b=int(input())
q=a//b
r=a%b
print("quotient=",q)
print("remainder=",r)
Sample Output:
enter first number
10
enter second number
3
quotient= 3
remainder= 1
🔷 PROGRAM 12: Sum of Digits (2-Digit Number)
Question:

Write a Python program to find sum of digits of a 2-digit number.

Program:
print("enter 2 digit number")
n=int(input())
s=(n//10)+(n%10)
print("sum=",s)
Sample Output:
enter 2 digit number
45
sum= 9
🔷 PROGRAM 13: Simple Interest
Question:

Write a Python program to calculate simple interest.

Program:
print("enter principal")
P=float(input())
print("enter rate")
R=float(input())
print("enter time")
T=float(input())
SI=(P*R*T)/100
print("simple interest=",SI)
Sample Output:
enter principal
1000
enter rate
5
enter time
2
simple interest= 100.0
🔷 PROGRAM 14: Compound Interest
Question:

Write a Python program to calculate compound interest.

Program:
print("enter principal")
P=float(input())
print("enter rate")
r=float(input())
print("enter time")
t=float(input())
print("enter number of times compounded")
n=int(input())
CI=P*(1+r/n)**(n*t)-P
print("compound interest=",CI)
Sample Output:
enter principal
1000
enter rate
5
enter time
2
enter number of times compounded
1
compound interest= 102.5
🔷 PROGRAM 15: Square Root
Question:

Write a Python program to find square root of a number.

Program:
print("enter number")
n=float(input())
sqrt=n**0.5
print("square root=",sqrt)
Sample Output:
enter number
25
square root= 5.0
🔷 PROGRAM 16: Celsius to Fahrenheit
Question:

Write a Python program to convert Celsius to Fahrenheit.

Program:
print("enter celsius")
C=float(input())
F=(C*9/5)+32
print("fahrenheit=",F)
Sample Output:
enter celsius
30
fahrenheit= 86.0
🔷 PROGRAM 17: Fahrenheit to Celsius
Question:

Write a Python program to convert Fahrenheit to Celsius.

Program:
print("enter fahrenheit")
F=float(input())
C=(F-32)*5/9
print("celsius=",C)
Sample Output:
enter fahrenheit
86
celsius= 30.0
🔷 PROGRAM 18: Kilometer to Miles
Question:

Write a Python program to convert kilometer to miles.

Program:
print("enter kilometer")
km=float(input())
miles=km*0.621
print("miles=",miles)
Sample Output:
enter kilometer
10
miles= 6.21
🔷 PROGRAM 19: Meter to Centimeter
Question:

Write a Python program to convert meter to centimeter.

Program:
print("enter meter")
m=float(input())
cm=m*100
print("centimeter=",cm)
Sample Output:
enter meter
5
centimeter= 500.0
🔷 PROGRAM 20: Days to Years
Question:

Write a Python program to convert days into years.

Program:
print("enter days")
d=int(input())
years=d/365
print("years=",years)
Sample Output:
enter days
730
years= 2.0



🔷 PROGRAM 21: Hours to Seconds
Question:

Write a Python program to convert hours into seconds.

Program:
print("enter hours")
h=int(input())
sec=h*3600
print("seconds=",sec)
Sample Output:
enter hours
2
seconds= 7200
🔷 PROGRAM 22: Bytes to KB
Question:

Write a Python program to convert bytes into kilobytes.

Program:
print("enter bytes")
b=int(input())
kb=b/1024
print("kb=",kb)
Sample Output:
enter bytes
2048
kb= 2.0
🔷 PROGRAM 23: Rupee to Paisa
Question:

Write a Python program to convert rupees into paisa.

Program:
print("enter rupees")
rs=float(input())
paisa=rs*100
print("paisa=",paisa)
Sample Output:
enter rupees
25
paisa= 2500.0
🔷 PROGRAM 24: KG to Grams
Question:

Write a Python program to convert kilogram into grams.

Program:
print("enter kg")
kg=float(input())
gm=kg*1000
print("grams=",gm)
Sample Output:
enter kg
3
grams= 3000.0
🔷 PROGRAM 25: Swapping Using Third Variable
Question:

Write a Python program to swap two numbers using third variable.

Program:
print("enter a")
a=int(input())
print("enter b")
b=int(input())
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)
Sample Output:
enter a
5
enter b
10
a= 10
b= 5
🔷 PROGRAM 26: Swapping Without Third Variable
Question:

Write a Python program to swap two numbers without third variable.

Program:
print("enter a")
a=int(input())
print("enter b")
b=int(input())
a,b=b,a
print("a=",a)
print("b=",b)
Sample Output:
enter a
7
enter b
9
a= 9
b= 7
🔷 PROGRAM 27: Swapping Using Mathematics
Question:

Write a Python program to swap two numbers using mathematical operations.

Program:
print("enter a")
a=int(input())
print("enter b")
b=int(input())
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)
Sample Output:
enter a
4
enter b
6
a= 6
b= 4
🔷 PROGRAM 28: Total Salary
Question:

Write a Python program to calculate total salary.

Program:
print("enter basic")
basic=float(input())
print("enter hra")
hra=float(input())
print("enter da")
da=float(input())
total=basic+hra+da
print("total salary=",total)
Sample Output:
enter basic
10000
enter hra
2000
enter da
1500
total salary= 13500.0
🔷 PROGRAM 29: Net Salary
Question:

Write a Python program to calculate net salary.

Program:
print("enter total salary")
total=float(input())
print("enter pf")
pf=float(input())
net=total-pf
print("net salary=",net)
Sample Output:
enter total salary
13500
enter pf
500
net salary= 13000.0
🔷 PROGRAM 30: Selling Price
Question:

Write a Python program to calculate selling price.

Program:
print("enter cost price")
cp=float(input())
print("enter profit")
profit=float(input())
sp=cp+profit
print("selling price=",sp)
Sample Output:
enter cost price
500
enter profit
100
selling price= 600.0



🔷 PROGRAM 31: Discounted Price
Question:

Write a Python program to calculate discounted price.

Program:
print("enter price")
price=float(input())
print("enter discount percentage")
disc=float(input())
final=price-(price*disc/100)
print("final price=",final)
Sample Output:
enter price
1000
enter discount percentage
10
final price= 900.0
🔷 PROGRAM 32: GST Calculation (18%)
Question:

Write a Python program to calculate GST amount (18%).

Program:
print("enter price")
price=float(input())
gst_amt=(price*18)/100
print("gst amount=",gst_amt)
Sample Output:
enter price
1000
gst amount= 180.0
🔷 PROGRAM 33: String Repetition
Question:

Write a Python program to repeat a string 5 times.

Program:
print("enter name")
name=input()
print(name*5)
Sample Output:
enter name
Hi
HiHiHiHiHi
🔷 PROGRAM 34: BMI Calculator
Question:

Write a Python program to calculate BMI.

Program:
print("enter weight (kg)")
weight=float(input())
print("enter height (meter)")
height=float(input())
bmi=weight/(height*height)
print("bmi=",bmi)
Sample Output:
enter weight (kg)
60
enter height (meter)
1.7
bmi= 20.761245674740486
🔷 PROGRAM 35: Percentage of 5 Subjects
Question:

Write a Python program to calculate percentage of 5 subjects.

Program:
print("enter marks1")
m1=int(input())
print("enter marks2")
m2=int(input())
print("enter marks3")
m3=int(input())
print("enter marks4")
m4=int(input())
print("enter marks5")
m5=int(input())
total=m1+m2+m3+m4+m5
per=(total/500)*100
print("percentage=",per)
Sample Output:
enter marks1
80
enter marks2
75
enter marks3
70
enter marks4
85
enter marks5
90
percentage= 80.0
🔷 PROGRAM 36: Reverse 2-Digit Number
Question:

Write a Python program to reverse a 2-digit number.

Program:
print("enter 2 digit number")
n=int(input())
rev=(n%10)*10+(n//10)
print("reverse=",rev)
Sample Output:
enter 2 digit number
45
reverse= 54
🔷 PROGRAM 37: Acceleration
Question:

Write a Python program to calculate acceleration.

Program:
print("enter initial velocity")
u=float(input())
print("enter final velocity")
v=float(input())
print("enter time")
t=float(input())
a=(v-u)/t
print("acceleration=",a)
Sample Output:
enter initial velocity
10
enter final velocity
20
enter time
5
acceleration= 2.0
🔷 PROGRAM 38: Force
Question:

Write a Python program to calculate force.

Program:
print("enter mass")
m=float(input())
print("enter acceleration")
a=float(input())
F=m*a
print("force=",F)
Sample Output:
enter mass
5
enter acceleration
2
force= 10.0
🔷 PROGRAM 39: Pressure
Question:

Write a Python program to calculate pressure.

Program:
print("enter force")
F=float(input())
print("enter area")
A=float(input())
P=F/A
print("pressure=",P)
Sample Output:
enter force
100
enter area
5
pressure= 20.0
🔷 PROGRAM 40: Work Done
Question:

Write a Python program to calculate work done.

Program:
print("enter force")
F=float(input())
print("enter distance")
d=float(input())
W=F*d
print("work done=",W)
Sample Output:
enter force
10
enter distance
5
work done= 50.0

Next: Programs 41–50 (Final Set)
Shall I continue?

41 50


🔷 PROGRAM 41: Kinetic Energy
Question:

Write a Python program to calculate kinetic energy.

Program:
print("enter mass")
m=float(input())
print("enter velocity")
v=float(input())
KE=0.5*m*v*v
print("kinetic energy=",KE)
Sample Output:
enter mass
2
enter velocity
3
kinetic energy= 9.0
🔷 PROGRAM 42: Potential Energy
Question:

Write a Python program to calculate potential energy.

Program:
print("enter mass")
m=float(input())
print("enter height")
h=float(input())
g=9.8
PE=m*g*h
print("potential energy=",PE)
Sample Output:
enter mass
5
enter height
2
potential energy= 98.0
🔷 PROGRAM 43: Slope of Line
Question:

Write a Python program to find slope of a line.

Program:
print("enter x1")
x1=float(input())
print("enter y1")
y1=float(input())
print("enter x2")
x2=float(input())
print("enter y2")
y2=float(input())
m=(y2-y1)/(x2-x1)
print("slope=",m)
Sample Output:
enter x1
1
enter y1
2
enter x2
3
enter y2
6
slope= 2.0
🔷 PROGRAM 44: Midpoint Formula
Question:

Write a Python program to find midpoint of two points.

Program:
print("enter x1")
x1=float(input())
print("enter y1")
y1=float(input())
print("enter x2")
x2=float(input())
print("enter y2")
y2=float(input())
x=(x1+x2)/2
y=(y1+y2)/2
print("midpoint x=",x)
print("midpoint y=",y)
Sample Output:
enter x1
2
enter y1
4
enter x2
6
enter y2
8
midpoint x= 4.0
midpoint y= 6.0
🔷 PROGRAM 45: Volume of Cylinder
Question:

Write a Python program to calculate volume of a cylinder.

Program:
print("enter radius")
r=float(input())
print("enter height")
h=float(input())
V=3.14*r*r*h
print("volume=",V)
Sample Output:
enter radius
3
enter height
5
volume= 141.3
🔷 PROGRAM 46: Volume of Cone
Question:

Write a Python program to calculate volume of a cone.

Program:
print("enter radius")
r=float(input())
print("enter height")
h=float(input())
V=(1/3)*3.14*r*r*h
print("volume=",V)
Sample Output:
enter radius
3
enter height
6
volume= 56.519999999999996
🔷 PROGRAM 47: Distance Between Two Points
Question:

Write a Python program to find distance between two points.

Program:
print("enter x1")
x1=float(input())
print("enter y1")
y1=float(input())
print("enter x2")
x2=float(input())
print("enter y2")
y2=float(input())
d=((x2-x1)**2+(y2-y1)**2)**0.5
print("distance=",d)
Sample Output:
enter x1
1
enter y1
2
enter x2
4
enter y2
6
distance= 5.0
🔷 PROGRAM 48: Total Surface Area of Cylinder
Question:

Write a Python program to calculate total surface area of a cylinder.

Program:
print("enter radius")
r=float(input())
print("enter height")
h=float(input())
A=2*3.14*r*(r+h)
print("total surface area=",A)
Sample Output:
enter radius
3
enter height
5
total surface area= 150.72
🔷 PROGRAM 49: Character to ASCII
Question:

Write a Python program to find ASCII value of a character.

Program:
print("enter character")
ch=input()
val=ord(ch)
print("ascii value=",val)
Sample Output:
enter character
A
ascii value= 65
🔷 PROGRAM 50: ASCII to Character
Question:

Write a Python program to convert ASCII value to character.

Program:
print("enter ascii value")
n=int(input())
ch=chr(n)
print("character=",ch)
Sample Output:
enter ascii value
65
character= A