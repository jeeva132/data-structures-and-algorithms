def prime(a):
    prime = False
    if a == 1:
        print('no is not a prime')
     
    elif a >1:
        
        for i in range(2,a):
            if a%i == 0:
                prime = True 
                break

        if prime:
            return 'not prime'
        else:
            return 'prime'
prime(2)