#!usr/bin/python
# coding = utf-8

#Aspect ratio program
def give_ratio():
    width = int(input("Screen width: "))
    height = int(input("Screen height: "))
    while True:
        if (width / 2).is_integer() and (height / 2).is_integer():
            width = (width / 2)
            height = (height / 2)
        elif (width / 3).is_integer() and (height / 3).is_integer():
            width = (width / 3)
            height = (height / 3)
        elif (width / 5).is_integer() and (height / 5).is_integer():
            width = (width / 5)
            height = (height / 5)
        else:
            width = int(width)
            height = int(height)
            break
    print("Aspect ratio: {}:{}".format(width, height))
    menu()
    
def create_resolution_width():
    width_aspect = int(input("Width of aspect ratio: "))
    height_aspect = int(input("Height of aspect ratio: "))
    width_input = int(input("Width of display (in pixels): "))
    width = int(width_input)
    height = int((width_input / width_aspect) * height_aspect)
    print("Display resolution: {} x {}".format(width, height))
    menu()
    
def create_resolution_height():
    width_aspect = int(input("Width of aspect ratio: "))
    height_aspect = int(input("Height of aspect ratio: "))
    height_input = int(input("Height of display (in pixels): "))
    height = int(height_input)
    width = int((height_input / height_aspect) * width_aspect)
    print("Display resolution: {} x {}".format(width, height))
    menu()

def menu():
    print(  "Would you like like to?"
            "\n1. Determine an aspect ratio based on a resolution"
            "\n2. Determine a resolution based on an aspect ratio and a width"
            "\n3. Determine a resolution based on an aspect ratio and a height"
            "\n4. Exit"
        )
    answer = int(input())
    if answer == 1:
        give_ratio()
    elif answer == 2:
        create_resolution_width()
    elif answer == 3:
        create_resolution_height()
    elif answer == 4:
        exit
    else:
        print("That isn't an option.")
            
menu()
