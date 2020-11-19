import copy

totalNumber = 9

def prepareToPossibleValues(possibleValues):
    for i in range(totalNumber):
        for j in range(totalNumber):
            for k in range(2, totalNumber+1):
                possibleValues[i][j].add(k)

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
                    deleteExtraValues(puzzleSolving, possibleValues)
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
                    deleteExtraValues(puzzleSolving, possibleValues)
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
                    deleteExtraValues(puzzleSolving, possibleValues)
                    isSmthChange = True
    if not isSmthChange:
        continueSolving = False
    else:
        continueSolving = True

def missingNumbers(possibleValues, puzzleSolving): #name is taken from https://www.conceptispuzzles.com/ru/index.aspx?uri=puzzle/sudoku/techniques
    global continueSolving
    isSmhchanged = True
    while isSmhchanged:
        isSmhchanged = False
        for i in range(totalNumber):
            for j in range(totalNumber):
                if puzzleSolving[i][j] == 0:
                    if len(possibleValues[i][j]) == 1:
                        puzzleSolving[i][j] = possibleValues[i][j].pop()
                        deleteExtraValues(puzzleSolving, possibleValues)
                        isSmhchanged = True
    continueSolving = False

def nakedPair(possibleValues, puzzleSolving):
    for i in range(totalNumber): 
        candidateCount = {a: 0 for a in range(1,totalNumber+1)} #для строк
        for j in range(totalNumber):
            if len(possibleValues[i][j]) > 1:
                for num in possibleValues[i][j]:
                    candidateCount[num] += 1
        for j in range(totalNumber-1):
            if len(possibleValues[i][j]) > 1:
                matchingCells = {}
                matchingCells[j] = possibleValues[i][j]
                for nextCol in range(j+1,9):
                    if len(possibleValues[i][nextCol]) > 1:
                        if len(possibleValues[i][nextCol].difference(matchingCells[j])) == 0:
                            matchingCells[nextCol] = possibleValues[i][nextCol]
                if len(matchingCells[j]) == 2:
                    for k in matchingCells.keys():
                        if k == j:
                            continue
                        else:
                            for col in range(totalNumber):
                                if col != j and col != k:
                                    possibleValues[i][col].difference_update(matchingCells[j])                          
        candidateCount = {a: 0 for a in range(1,totalNumber+1)} #для столбцов
        for j in range(totalNumber):
            if len(possibleValues[j][i]) > 1:
                for num in possibleValues[j][i]:
                    candidateCount[num] += 1
        for j in range(totalNumber-1):
            if len(possibleValues[j][i]) > 1:
                matchingCells = {}
                matchingCells[j] = possibleValues[j][i]
                for nextRow in range(j+1,9):
                    if len(possibleValues[nextRow][i]) > 1:
                        if len(possibleValues[nextRow][i].difference(matchingCells[j])) == 0:
                            matchingCells[nextRow] = possibleValues[nextRow][i]
                if len(matchingCells[j]) == 2:
                    for k in matchingCells.keys():
                        if k == j:
                            continue
                        else:
                            for rw in range(totalNumber):
                                if rw != j and rw != k:
                                    possibleValues[rw][i].difference_update(matchingCells[j]) 
    for countBlock in range(totalNumber):
        candidateCount = {a: 0 for a in range(1,totalNumber+1)}
        fIndexRow = 3*(countBlock // 3)
        fIndexColumn = 3*(countBlock % 3)
        for i in range(3):
            for j in range(3):
                if len(possibleValues[fIndexRow+i][fIndexColumn+j]) > 1:
                    for num in possibleValues[fIndexRow+i][fIndexColumn+j]:
                        candidateCount[num] += 1
        for index in range(totalNumber):
            if len(possibleValues[fIndexRow + index // 3][fIndexColumn + index % 3]) > 1:
                matchingCells = {}
                matchingCells[index] = possibleValues[fIndexRow + index // 3][fIndexColumn + index % 3]
                for nextCell in range(index+1,9):
                    if len(possibleValues[fIndexRow+nextCell // 3][fIndexColumn+nextCell % 3]) > 1:
                        if len(possibleValues[fIndexRow+nextCell // 3][fIndexColumn+nextCell % 3].difference(matchingCells[index])) == 0:
                            matchingCells[nextCell] = possibleValues[fIndexRow+nextCell // 3][fIndexColumn+nextCell % 3]

def Solve(puzzleSolving):
    possibleValues = [[{1} for i in range(9)] for j in range(9)]
    prepareToPossibleValues( possibleValues) 
    deleteExtraValues(puzzleSolving, possibleValues)
    global continueSolving
    continueSolving = True
    while continueSolving:
        nakedPair(possibleValues, puzzleSolving)
        missingNumbers(possibleValues, puzzleSolving)
        singleCandidates(puzzleSolving, possibleValues)
    return puzzleSolving


puzzle = [
    [4, 0, 0, 0, 0, 0, 9, 3, 8],
    [0, 3, 2, 0, 9, 4, 1, 0, 0],
    [0, 9, 5, 3, 0, 0, 2, 4, 0],
    [3, 7, 0, 6, 0, 9, 0, 0, 4],
    [5, 2, 9, 0, 0, 1, 6, 7, 3],
    [6, 0, 4, 7, 0, 3, 0, 9, 0],
    [9, 5, 7, 0, 0, 8, 3, 0, 0],
    [0, 0, 3, 9, 0, 0, 4, 0, 0],
    [2, 4, 0, 0, 3, 0, 7, 0, 9]
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
