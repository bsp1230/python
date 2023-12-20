import os
f = open('Dates.py')

print(f.readline())

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")


#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())
try:
    if os.path.dirname('temp'):
        print('Filenot exist')
        
    if os.path.exists('demofile2.txt'):
        os.remove('demofile2.txt')
    else:
        print('Filenot exist')
except:
    print('Error in file deleting')  