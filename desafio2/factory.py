import math

def verify(a,m):
    k = 1
    while(k < math.log(m,2) + 1):
        if((a*(2**k))%m == 0):
            return True
        k += 1
    return False

def main():
    x = input().split()
    a = int(x[0])
    m = int(x[1])
    if(a%m == 0):
        print("Yes")
    elif(verify(a,m)):
        print("Yes")
    else:
        print("No")

main()