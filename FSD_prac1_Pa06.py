myList = [4, 12, 999, 42, 26, 6969, 8, 18]
def bubbleSort(myList):
    for passnum in range(len(myList)-1,0,-1):
        for i in range(passnum):
            if myList [i]>myList[i+1]:
                top7 = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = top7

x = int(input("Enter a number "))

found = False

for i in range(len(myList)):
 if(myList[i] == x):
  found = True
  print("%d found at %dth position"%(x,i))
  break

if(found == False):
 print("%d is not in list"%x)


bubbleSort(myList)
print(myList)


