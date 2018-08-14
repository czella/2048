import random 
import os
import time
import itertools

row_1 = [16,32,16,0]
row_2 = [32,0,32,16]
row_3 = [16,32,16,32]
row_4 = [0,0,0,0]

g = 0


current_score = 0

def print_table():
    print_row_1 = "  | ".join('{:4}'.format(item) for item in row_1)
    print_row_2 = "  | ".join('{:4}'.format(item) for item in row_2)
    print_row_3 = "  | ".join('{:4}'.format(item) for item in row_3)
    print_row_4 = "  | ".join('{:4}'.format(item) for item in row_4)

    print (print_row_1)
    print ("---------------------------------")
    print (print_row_2)
    print ("---------------------------------")
    print (print_row_3)
    print ("---------------------------------")
    print (print_row_4)
    print ("Score = ",current_score)

def check_if_gameover():

    matrix = [row_1,row_2,row_3,row_4]
    check_zero = []
    for x in range (0,4):
        check_zero.append(row_1[x])
        check_zero.append(row_2[x])
        check_zero.append(row_3[x])
        check_zero.append(row_4[x])

    gameover_value = 0

    for x,y in itertools.product (range(0,4),range(1,4)):
        if matrix [x][y] == matrix [x][y - 1]:
            gameover_value = gameover_value + 1
        if matrix [y][x] == matrix [y - 1][x]:
            gameover_value = gameover_value + 1
    if gameover_value == 0 and 0 not in check_zero:
        print ('You lose!')
        print (check_zero)
        print_table()
        time.sleep(5)
        global g
        g = g + 1
        
    else:
        print('value' ,gameover_value)


        
    



def number_generator():
    nulls_places = [[],[],[],[]]

    for x in range (0,4):
        if row_1[x] == 0:
            nulls_places[0].append(x)
        if row_2[x] == 0:
            nulls_places[1].append(x)
        if row_3[x] == 0:
            nulls_places[2].append(x)
        if row_4[x] == 0:
            nulls_places[3].append(x)
    temp_nulls = []


    for x in range (0,4):
        if len(nulls_places[x]) != 0:
            temp_nulls.append(x)
    n_temp_nulls = len(temp_nulls)

    if n_temp_nulls > 0:
        random_row = random.choice(temp_nulls)
        two_or_four =[2,4]        
        if random_row == 0:
            rand_1 = random.choice(nulls_places[0])
            row_1[rand_1] = random.choice(two_or_four)
        elif random_row == 1:
            rand_2 = random.choice(nulls_places[1])
            row_2[rand_2] = random.choice(two_or_four)
        elif random_row == 2:
            rand_3 = random.choice(nulls_places[2])
            row_3[rand_3] = random.choice(two_or_four)
        elif random_row == 3:
            rand_4 = random.choice(nulls_places[3])
            row_4[rand_4] = random.choice(two_or_four)

    
def w_reaction():
    i = 0
    occupied_block = []
    global current_score
    while i < 3:
        for x in range(0,4):
            if row_1[x] == 0:
                row_1[x] = row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
            elif row_1[x] == row_2[x] and row_1 != 0 and [1,x] not in occupied_block and [2,x] not in occupied_block:
                row_1[x] = row_1[x] + row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([1,x])
                current_score = current_score + row_1[x]

            if row_2[x] == 0:
                row_2[x] = row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
            elif row_2[x] == row_3[x] and row_2 != 0 and [2,x] not in occupied_block and [3,x] not in occupied_block:
                row_2[x] = row_2[x] + row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([2,x])
                current_score = current_score + row_2[x] 
            
            if row_3[x] == 0:
                row_3[x] = row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
            elif row_3[x] == row_4[x] and row_3 != 0 and [3,x] not in occupied_block and [4,x] not in occupied_block:
                row_3[x] = row_3[x] + row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                occupied_block.append([3,x])
                current_score = current_score + row_3[x]

        i = i + 1

def s_reaction():
    i = 0
    occupied_block = []
    global current_score
    while i < 3:
        for x in range(0,4):
            if row_4[x] == 0:
                row_4[x] = row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
            elif row_3[x] == row_4[x] and row_3 != 0 and [3,x] not in occupied_block and [2,x] not in occupied_block:
                row_4[x] = row_3[x] + row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([3,x])
                current_score = current_score + row_4[x]

            if row_3[x] == 0:
                row_3[x] = row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
            elif row_2[x] == row_3[x] and row_2 != 0 and [2,x] not in occupied_block:
                row_3[x] = row_2[x] + row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([2,x])
                current_score = current_score + row_3[x] 

            if row_2[x] == 0:
                row_2[x] = row_1[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
            elif row_1[x] == row_2[x] and row_1 != 0 and [1,x] not in occupied_block and [2,x] not in occupied_block:
                row_2[x] = row_1[x] + row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                occupied_block.append([1,x])
                current_score = current_score + row_2[x]
    
        i = i + 1
def a_reaction():
    i = 0
    occupied_block = []
    global current_score
    while i < 3:
        for x in range (1,4):
            if row_1[x-1] == 0:
                row_1[x-1] = row_1[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
            elif row_1[x-1] == row_1[x] and row_1[x-1] != 0 and [1,x] not in occupied_block and [1,x-1] not in occupied_block:
                row_1[x-1] = row_1[x-1] + row_1[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                occupied_block.append([1,x-1])
                current_score = current_score + row_1[x-1]

            if row_2[x-1] == 0:
                row_2[x-1] = row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
            elif row_2[x-1] == row_2[x] and row_2[x-1] != 0 and [2,x] not in occupied_block and [2,x-1] not in occupied_block:
                row_2[x-1] = row_2[x-1] + row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([2,x-1])
                current_score = current_score + row_2[x-1]

            if row_3[x-1] == 0:
                row_3[x-1] = row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
            elif row_3[x-1] == row_3[x] and row_3[x-1] != 0 and [3,x] not in occupied_block and [3,x-1] not in occupied_block:
                row_3[x-1] = row_3[x-1] + row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([3,x-1])
                current_score = current_score + row_3[x-1]

            if row_4[x-1] == 0:
                row_4[x-1] = row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
            elif row_4[x-1] == row_4[x] and row_4[x-1] != 0 and [4,x] not in occupied_block and [4,x-1] not in occupied_block:
                row_4[x-1] = row_4[x-1] + row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                occupied_block.append([4,x-1])
                current_score = current_score + row_4[x-1]

        i = i + 1

def d_reaction():
    i = 0
    occupied_block = []
    global current_score
    while i < 3:
        for x in range (0,3):
            if row_1[x+1] == 0:
                row_1[x+1] = row_1[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
            elif row_1[x+1] == row_1[x] and row_1[x+1] != 0 and [1,x] not in occupied_block and [1,x+1] not in occupied_block:
                row_1[x+1] = row_1[x+1] + row_1[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                occupied_block.append([1,x+1])
                current_score = current_score + row_1[x+1]

            if row_2[x+1] == 0:
                row_2[x+1] = row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
            elif row_2[x+1] == row_2[x] and row_2[x+1] != 0 and [2,x] not in occupied_block and [2,x+1] not in occupied_block:
                row_2[x+1] = row_2[x+1] + row_2[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([2,x+1])
                current_score = current_score + row_2[x+1]

            if row_3[x+1] == 0:
                row_3[x+1] = row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
            elif row_3[x+1] == row_3[x] and row_3[x+1] != 0 and [3,x] not in occupied_block and [3,x+1] not in occupied_block:
                row_3[x+1] = row_3[x+1] + row_3[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([3,x+1])
                current_score = current_score + row_3[x+1]

            if row_4[x+1] == 0:
                row_4[x+1] = row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
            elif row_4[x+1] == row_4[x] and row_4[x+1] != 0 and [4,x] not in occupied_block and [4,x+1] not in occupied_block:
                row_4[x+1] = row_4[x+1] + row_4[x]
                print_table()
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                occupied_block.append([4,x+1])
                current_score = current_score + row_4[x+1]

        i = i + 1



number_generator()
number_generator()

while g < 1:
    print_table()
    user_input = input('Please press "w","a","s" or "d":')
    os.system("cls" if os.name == "nt" else "clear")
    if user_input == "q":
        break
    if user_input == "w":
        w_reaction()
    elif user_input == "s":
        s_reaction()
    elif user_input == "a":
        a_reaction()
    elif user_input == "d":
        d_reaction()
    number_generator()
    check_if_gameover() 
    


      

