def fibonacci():
    a,b=0,1
    #print(a,b)
    n=int(input("Enter the length"))
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
fibonacci()

        
    
        
