nnumber = int(input("how many terms? "))

n1, n2 = 0, 1
count = 0

if nnumber <= 0:
   print("please enter a positive integer")

elif nnumber == 1:
   print("fibonacci sequence upto",nnumber,":")
   print(n1)

else:
   print("fibonacci sequence:")
   while count < nnumber:
       print(n1)
       nth = n1 + n2
   
       n1 = n2
       n2 = nth
       count += 1