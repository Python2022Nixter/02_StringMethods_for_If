# input pytamide heigth
DRAW_SYMBOL = "✡︎"
SPACEER = " "
'''
        *
       * *
      * * *
'''

heigth = int(input("Enter heigth: "))
# for row_counter in range(heigth):
#     print((heigth - row_counter ) * SPACEER + (row_counter) * (DRAW_SYMBOL + SPACEER))
#     pass

for row_counter in range(heigth):
    print()
    for blocks_counter in range(heigth - row_counter):
        print(SPACEER, end="")
    for blocks_counter in range(row_counter):
        print(DRAW_SYMBOL + SPACEER, end="")
    pass
