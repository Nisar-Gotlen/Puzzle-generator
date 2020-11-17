import copy

totalNumber = 9

def prepareToPossibleValues(possibleValues):
    for i in range(totalNumber):
        for j in range(totalNumber):
            for k in range(1, totalNumber+1):
                possibleValues[i][j].add(k)
    return possibleValues

def deleteExtraValues(puzzleSolving, possibleValues):
    for i in range(totalNumber):
        for j in range(totalNumber):
            if puzzleSolving[i][j] != 0:
                possibleValues[i][j].clear()
                for chv in range(totalNumber):
                        possibleValues[i][chv].discard(puzzleSolving[i][j])
                        possibleValues[chv][j].discard(puzzleSolving[i][j])
                firstIndexRow = 3*(i//3) 
                firstIndexColumn = 3*(j//3)
                for chvr in range(3):
                    for chvc in range(3):
                            possibleValues[firstIndexRow+chvr][firstIndexColumn +
                                                               chvc].discard(puzzleSolving[i][j])
    return possibleValues


def singleCandidates(puzzleSolving, possibleValues): #name is taken from https://www.conceptispuzzles.com/ru/index.aspx?uri=puzzle/sudoku/techniques
    global continueSolving
    isSmthChange = False
    for j in range(totalNumber):
        for k in range(1, totalNumber+1):
            soughtNumber = k
            for i in range(totalNumber):
                if puzzleSolving[i][j] == k:
                    soughtNumber = 0
            if soughtNumber != 0:
                placeCount = 0
                for i in range(totalNumber):
                    if placeCount < 2:
                        if soughtNumber in possibleValues[i][j]:
                            placeCount += 1
                            indexSoughtRow = i
                    else: 
                        break
                if placeCount == 1:
                    puzzleSolving[indexSoughtRow][j] = k
                    possibleValues = deleteExtraValues(puzzleSolving, possibleValues)
                    isSmthChange = True
    for i in range(totalNumber):
        for k in range(1, totalNumber+1):
            soughtNumber = k
            for j in range(totalNumber):
                if puzzleSolving[i][j] == k:
                    soughtNumber = 0
            if soughtNumber != 0:
                placeCount = 0
                for j in range(totalNumber):
                    if placeCount < 2:
                        if soughtNumber in possibleValues[i][j]:
                            placeCount += 1
                            indexSoughtColumn = j
                    else: 
                        break
                if placeCount == 1:
                    puzzleSolving[i][indexSoughtColumn] = k
                    possibleValues = deleteExtraValues(puzzleSolving, possibleValues)
                    isSmthChange = True

    for countBlock in range(totalNumber):
        firstIndexRow = 3*(countBlock // 3)
        firstIndexColumn = 3*(countBlock % 3)
        for k in range(1, totalNumber+1):
            soughtNumber = k
            for i in range(3):
                for j in range(3):
                    row = firstIndexRow+i
                    col = firstIndexColumn+j
                    if puzzleSolving[row][col] == k:
                        soughtNumber = 0
            if soughtNumber != 0:
                placeCount = 0
                for i in range(3):
                    for j in range(3):
                        row = firstIndexRow+i
                        col = firstIndexColumn+j
                        if placeCount < 2:
                            if soughtNumber in possibleValues[row][col]:
                                placeCount += 1
                                indexSoughtColumn = row
                                indexSoughtRow = col
                        else: 
                            break
                if placeCount == 1:
                    puzzleSolving[indexSoughtColumn][indexSoughtRow] = soughtNumber
                    possibleValues = deleteExtraValues(puzzleSolving, possibleValues)
                    isSmthChange = True
    if not isSmthChange:
        continueSolving = False
    else:
        continueSolving = True
    return puzzleSolving


def missingNumbers(possibleValues, puzzleSolving): #name is taken from https://www.conceptispuzzles.com/ru/index.aspx?uri=puzzle/sudoku/techniques
    global continueSolving
    isSmhchanged = True
    while isSmhchanged:
        isSmhchanged = False
        for i in range(totalNumber):
            for j in range(totalNumber):
                if puzzleSolving[i][j] == 0:
                    if len(possibleValues[i][j]) == 1:
                        puzzleSolving[i][j] = possibleValues[i][j][0]
                        possibleValues = deleteExtraValues(puzzleSolving, possibleValues)
                        isSmhchanged = True
    continueSolving = False
    return puzzleSolving

def nakedPairs(possibleValues, puzzleSolving):

    return puzzleSolving


def Solve(puzzleSolving):
    possibleValues = [[{0} for i in range(9)] for j in range(9)]
    possibleValues = prepareToPossibleValues( possibleValues) 
    possibleValues = deleteExtraValues(puzzleSolving, possibleValues)
    global continueSolving
    continueSolving = True
    while continueSolving:
        puzzleSolving = missingNumbers(possibleValues, puzzleSolving)
        puzzleSolving = singleCandidates(puzzleSolving, possibleValues)
    return puzzleSolving


puzzle = [
    [0, 0, 5, 1, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 7],
    [0, 1, 0, 0, 0, 4, 3, 0, 2],
    [0, 8, 0, 0, 0, 0, 0, 6, 4],
    [0, 0, 0, 0, 0, 0, 2, 3, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 9, 0, 0, 0],
    [4, 7, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 3, 0, 0, 0, 9, 2, 0]
]


puzzleSolving = copy.deepcopy(puzzle)
puzzleSolving = Solve(puzzleSolving)

'''
puzzle = [
    [0, 0, 5, 1, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 7],
    [0, 1, 0, 0, 0, 4, 3, 0, 2],
    [0, 8, 0, 0, 0, 0, 0, 6, 4],
    [0, 0, 0, 0, 0, 0, 2, 3, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 9, 0, 0, 0],
    [4, 7, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 3, 0, 0, 0, 9, 2, 0]
]


puzzleSolving = copy.deepcopy(puzzle)
puzzleSolving = Solve(puzzleSolving)
'''
