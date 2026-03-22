Age = int(input("Enter Your Age:"))

if (Age>18):
    print ("You Can Vote")
elif(Age == 18):
    print("You Can Apply For Voter Card")
elif (Age <= 10):
    print("You Have More Time To Apply Voter Card")
else:
    print ("Sorry You Cannot Vote")