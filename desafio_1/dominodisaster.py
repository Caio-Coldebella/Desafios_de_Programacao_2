def main():
    n = int(input())
    for i in range(n):
        width = int(input())
        row = input()
        other = []
        for j in range (len(row)):
            x = row[j]
            if(x=='U'):
                other.append('D')
            elif(x=='D'):
                other.append('U')
            else:
                other.append(x)
        other = ''.join(other)
        print(other)
main()