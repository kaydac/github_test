# def add(x, y):
#     return x + y
#
# print(add(6,7))
#
# def add(x, y):
#     return x + y
#
#
# print("Here it is")
#
# x = 4
# print(x)
#
# y = input(" Type Y: ")
#
# print(y)


# Ask the User to Do ADD, SUb, div or mul
# get the 2 inputs
# display/Print the desired output

# print("add,sub,div, or mul something")
# y=int(input("Enter y"))
# x=int(input("Enter x"))
# #
# # y = int(y)
# # x = int(x)
#
# print(x+y,x-y,x/y,x*y)
#
#

print("Enter number of what you want to do")
print("1.Add" "\n" "2.Subtract" "\n" "3.Multiply")

z=int(input("Enter Here:"))
if z >= 4:
    print("invalid option")

elif z == 1:
    print("You Chose ADDITION ")
    x=float(input("Enter First Number:"))
    y=float(input("Enter Second Number:"))
    if x|y < 0:
            print('invalid input try again')

    else:
        print("ANSWER:",x+y)

elif z == 2:
    print("You Chose SUBTRACTION ")
    x=float(input("Enter First Number:"))
    y=float(input("Enter Second Number:"))
    if x|y < 0:
            print('invalid input try again')

    else:
        print("ANSWER:",x-y)



elif z == 3:
    print("You Chose MULTIPLICATION ")
    x=float(input("Enter First Number:"))
    y=float(input("Enter Second Number:"))
    if x | y < 0:
            print('invalid input try again')

    else:
        print("ANSWER:",x*y)
