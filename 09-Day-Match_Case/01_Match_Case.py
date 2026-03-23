Number = int(input("Enter Your Number Between 1 to 10: "))

match Number:
    case 2:
        print("You Won This Game.")
    case 5:
        print("You Give Money To Partha.")
    case 9:
        print("You Lost The Game.")
    case _:
        print("Invalid choice or no result.")