color_names={"Alice Blue":"#f0f8ff", "Antique White":"#faebd7","Antique White 1":"#ffefdb", "Antique White 2":"#eedfcc"}
color = input("Enter color name: ")
while color != "":
    if color in color_names:
        print(color, "is", color_names[color])
    else:
        print("Invalid color")
    color = input("Enter color name: ")
