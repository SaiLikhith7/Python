file=open("C:/Users/Sadiq/Demo/testdata.txt","r")

print(file.read())

file.close()

file=open("C:/Users/Sadiq/Demo/testdata.txt","r")

print(file.readlines())

file.close()

file=open("C:/Users/Sadiq/Demo/testdata.txt","r")

print(file.readline())

file.close()

file=open("C:/Users/Sadiq/Demo/testdata.txt","a")

file.write('This is my Third Line\n')

file.close()

file=open("C:/Users/Sadiq/Demo/testdata.txt","r")

for l in file:
      print(l)
file.close()