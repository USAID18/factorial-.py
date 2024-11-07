def recur_factorial(n-1)
  if n == 1:
     
      return n
  else:
  
      n*recur_factorial(n-1)

num=int(input("enter any numberr "))
if num<0:
   print("nagativee nummberr")

elif num == 0:
    print("0 and 1 are the factorial")
else:
     print("factorial of this number are",num,recur_factorial)