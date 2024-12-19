from itertools import product, permutations

def domaths(maths, ans):
    ops = ['* ','+ ','|| ']
    for oper in product(ops,repeat=len(maths)-1):
        formula = " ".join(o+v for o,v in zip([""]+list(oper),maths))
        evals = eval(formula)
        if evals == int(ans):
            #print(eval(formula), "=",ans)
            return True
    return False

def eval(exp):
    permutation_split: list[str] = exp.split()
    result: str = permutation_split[0]
    for i in range(1, len(permutation_split), 2):
        if permutation_split[i] == "+":
            result = str(int(result) + int(permutation_split[i + 1]))
        elif permutation_split[i] == "*":
            result = str(int(result) * int(permutation_split[i + 1]))
        elif permutation_split[i] == "||":
            result = result + str(eval(permutation_split[i + 1]))

    return int(result)
    
    

            

if __name__ == "__main__":
    input = []
    with open("input.txt", 'r') as file:
        for line in file.readlines():
            
            input.append([s for s in line.strip().split(':')])

    for x in input:
        x[1] = [s for s in x[1].strip().split(' ')]
    tot = 0
    for i in input:
        if domaths(i[1],i[0]):
            tot = tot + int(i[0])

    print(tot)

