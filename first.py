

# 	WAP to calculate the bill amount for an item given as  quantity sold, value, discount and tax. 👉

value = int(input("Pls Enter the value of an item : \n "))
itemcount = int(input("Pls Enter how many item you purchase : \n"))

# i'll take discount and tax static 
discount = 10;
tax = 5
total_price = value * itemcount
discount_price = total_price - total_price * discount/100
final_price = discount_price + discount_price*tax/100
print ("Your Fianl Price is : ",final_price ) 


# 2nd Program Start From Here 👉
# 	WAP to convert degree fahrenheit  into celsius.

c = float(input("Pls Enter the degree celcious : "))
f = c * (9/5) + 32
print("fahrenheit : " , f)

# 3rd  wap to calculate as e = mc2 where m is the mass of the object and c is velocity 👉 

m = float(input("Pls enter the Mass of the object : \n"))
c = float(input("Pls enter the velocity of object : \n"))
e = m * (c*c)
print("The value of e : " , e)


# 4 WAP to print the ASCII value of character 👉
c = input("Pls Enter any value : ")
a = ord(c)
print("ASCII value of your charcter : ", a)



#5 Wap to swap num using temp variable 👉
a = int(input("Pls enter first value : \n"))
b = int(input("Pls enter sec. value : \n"))
print("before swaping the value a and b = ", a , b)
temp = a
a = b
b = temp
print("before swaping the value a and b = ", a , b)

#6 wap to calculate salary of an emplyee given his basic pay ( to enterd by the user ). HRA = 10% to basic pay , TA = 5% to basic pay , 
# define hra & ta as constats and use them to calculate the salary of an employee ? 👉

salary = int(input("Enter Your basic Salary : "))
hra = salary * 10/100
tra = salary * 5/100
finalsalary = salary + hra + tra
print("Your Final Salary (including hra and tra) : " , finalsalary )

# 	What is implicit and explicit type conversion? Give an example.

# in inplicit python interpreter change data vlaue acording to your value 
# ex: 
from stringprep import c9_set


a = 10
b = 10.68
print(" type of a and b is  \n", type(a) , type(b))
c = a+b 
print("We have both value in c ( int and float ) so it's data type is : \n" , type(c))

# # in explict we change data format according to our need like :
a = input("Pls enter any number : \n")
b = type(a) 
print("data type of enter value is : \n" , b)
c = int(a)
print("after change the data type is : \n" , type(c))


