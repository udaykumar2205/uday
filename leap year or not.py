year=int(input('enter year'))
if (year%100!=0 and year%4==0)or(year%100==0 and year%400==0):
     print('a leap year')
else:
    print('not a leap year')
   
