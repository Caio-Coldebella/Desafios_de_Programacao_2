def main():
    x = [int(i) for i in input().split()]
    nel = x[0]
    leng = x[1]
    arr = [int(i) for i in input().split()]
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    sum = sum + len(arr) - 1
    if((sum == leng) and (len(arr) == nel)):
        print("YES")
    else:
        print("NO")

main()