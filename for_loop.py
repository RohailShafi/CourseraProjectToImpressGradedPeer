# for i in range(7):
#     for j in range(i+1):
#         print('*',end='')
#     print('\n')
    
# print('\n\tNext\t\n')
# i=0
# for i in range(7):
#     for j in range(7-i):
#         print('*',end='')
#     print('\n')

# for i in range(7):
#     for j in range(i+1):
#         print('*     ',end='')
#     print('\n')
    
# print('\n\tNext\t\n')
# i=0
# for i in range(7):
#     for j in range(7-i):
#         print('*     ',end='')
#     print('\n')

n = int(input('Enter your number to calculate sum '))
total = 0
avg = 0
for i in range(1,n+1):
    total = total + i
print(f'Sum of number from 1 to {n} : {total}\n Average : {total/n}')