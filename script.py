#EX 1
#aX^2 + bX + c = 0
# def quadraticEquation(a,b,c):
#     delta = (b)**2.0 - (4.0*a*c)
#     if (delta < 0):
#         x1 = complex(-b/(2.0*a),((delta*-1.0)**0.5)/2.0*a)
#         x2 = complex(-b/(2.0*a),-((delta*-1.0)**0.5)/2.0*a)
#     elif (delta > 0):
#         x1 = ((-b + ((delta)**0.5))/(2.0*a))
#         x2 = ((-b - ((delta)**0.5))/(2.0*a))
#     else:
#         x1 = ((-b + ((delta)**0.5))/(2.0*a))
#         x2 = x1
#     return (x1,x2)

# print(quadraticEquation(1,3,1))




#EX2

# money = input("How amount of money do you have? ")
# print("You have amount of money " , money)
# if int(money) < 10:
#     need = 10 - int(money)
#     print("You will need", need , "$ of money afford")
# else:
#     print("You don't need to affor the money an additional")




#EX3
# for i in range(99 ,0 ,-1):
#     print(i ,"Bottles of Beer")


#EX4
# num = input("inter the number")
# num = int(num)
# # check if the number is negative, positive or zero
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#     for i in range(1,num +1):
#         factorial = factorial*i
#     print("The factorial of",num,"is",factorial)




#EX5
num = input("inter the number")
num = int(num)
# check if the number is negative, positive or zero
factors = 0
if num < 0:
   print("Sorry, factors does not exist for negative numbers")
elif num == 0:
   print("The factors of 0 is 0")
else:
    for i in range(1,num +1):
        if num % i == 0:
            print(i, "Is factors of", num)
            factors = factors + i
    print("the sum of factors is :",factors)
