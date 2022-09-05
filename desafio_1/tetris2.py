def verify(arr,parity):
    if(len(arr)>1):
        for i in range(len(arr)):
            if(arr[i]%2 != parity):
                return False
    return True

def main():
    ncases = int(input())
    for i in range(ncases):
        ncol = int(input())
        arr = [int(i) for i in input().split()]
        parity = arr[0]%2
        if(verify(arr,parity)):
            print("YES")
        else:
            print("NO")
                  
main()