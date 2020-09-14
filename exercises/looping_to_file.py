"""for i in range(10, 0, -1):
    for j in range(i):
        print(j, end='')
    print()
"""
"""
myfile = open('looping_to_file_print.txt', mode='w')
for i in range(10, 0, -1):
    for j in range(i):
        print(j, end='')
    print()
"""    
    
myfile = open('looping_to_file_print.txt', mode='w')
for i in range(10, 0, -1):
    for j in range(i):
        myfile.write(str(j))
    myfile.write('\n')