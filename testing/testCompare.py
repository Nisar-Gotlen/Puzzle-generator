
import os
import sys
import inspect
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
            if name == filNameA:
                k += 1
                continue
            filName2.write(row)
        k += 1
        if k % n == 0:
            break
    return data


filNameTF = open('testing/TestFields.txt', 'r')
filNameA = open('testing/Answers.txt', 'r')
filName2 = open('testing/TestResults.txt', 'w')
k = 10
Nex = filNameTF.readline()
puzzle = [[0] * 9 for i in range(9)]
puzzleAnswers = [[0] * 9 for i in range(9)]
#module_name = 'solvingMethods'
#module = importlib.import_module(module_name)


for i in range(int(Nex)):
    res = FieldReading(filNameTF, k, puzzle)
    k = 10
    resAnswers = FieldReading(filNameA, k, puzzleAnswers)

    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

    from solvingMethods import SolvingMethods

    solving = SolvingMethods(res)
    puzzleSolved = solving.Solve()
  #  puzzleSolved = solvingMethods.Solve(res)

    for l in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzleSolved[l][j] != resAnswers[l][j]:
                filName2.write(str(puzzleSolved[l][j]) +
                               "/" + str(resAnswers[l][j]) + ' ')
            else:
                filName2.write(str(puzzleSolved[l][j]) + ' ')
        filName2.write("\n")
'''
    for row in puzzleSolved:
        for elem in row:
            filName2.write(str(elem) + ' ')
        filName2.write("\n")
'''
filNameTF.close()
filNameA.close()
filName2.close()
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
