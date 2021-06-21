'''
*****
****
***
**
*
'''

for n in range(0,5):
    for m in range(0,5-n):
        print('*',end='')
    print('')

for n in range(5,0,-1):
    for m in range(n):
        print('*',end='')
    print('')
