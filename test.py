
#from pole1 import Solve
import importlib


def FieldReading(name, k, puz):
    data = []
    n = k

    for row in name:
        if row[0].isdigit():
            cols = list(map(int, row.split()))
            data.append(cols)
            puz[k-11] = cols
        else:
            if name == filA:
                k += 1
                continue
            fil2.write(row)
        k += 1
        if k % n == 0:
            break
    return data


fil = open('testing/TestFields.txt', 'r')
filA = open('testing/Answers.txt', 'r')
fil2 = open('testing/TestResults.txt', 'w')
k = 10
Nex = fil.readline()
puzzle = [[0] * 9 for i in range(9)]
puzzleAnswers = [[0] * 9 for i in range(9)]
module_name = 'solvingMethods'
module = importlib.import_module(module_name)


for i in range(int(Nex)):
    res = FieldReading(fil, k, puzzle)
    k = 10
    resAnswers = FieldReading(filA, k, puzzleAnswers)
    puzzleSolved = module.Solve(res)

    for l in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzleSolved[l][j] != resAnswers[l][j]:
                fil2.write(str(puzzleSolved[l][j]) +
                           "/" + str(resAnswers[l][j]) + ' ')
            else:
                fil2.write(str(puzzleSolved[l][j]) + ' ')
        fil2.write("\n")
'''
    for row in puzzleSolved:
        for elem in row:
            fil2.write(str(elem) + ' ')
        fil2.write("\n")
'''
fil.close
filA.close
fil2.close
#'Testing/TestFields.txt', 'r'
'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''
