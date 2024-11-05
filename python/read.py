def read_furniture_details():  # to read details from file
    file = open("furniture.txt", "r")#path to the file
    furniture_list = []
    for furniture in file:
        row = furniture.replace("\n", "").replace("$", "").split(',')
        store = [int(row[0]), (row[1]), (row[2]), int(row[3]), int(row[4])]
        furniture_list.append(store)
    file.close()
    return furniture_list


#print(display_furniture_details())

