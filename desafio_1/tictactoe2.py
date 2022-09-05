def entries():
    line1 = input()
    line2 = input()
    line3 = input()
    print(line1)
    arr = [line1,line2,line3,[line1[0],line2[0],line3[0]],[line1[1],line2[1],line3[1]],
    [line1[2],line2[2],line3[2]],[line1[0],line2[1],line3[2]],[line1[2],line2[1],line3[0]]]
    return arr

def count(arr):
    cross = 0
    zero = 0
    for i in range(3):
        for j in range(3):
            if(arr[i][j]=='x'):
                cross += 1
            elif(arr[i][j]=='0'):
                zero += 1
    return cross,zero

def illegal(arr):
    print(arr)
    cross,zero = count(arr)
    if(zero>cross):
        return True
    if((cross - 1)> zero):
        return True
    return False

def win(arr):
    for i in range(len(arr)):
        first = arr[i][0]
        for j in range(1,3):
            if(arr[i][j] != first):
                break
            if(j==2):
                if(first=='x' or first=='0'):
                    return first
    return "none"

def main():
    arr = entries()
    if(illegal(arr)):
        print("illegal")
        return 0
    result = win(arr)
    if(result=='x'):
        print("first")
        return 0
    if(result=='0'):
        print("second")
    

main()