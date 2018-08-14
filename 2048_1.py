import random 
import os


row_1 = [4,16,8,0]
row_2 = [4,16,4,0]
row_3 = [2,16,2,2]
row_4 = [2,4,2,0]


print_row_1 = " ".join('{:5}'.format(item) for item in row_1)
print_row_2 = " ".join('{:5}'.format(item) for item in row_2)
print_row_3 = " ".join('{:5}'.format(item) for item in row_3)
print_row_4 = " ".join('{:5}'.format(item) for item in row_4)

print(print_row_1)
print(print_row_2)
print(print_row_3)
print(print_row_4)
'''
user_input = input('Please press "w","a","s" or "d":')
'''
occupied_block = []
def w_reaction():
    i = 0
    
    while i < 3:
        for x in range(0,4):
            if row_1[x] == 0:
                row_1[x] = row_2[x]
                row_2[x] = 0
            elif row_1[x] == row_2[x] and row_1 != 0 and [1,x] not in occupied_block and [2,x] not in occupied_block:
                row_1[x] = row_1[x] + row_2[x]
                row_2[x] = 0
                occupied_block.append([1,x])

            if row_2[x] == 0:
                row_2[x] = row_3[x]
                row_3[x] = 0
            elif row_2[x] == row_3[x] and row_2 != 0 and [2,x] not in occupied_block and [3,x] not in occupied_block:
                row_2[x] = row_2[x] + row_3[x]
                row_3[x] = 0
                occupied_block.append([2,x]) 
            
            if row_3[x] == 0:
                row_3[x] = row_4[x]
                row_4[x] = 0
            elif row_3[x] == row_4[x] and row_3 != 0 and [3,x] not in occupied_block and [4,x] not in occupied_block:
                row_3[x] = row_3[x] + row_4[x]
                row_4[x] = 0
                occupied_block.append([3,x])

        i = i + 1
    
w_reaction()
print_row_1 = " ".join('{:5}'.format(item) for item in row_1)
print_row_2 = " ".join('{:5}'.format(item) for item in row_2)
print_row_3 = " ".join('{:5}'.format(item) for item in row_3)
print_row_4 = " ".join('{:5}'.format(item) for item in row_4)

print('......................................................................')
print(print_row_1)
print(print_row_2)
print(print_row_3)
print(print_row_4)
      
print(occupied_block)
