#! /usr/bin/env python3
import sys
num = sys.argv[1]
num = int(num)
if (num>0):
    print('positive')
    if (num <50):
     #   print('smaller than 50')
        if (num%2 ==0):
            print('it is an even number that is smaller than 50')
    else:
        if (num %3 ==0):
            print('it is larger than 50 and divisble by 3')
elif (num==0):
    print('equal to 0')
else:
    print('negative')
