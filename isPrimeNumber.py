
# coding: utf-8



import math

def isPrimeNumber(a): # time Complexity(n^1/2)
    i=3
    
    if a==1:
        print("False")
        return False
    if (a%2==0):
        if a==2:
            print("True")
            return True
        else: 
            print("False")
            return False
    while(i<math.sqrt(a)):
        if(a%i==0):
            print("False")
            return False
        i+=1
    print("True")
    return True



if __name__ == "__main__":
    isPrimeNumber(55)
    isPrimeNumber(2)
    isPrimeNumber(1)
    isPrimeNumber(6)







