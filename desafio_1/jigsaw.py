def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def main():
    fstline = input().split()
    students = int(fstline[0])
    puzzles = int(fstline[1])
    nparts = [int(i) for i in input().split()]
    nparts = insertion_sort(nparts)
    diff = 1000000
    if(puzzles == students):
        diff = nparts[len(nparts)-1] - nparts[0]
    for i in range(puzzles - students + 1):
        selected = []
        for j in range(i,i+students):
            selected.append(nparts[j])
        if((selected[len(selected)-1]-selected[0])<diff):
            diff = selected[len(selected)-1] - selected[0]
    print(diff)
main()