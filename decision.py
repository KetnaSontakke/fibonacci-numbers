n= int(input("How many terms? "))

# first two terms
t1, t2 = 0, 1
count = 0

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(t1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(t1)
       nth = t1 + t2
       # update values
       t1 = t2
       t2 = nth
       count += 1
