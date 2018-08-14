#!/usr/bin/env python
row_1 = [16,32,16,0]
row_2 = [32,0,32,16]
row_3 = [16,32,16,32]
row_4 = [0 ,0,0 ,0]

row_4[1]=''

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

