import re
array=[]


def part1():
    with open("input.txt", 'r') as file: 
        input = file.read()
        array.append(input.splitlines())
    new = []
    count = 0
    match = re.findall(r"XMAS", input)
    count = len(match)
    match = re.findall(r"SAMX", input)
    count = count+ len(match)


    for x in array:
            for i in x:
                new.append(list(i))

    max_col = len(new[0])
    max_row = len(new)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(new[y][x])
            rows[y].append(new[y][x])
            fdiag[x+y].append(new[y][x])
            bdiag[x-y-min_bdiag].append(new[y][x])

    diagtextf=[]
    diagtextb=[]

    for i in bdiag:
        diagtextf.append("".join(i))
    for i in fdiag:
        diagtextb.append("".join(i))

    for x in diagtextf:
        match = re.findall(r"XMAS", x)
        count = count + len(match)
        match = re.findall(r"SAMX", x)
        count = count + len(match)

    for x in diagtextb:
        match = re.findall(r"XMAS", x)
        count = count + len(match)
        match = re.findall(r"SAMX", x)
        count = count + len(match)

    vert = list(zip(*reversed(new)))
    vertt = []

    for i in vert:
        vertt.append("".join(i))
    for x in vertt:
        match = re.findall(r"XMAS", x)
        count = count + len(match)
        match = re.findall(r"SAMX", x)
        count = count + len(match)

    print(count)

def part2():

    with open("input.txt", 'r') as file: 
        input = file.read()
        array.append(input.splitlines())

    new = []
    count = 0

    for x in array:
            for i in x:
                new.append(list(i))

    size = len(new[0])
    x = 1
    while x <  size-1:
        y=1
        while y < size-1:
            if new[x][y] == 'A':
                    if new[x-1][y-1] == 'S' or new[x-1][y-1] == 'M':
                            if (new[x+1][y+1] == 'S' or new[x+1][y+1] == 'M') and new[x-1][y-1] != new[x+1][y+1]:
                                if new[x-1][y+1] == 'S' or new[x-1][y+1] == 'M':
                                    if (new[x+1][y-1] == 'S' or new[x+1][y-1] == 'M') and new[x+1][y-1] != new[x-1][y+1]:
                                            count = count + 1
            y = y + 1
        x=x+1

    print(count)

if __name__ == "__main__":
    part1()
    part2()