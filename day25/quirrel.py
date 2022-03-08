# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

import pandas

data = pandas.read_csv("squirrel.csv")


# Create a spreadsheet with

# Index, color, number of quirrel
# three colors: Gray, Black, Red




primary_color = data["Primary Fur Color"].to_list()

primary_color_1 = data[data["Primary Fur Color"] == "Gray"]
print(type(primary_color_1))

def get_number_of_quirrel(color, color_list):
    count = 0
    for i in color_list:
        if i == color:
            count += 1
    return count

new_data = {
    "color": ["Gray", "Black", "Red"],
    "number": [get_number_of_quirrel("Gray", primary_color),
               get_number_of_quirrel("Black", primary_color),
               get_number_of_quirrel("Red", primary_color)]
}


new_quirrel_table = pandas.DataFrame(new_data)

print (new_quirrel_table.to_csv())



