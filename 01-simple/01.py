def square():

 myList=[]
 num = 0

 while num < 5:
      num+=1
      result=int(input("Enter the number: "))
      myList.append(result**2)

 return myList


print(square())
