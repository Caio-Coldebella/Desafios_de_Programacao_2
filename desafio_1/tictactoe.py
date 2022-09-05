def verify3(arr):
    nofx = 0
    nofb = 0
    for i in range(3):
        if(arr[i] == '.'):
            nofb += 1
        elif(arr[i] == 'x'):
            nofx += 1
    if((nofx == 2 and nofb == 1) or nofx == 3):
        return True
    return False
def verify4(arr):
    if(verify3(arr[:3])):
        return True
    if(verify3(arr[1:])):
        return True
    return False

def tictactoe():
    lines = []
    for i in range(4):
        lines.append(input())
    for i in range(4):
        if(verify4(lines[i])):
            return True
    columns = []
    for i in range(4):
        columns.append(str(lines[0][i])+str(lines[1][i])+str(lines[2][i])+str(lines[3][i]))
    for i in range(4):
        if(verify4(columns[i])):
            return True
    DIAG = [str(lines[0][0])+str(lines[1][1])+str(lines[2][2])+str(lines[3][3]),
    str(lines[3][0])+str(lines[2][1])+str(lines[1][2]+str(lines[0][3]))
    ,str(lines[1][0])+str(lines[2][1])+str(lines[3][2])
    ,str(lines[0][1])+str(lines[1][2])+str(lines[2][3])
    ,str(lines[2][0])+str(lines[1][1])+str(lines[0][2])
    ,str(lines[3][1])+str(lines[2][2])+str(lines[1][3])]
    if(verify4(DIAG[0]) or verify4(DIAG[1])):
        return True
    for i in range(2,6):
        if(verify3(DIAG[i])):
            return True
    return False
if(tictactoe()):
    print("YES")
else:
    print("NO")