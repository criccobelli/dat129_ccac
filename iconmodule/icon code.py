#asking for user's icon and changing 0s to -s and 1s to Xs:
seq = list(input("Please enter a 100 character binary sequence: "))

for x in range(0, len(seq)):
    seq[x] = int(seq[x])

for i in range (len(seq)):
    if seq[i] == 1:
        seq[i] = "X"
    if seq [i] == 0:
        seq[i] = "-" 

#separate 100 characters into 10 rows of 10:
line1 = seq[0:10]
line2 = seq[10:20]
line3 = seq[20:30]
line4 = seq[30:40]
line5 = seq[40:50]
line6 = seq[50:60]
line7 = seq[60:70]
line8 = seq[70:80]
line9 = seq[80:90]
line10 = seq[90:100]

#printing each line to show the icon:
def visualDisplay():
    for value in line1:
        print(value, end='')
    print('\n')
    for value in line2:
        print(value, end='')
    print('\n')
    for value in line3:
        print(value, end='')
    print('\n')
    for value in line4:
        print(value, end='')
    print('\n')
    for value in line5:
        print(value, end='')
    print('\n')
    for value in line6:
        print(value, end='')
    print('\n')
    for value in line7:
        print(value, end='')
    print('\n')
    for value in line8:
        print(value, end='')
    print('\n')
    for value in line9:
        print(value, end='')
    print('\n')
    for value in line10:
        print(value, end='')
    print('\n')

def main():
	print("Visual display of your icon:")
	visualDisplay()
main()

#ask user if they want to reverse the icon:
rev = input("Do you want to reverse your icon? ")

#reverse each line and print icon:
if rev == "yes" or rev == "Yes":
    print('\n')

    stringlength = len(line1)
    slicedString = line1[stringlength::-1]
    print (slicedString)

    stringlength = len(line2)
    slicedString = line2[stringlength::-1]
    print (slicedString) 

    stringlength = len(line3)
    slicedString = line3[stringlength::-1]
    print (slicedString) 

    stringlength = len(line4)
    slicedString = line4[stringlength::-1]
    print (slicedString) 

    stringlength = len(line5)
    slicedString = line5[stringlength::-1]
    print (slicedString) 

    stringlength = len(line6)
    slicedString = line6[stringlength::-1]
    print (slicedString) 

    stringlength = len(line7)
    slicedString = line7[stringlength::-1]
    print (slicedString) 

    stringlength = len(line8)
    slicedString = line8[stringlength::-1]
    print (slicedString) 

    stringlength = len(line9)
    slicedString = line9[stringlength::-1]
    print (slicedString) 

    stringlength = len(line10)
    slicedString = line10[stringlength::-1]
    print (slicedString)
