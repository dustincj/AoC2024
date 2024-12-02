
def checkrow(array, count):
    inc = 0
    check = []
    while(inc < count):    
        if inc == count-1:
            dif = abs(array[inc]-array[inc-1])
            if   dif < 1 or dif >3:
                return 0
        else:
            if array[inc] <= array[inc+1]:
                check.append(1)
            else:
                check.append(0) 
            dif = abs(array[inc+1]-array[inc])

            if dif < 1 or dif >3:
                return 0
        inc = inc + 1

    ones = check.count(1)
    zeros = check.count(0)

    if zeros == 0 or ones == 0:
        return 1
    return 0

array = []

with open("input.txt", 'r') as f:
    for line in f.readlines():
        array.append([int(s) for s in line.strip().split(' ')])

safe = 0
rows = len(array)

count1 = 0
while(count1 < rows):
    columns = len(array[count1])
    tryremoveindex = 0
    if checkrow(array[count1], len(array[count1])) == 0:
        while tryremoveindex < columns:
            array1 = array[count1].copy()
            array1.pop(tryremoveindex)
            
            if checkrow(array1, len(array1)) == 1:
                safe = safe + 1
                break
            else:
                tryremoveindex = tryremoveindex + 1
    else:
        safe = safe + 1
    count1 = count1 + 1




print(safe)