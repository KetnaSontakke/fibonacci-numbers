j=int(input("Enter the terms : "))
i=0                                         #first element of series
t=1                                         #second element of series
if j<=0:
    print("The requested series is", i)
else:
    print(i,t,end=" ")
    for x in range(2,j):
        next=i+t                           
        print(next,end=" ")
        i=t
        t=next
