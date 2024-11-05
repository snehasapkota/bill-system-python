
import read
import operation


l = read.read_furniture_details()
print(l)


line = "-"*70

print(line)
print(" ")
print("\t\t WELCOME TO BRJ FURNITURE NEPALI")
print(" ")
print(line)
print("\n")


# for program continuation creating loop

loop = True
while loop:
    # menu options
    print(' ')
    print("\t1) press 1 to display furniture.")
    print("\t2) press 2 to order furniture.")
    print("\t3) press 3 to sell furniture.")
    print("\t4) press 4 to to exit from the program.")
    print(" ")
    print(line)

    try:

        choice = int(input("Enter the option:"))

        if choice == 1:
            print("furniture displayed")
            operation.display_furniture(l)
        elif choice == 2:
             operation.buy_furniture()
             print("furniture ordered")
        elif choice == 3:
             print("furniture sell")
             operation.sell_furniture()
        elif choice == 4:
            print("exiting form the program....")
            loop = False
        else:
            print("\t*Enter a valid option*")

    except:
        print(line)
        print("\t*Enter the number*")
        print(line)
