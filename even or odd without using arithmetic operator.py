'''num=int(input('enter a number'))
if num&1==0:
    print('even')
else:
    print('odd')
'''

'''num=int(input('enter a number'))
if num^1==num+1:
    print('even')
else:
    print('odd')
'''

num=int(input('enter a number'))
s=str(num)
if s[-1] in '02468':
    print('even')
else:
    print('odd')
    
