def main():
    x = input().split()
    n = int(x[0])
    a = int(x[1])
    b = int(x[2])
    percnt = b/a
    arr = [int(i) for i in input().split()]
    first = arr[0]
    vazao = first
    holes = sorted(arr[1:])
    for i in range(len(holes)):
        vazao += holes[i]
    i = n-2
    nholes = 0
    while((first/vazao) < percnt):
        vazao -= holes[i]
        i -= 1
        nholes += 1
    print(nholes)

main()