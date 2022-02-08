import life # for importing file 
# print(life.name)
# print(life.age)

# import life as l # here l is alias name means you short the name
# print(l.name)


# third way to import a file 
# from life import age
# print(age)

# import function from another file
# import function 
# print(function.cube(8))


# import math
# num = int(math.sqrt(4))
# print(num)

# how to print any month calender from this month
import calendar 
# print(calendar.month(2022,2))

#wap to print the calender of given year of all month
y = int(input("Enter the Year : "))
for i in range(1,13):
    print(calendar.month(y,i))
