# a= 4
# b= 6
# c= 7
# Average=(a+b+c)/3.0 
# print (Average)

# a1= 8
# b2= 9
# c3= 10
# Average=(a1+b2+c3)/3 
# print (Average)


# def average(a,b,c):
#     average=(a+b+c)/3.0
#     print(average)

# a= 4
# b=3
# c= 7
# average(a,b,c)

# a1=  2
# b1=  3
# c1=  5
# average(a1,b1,c1)




def ifvote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")

def check_height(height):
    if height >= 150:
        print("Height is sufficient")
    else:
        print("Height is low")

age = int(input("Enter your age: "))
ifvote(age)

height = int(input("Enter your height: "))
check_height(height)



def average(a,b,c):
    d=(a+b+c)/3.0
    print (d)
average(4,5,6) 
average(7,8,9) 
average(10,11,12)





def average(a,b,c):
    d=(a+b+c)/3.0
    return d

a1 = average(4,5,6)
b1 = average(7,8,9)
c1 = average(10,11,12)
print(a1)
print(b1)
print(c1)