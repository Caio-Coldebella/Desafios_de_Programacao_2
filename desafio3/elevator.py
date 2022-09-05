def main():
    x = input().split()
    n = int(x[0])
    m = int(x[1])
    for i in range(n):
        x = input().split()
        start = int(x[0])
        finish = int(x[1])
        timeinit = int(x[2])
        if(start == finish):
            print(timeinit)
        elif(start < finish):
            trips = 0
            while(timeinit > 2*trips*(m-1) + start - 1):
                trips += 1
            timef = 2*trips*(m-1) + finish - 1
            print(timef)
        else:
            trips = 0
            while(timeinit > 2*(m-1)*(trips+1) - start + 1):
                trips += 1
            timef = 2*(m -1)*(trips + 1) + 1 - finish
            print(timef)

main()