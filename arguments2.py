import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = 9.00
currnet_amount = 0

if b-a > 0 :
    currnet_amount = (b-a) * c
    print(f'current bill amount : {currnet_amount}')
