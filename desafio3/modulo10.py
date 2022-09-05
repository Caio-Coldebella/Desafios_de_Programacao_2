def operation(n):
    n += n%10
    return n

def operationmod2(n):
    if(n%10 == 0 or n%10 == 5):
        return n
    while(n%10 != 2):
        n += n%10
    return n

def arrayequal(arr):
    for i in range(len(arr)-1):
        if(arr[i] != arr[i+1]):
            return False
    return True

def arraytype2(arr):
    typemod = arr[0]%20
    for i in range(len(arr)):
        if(arr[i]%20 != typemod):
            return False
    return True

def modulo10(m,arr):
    group = 0
    if(arr[0]%10 == 0 or arr[0]%10 == 5):
        group = 1
    else:
        group = 2
    if(group == 1):
        for i in range(m):
            arr[i] = operation(arr[i])
        if(arrayequal(arr)):
            return "Yes"
        return "No"
    if(group == 2):
        for i in range(m):
            arr[i] = operationmod2(arr[i])
        if(arraytype2(arr)):
            return "Yes"
        return "No"    

def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        arr = [int(i) for i in input().split()]
        print(modulo10(m,arr))

main()