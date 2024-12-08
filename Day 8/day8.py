import math
from itertools import product, combinations


def getantinodesp1(antennas, rows,cols):
    antinodes = set()
    for freq, positions in antennas.items():
        for (r1, c1), (r2, c2) in combinations(positions, 2):
            dr = r2 - r1
            dc = c2 - c1
            
            if 0 <= r1 - dr < rows and 0 <= c1 - dc < cols:
                antinodes.add((r1 - dr, c1 - dc))
            if 0 <= r2 + dr < rows and 0 <= c2 + dc < cols:
                antinodes.add((r2 + dr, c2 + dc))
        
            if 0 <= r1 - dr < rows and 0 <= c1 - dc < cols:
                antinodes.add((r1 - dr, c1 - dc))
            if 0 <= r2 + dr < rows and 0 <= c2 + dc < cols:
                antinodes.add((r2 + dr, c2 + dc))


    # print(antinodes)
    return antinodes

def getantinodesp2(antennas, rows,cols):
    antinodes = set()
    for freq, positions in antennas.items():
        if len(positions)>1:
            for x in positions:
                antinodes.add((x[0],x[1]))
        for (r1, c1), (r2, c2) in combinations(positions, 2):     
            x = 1
            while True:
                dr = x*(r2 - r1)
                dc = x*(c2 - c1)
                if 0 <= r1 - dr < rows and 0 <= c1 - dc < cols:
                    antinodes.add((r1 - dr, c1 - dc))
                if 0 <= r2 + dr < rows and 0 <= c2 + dc < cols:
                    antinodes.add((r2 + dr, c2 + dc))
            
                if 0 <= r1 - dr < rows and 0 <= c1 - dc < cols:
                    antinodes.add((r1 - dr, c1 - dc))
                if 0 <= r2 + dr < rows and 0 <= c2 + dc < cols:
                    antinodes.add((r2 + dr, c2 + dc))
                if dr > rows or dc > rows:
                    break
                x += 1
    return antinodes



if __name__ == "__main__":
    
    input = []
    with open("input.txt", 'r') as file:
        for line in file.readlines():
            input.append(line.strip())
    lenrow = len(input)
    lencol = len(input[0])
    antennas = {}
    for r in range(lenrow):
        for c in range(lencol):
            char = input[r][c]
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    locations = getantinodesp1(antennas,lenrow,lencol)
    print("Antinodes for p1 = " + str(len(locations)))

    locations = getantinodesp2(antennas,lenrow,lencol)
    print("Antinodes for p2 = " + str(len(locations)))
