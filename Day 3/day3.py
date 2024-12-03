import re


with open("input.txt", 'r') as file: 
        input = file.read()
        
#Part 1
match = re.findall(r"mul\([0-9]+,[0-9]+\)", input)

nums = []
for item in match:
      nums.append(re.findall(r"[0-9]+",item))

total = 0
for item in nums:
      item[0] = int(item[0])
      item[1] = int(item[1])
      total = total + item[0] * item[1]
print(total)


#Part 2
match = re.findall(r"don't\(\)|mul\([0-9]+,[0-9]+\)|do\(\)", input)
nums = []
add = True
for item in match:
     if item == "don't()":
          add = False
     elif item == "do()":
          add = True
     elif add == True: 
          nums.append(re.findall(r"[0-9]+",item))         
          
total = 0
for item in nums:
      item[0] = int(item[0])
      item[1] = int(item[1])
      total = total + item[0] * item[1]
print(total)
