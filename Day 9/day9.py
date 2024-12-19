import copy
input = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        input.append([int(s) for s in line.strip()])

clean = input[0]

new = []
i=0
counter = 0
while i < len(clean):
    if i % 2 != 0 and i != 0:
        v = 0
        x = clean[i]
        while v < x:
            new.append('.')
            v+=1
    else:
        v = 0
        x = clean[i]
        while v < x: 
            new.append(str(counter))
            v+=1
        counter +=1
    i+=1

newp2 = copy.deepcopy(new)

y = len(new)-1
x = 0
while x < y:
    while new[x] == '.' and x < y:
        if new[y] != ".":
            new[x]= new[y]
            new[y] = '.'
        else:
            new.pop(y)
        y-=1
    x+=1


x=0
tot = 0
while x < len(new) :
    if new[x]=='.':
        break
    fetch =  x * int(new[x])
    tot = tot + fetch
    x += 1

print("p1 calc: " + str(tot))

groups = []
i = 0
while i < len(newp2):
    if newp2[i] != '.':
        # Start of a group of numbers
        start = i
        while i < len(newp2) and newp2[i] == newp2[start]:
            i += 1
        groups.append([int(newp2[start]),start, i - 1])  # Store the group as (start, end) indices
    else:
        i += 1
print(newp2)
freespace = []
i = 0
while i < len(newp2):
    if newp2[i] == '.':
        # Start of a group of spaces
        start = i
        while i < len(newp2) and newp2[i] == newp2[start]:
            i += 1
        freespace.append([start, i - 1])  # Store the group as (start, end) indices
    else:
        i += 1

i = len(groups)-1
while i >= 0:
    
    space_needed = groups[i][2]-groups[i][1]+1
    free = 0

    while free < len(freespace):
        if (freespace[free][1]-freespace[free][0]) >= space_needed-1 and freespace[free][0] <= groups[i][1]:
            add = freespace[free][0]
            occ = 0
            while add <= freespace[free][1] and occ < space_needed:
                newp2[add] = groups[i][0]
                add += 1
                occ+=1

            pop = groups[i][1]
            
            while pop <= groups[i][2]:
                newp2[pop] = "."
                pop+=1

            if freespace[free][1]-freespace[free][0] == space_needed-1:
                freespace.pop(free)
                
            else: 
                freespace[free][0] = freespace[free][0]+space_needed
            break
        free += 1

            
    
    i-=1
    # if i % 1000 == 0:
    #     print("still running")

print(newp2)
tot = 0
x = 0
while x < len(newp2) :
    if newp2[x]!='.':
        fetch =  x * int(newp2[x])
        tot = tot + fetch
    x += 1
print("p2 calc: " + str(tot))