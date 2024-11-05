import read
import datetime

'''In this operation file, there is code for displaying the furniture, buing/purchasing furniture and selling furniture,
while buying furniture one should not include vat and shipping cost according to quaction but for selling furinture one should add vat and shipping cost'''


vat = 0.13
date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month)+ "-" + str(datetime.datetime.now().day)
time = str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
date_time = date + "-" + time


def display_furniture(furniture_list):
    print("\n\t AVAILABLE FURNITURE:")
    for furniture in furniture_list:
        print("Unique ID:", furniture[0], "Manufacture:", furniture[1], "Furniture type:", furniture[2], "Quantity:", furniture[3], "Price per piece:", furniture[4])
    #transaction_process(furniture_list,1)


def buy_furniture():
    print("\t\t BUY A Furniture ")
    print("\n")
    
    furnituress = read.read_furniture_details()
        
    line = "-"*70
    name = input("Enter your name:").lower()
    phone_number = int(input("Enter your phone number:"))
    company = input("Enter your company name:").lower()
    
    status = True

    while status:
        furniture_Id = int(input("Enter the furniture ID:"))
        
        furniture_name = input("Enter the name of the furniture you want to buy:")

        found = False  # To check if ID is found
        
        for furniture in furnituress:
            if furniture[0] == furniture_Id:
                try:
                    furniture_quantity_buy = int(input("Enter the quantity:"))
                except ValueError:
                    print("Please enter a numeric value.")
                    continue

                if furniture_quantity_buy > 0:
                    furniture[3] = furniture[3] + furniture_quantity_buy
                    total_amount = furniture[4] * furniture_quantity_buy
                    print("Successful Transaction")
                    print(line)
                    print("Total cost: " + str(total_amount))
                    print(line)
                    found = True
                else:
                    print("Please enter a quantity greater than zero!")
                break
        
        if not found:
            print("The given furniture ID was not found.")
        
        buy_more = input("Do you want to buy more? (yes/no):").lower()
        if buy_more != "yes":
            print("Thank you for your purchase")
            status = False
#buy_furniture()

            

def sell_furniture():
    print("\t\t SELL A Furniture ")
    print("\n")
    
    furnituress = read.read_furniture_details()

    line = "-"*70
    name = input("Enter your name:").lower()
    phone_number = int(input("Enter your phone number:"))
    
    VAT = 0.13  # Assuming 15% VAT
    

    status = True

    while status:
        furniture_name = input("Enter the name of furniture you want to sell:").lower()
        item = input("Is the item available? (yes/no) \n")
        
        if item.lower()== "yes":
            
            furniture_Id = int(input("Enter the furniture ID:"))
            company = input("Enter your company name:").lower()
            
            found = False
        
            for furniture in furnituress:
                if furniture[0] == furniture_Id:

                    
                    try:
                        furniture_quantity_sell = int(input("Enter the quantity:"))
                    except:
                        print("Please enter a numeric value.")
                        continue
                
                    if furniture_quantity_sell > 0 and furniture_quantity_sell <= furniture[3]:
                        furniture[3] = furniture[3] - furniture_quantity_sell
                        total_cost = furniture[4] * furniture_quantity_sell
                        vat_amount = VAT * total_cost

                        

                        shipping_option = input("Enter the shipping option(within valley/outside valley/in person):").lower()
                        if shipping_option == "within valley":
                            SHIPPING_COST = 1000
                        elif shipping_option == "outside valley":
                            SHIPPING_COST = 1500
                        elif shipping_option == "in person":
                            SHIPPING_COST = 0
                        else:
                            print("Invalid option")
                            continue

                        
                        final_cost = total_cost + vat_amount + SHIPPING_COST
                        print("Transaction successful!")
                        print(line)
                        print("Date:" + date_time)
                        print("Total Cost: " + str(total_cost))
                        print("VAT: " + str(vat_amount))
                        print("Shipping Cost: " + str(SHIPPING_COST))
                        print(line)
                        print("Final Cost: " + str(final_cost))
                        print(line)
                        found = True

                        
                    else:
                        print("Please enter a valid quantity (greater than zero and within available stock).")
                        continue
        
            if found:
                status = False
                sell_more = input("Do you want to sell more furniture? (yes/no):").lower()
                if sell_more == "yes":
                    status = True
                    
                else:
                    print("Thank you for using our service")
            else:
                print("The given furniture ID is not found.")

                
        elif item.lower() == "no":
            print("Item not available")
            break
        else:
            print("Invalid input")
             
#sell_furniture()
        
        
            

        

          




        

    

    


            
            
                
                
                           
                           
        
    

    
    
    



    
        
