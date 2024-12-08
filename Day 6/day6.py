import copy
def movementp1(row, col, count,pos):
    while True:
        if row == 0 or row == len(pos)-1 or col == 0 or col == len(pos)-1:
            count = count + 1
            return pos
        if pos[row][col] == "^":
            pos[row][col] = 'X'
            row, col, pos, count = up(row,col,count,pos)
        if pos[row][col] == "<":
            pos[row][col] = 'X'
            row, col, pos, count = left(row,col,count,pos)
        if pos[row][col] == ">":
            pos[row][col] = 'X'
            row, col, pos, count = right(row,col,count,pos)
        if pos[row][col] == "v":
            pos[row][col] = 'X'
            row, col, pos, count = down(row,col,count,pos)
            
def movementp2(row, col, count,newt):
    timer = 0
    while timer < 10000:
        if row == 0 or row == len(newt)-1 or col == 0 or col == len(newt)-1:
            count = count + 1
            print("here")
            return True
        if newt[row][col] == "^":
            newt[row][col] = 'X'
            row, col, newt, count = up(row,col,count,newt)
        if newt[row][col] == "<":
            newt[row][col] = 'X'
            row, col, newt, count = left(row,col,count,newt)
        if newt[row][col] == ">":
            newt[row][col] = 'X'
            row, col, newt, count = right(row,col,count,newt)
        if newt[row][col] == "v":
            newt[row][col] = 'X'
            row, col, newt, count = down(row,col,count,newt)
        timer += 1
    return False   
     

def up(row,col,count,pos):
    if pos[row-1][col] == '#':
        pos[row][col] = ">"
        return row, col, pos, count
    else:
        pos[row][col] = 'X'
        row = row - 1
        pos[row][col] = "^"
        return row, col, pos, count

def left(row,col,count,pos):
    if pos[row][col-1] == '#':
        pos[row][col] = "^"
        return row, col, pos, count
    else:
        pos[row][col] = 'X'
        col = col - 1
        pos[row][col] = "<"
        return row, col, pos, count

def right(row,col,count,pos):
    if pos[row][col+1] == '#':
        pos[row][col] = "v"
        return row, col, pos, count
    else:
        pos[row][col] = 'X'
        col = col + 1
        pos[row][col] = ">"
        return row, col, pos, count

def down(row,col,count,pos):
    if pos[row+1][col] == '#':
        pos[row][col] = "<"
        return row, col, pos, count
    else:
        pos[row][col] = 'X'
        row = row + 1
        pos[row][col] = "v"
        return row, col, pos, count



if __name__ == "__main__":
    input = []
    with open("input.txt", 'r') as file:
        for line in file.readlines():
            input.append([s for s in line.strip().split(' ')])

    fix = []

    for s in input:
        for i in s:
            fix.append(list(i))

    rowlen = len(fix)
    collen = len(fix[0])
    gcol = 0
    grow = 0
    i = 0
    while i < rowlen:
        x = 0
        while x < collen:
            if fix[i][x] == "^":
                gcol = x
                grow = i
                i = rowlen
                break
            x  = x + 1
        i = i + 1
    count = 0

    new = movementp1(grow,gcol,count,fix)
    for x in new:
        count = count + x.count("X")
    print(count+1)
    obs = []


    i= 0
    while i < rowlen:
        x = 0
        while x < collen:
            if fix[i][x] == ".":
                obs.append([i,x])
            x += 1
        i+=1
    newt = []
    newt = copy.deepcopy(fix)
    p = 0
    for n in obs:
        newt = copy.deepcopy(fix)
        newt[n[0]][n[1]] = "#"
        if not movementp2(grow,gcol,count,newt):
            p += 1
    print(p)
            
