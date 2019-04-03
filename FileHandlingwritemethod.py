"""file=open("C:/Users/Sadiq/Demo/testdata.txt","w")

file.write('This is my First Line\n')
file.write('This is my Second Line\n')

file.close()"""



file=open("C:/Users/Sadiq/Demo/testdata.txt","r")

for l in file:
    print(l)

file.close()