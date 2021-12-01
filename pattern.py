n=9
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        k+=1
        if i<=j:
            print(k,end=' ')
        else:
            print(' ',end=' ')
        
    print( )
           
        
