def fibonacci():
    a,b=0,1
    #print(a,b)
    n=int(input("Enter the Length = "))
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
print("Fibonacci Series is as follows: ")
fibonacci()
print("Done Successfully.")
print("Bye Bye")

        
    
        
