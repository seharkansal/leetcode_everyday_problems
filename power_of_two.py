def pow_two(n):
    if n==0:
        return False

    while n%2==0:
        n=n//2
    
    if n==1:
        return True
    else:
        return False

n=int(input("enter a number:"))
print(pow_two(n))




        
    
