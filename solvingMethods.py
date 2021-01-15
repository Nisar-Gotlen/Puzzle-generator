class SolvingMethods(object):

    def __init__(self, startField):
        self.totalNumber = 9
        self.startField = startField
        self.numberField = self.prepareField()
        self.solvedField = [
            [0 for i in range(self.totalNumber)] for j in range(self.totalNumber)]
        self.done = False
        self.changes = False
        self.difficult = 0
        self.SingleCand = 0
        self.NakedPairs = 0
        self.NakedThree = 0
        self.HidPair = 0
        self.HidTree = 0
        self.solvingProcces()

    def isPossible(self):
        return self.done

    def Solve(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber):
                if len(self.numberField[i][j]) == 1:
                    for k in self.numberField[i][j]:
                        self.solvedField[i][j] = k
                else:
                    self.solvedField[i][j] = 0
        return self.solvedField

    def checksolving(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber):
                if len(self.numberField[i][j]) == 1:
                    self.done = True
                elif len(self.numberField[i][j]) > 1:
                    self.done = False
                    break
            if self.done == False:
                break
        if self.done:
            self.addSolution()
        return self.done

    def solvingProcces(self):
        while not self.done:
            self.deleteExtraValues()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.singleCandidates()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.nakedPairs()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.nakedTreesome()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.hiddenPiars()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.hiddenTriples()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            if not self.changes:
                break

    def addSolution(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber):
                for k in self.numberField[i][j]:
                    self.solvedField[i][j] = k

    def prepareField(self):
        numberField = [[{1} for i in range(self.totalNumber)]
                       for j in range(self.totalNumber)]
        for i in range(self.totalNumber):
            for j in range(self.totalNumber):
                if self.startField[i][j] != 0:
                    numberField[i][j].clear()
                    numberField[i][j].add(self.startField[i][j])
                    continue
                for k in range(2, self.totalNumber+1):
                    numberField[i][j].add(k)
        return numberField

    def deleteExtraValues(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber):
                if len(self.numberField[i][j]) == 1:
                    for k in self.numberField[i][j]:
                        num = k
                    for chv in range(self.totalNumber):
                        if not self.changes:
                            chCell1 = len(self.numberField[i][chv])
                            chCell2 = self.numberField[chv][j]
                        self.numberField[i][chv].discard(num)
                        self.numberField[chv][j].discard(num)
                        if not self.changes:
                            if chCell1 != len(self.numberField[i][chv]) or chCell2 != self.numberField[chv][j]:
                                self.changes = True
                    self.numberField[i][j].add(num)
                    firstIndexRow = 3*(i//3)
                    firstIndexColumn = 3*(j//3)
                    for chvr in range(3):
                        for chvc in range(3):
                            if not self.changes:
                                chCell = len(self.numberField[firstIndexRow + chvr][firstIndexColumn + chvc])
                            self.numberField[firstIndexRow + chvr][firstIndexColumn + chvc].discard(num)
                            if not self.changes:
                                if chCell != len(self.numberField[firstIndexRow + chvr][firstIndexColumn + chvc]):
                                    self.changes = True
                    self.numberField[i][j].add(num)

    # name is taken from https://www.conceptispuzzles.com/ru/index.aspx?uri=puzzle/sudoku/techniques
    def singleCandidates(self):
        for j in range(self.totalNumber):  # row
            for k in range(1, self.totalNumber+1):
                soughtNumber = k
                for i in range(self.totalNumber):
                    for cell in self.numberField[i][j]:
                        if cell == k:
                            soughtNumber = 0
                            break
                if soughtNumber != 0:
                    placeCount = 0
                    for i in range(self.totalNumber):
                        if placeCount == 2:
                            break
                        if soughtNumber in self.numberField[i][j]:
                            placeCount += 1
                            indexSoughtRow = i
                    if placeCount == 1:
                        self.numberField[indexSoughtRow][j].clear()
                        self.numberField[indexSoughtRow][j].add(soughtNumber)
                        self.deleteExtraValues()
                        self.changes = True
                        self.SingleCand += 1
        for i in range(self.totalNumber):  # column
            for k in range(1, self.totalNumber+1):
                soughtNumber = k
                for j in range(self.totalNumber):
                    for cell in self.numberField[i][j]:
                        if cell == k:
                            soughtNumber = 0
                            break
                if soughtNumber != 0:
                    placeCount = 0
                    for j in range(self.totalNumber):
                        if placeCount == 2:
                            break
                        if soughtNumber in self.numberField[i][j]:
                            placeCount += 1
                            indexSoughtColumn = j
                    if placeCount == 1:
                        self.numberField[i][indexSoughtColumn].clear()
                        self.numberField[i][indexSoughtColumn].add(
                            soughtNumber)
                        self.deleteExtraValues()
                        self.changes = True
                        self.SingleCand += 1
        for countBlock in range(self.totalNumber):  # block
            firstIndexRow = 3*(countBlock // 3)
            firstIndexColumn = 3*(countBlock % 3)
            for k in range(1, self.totalNumber+1):
                soughtNumber = k
                for i in range(3):
                    for j in range(3):
                        row = firstIndexRow+i
                        col = firstIndexColumn+j
                        for cell in self.numberField[row][col]:
                            if cell == k:
                                soughtNumber = 0
                                break
                if soughtNumber != 0:
                    placeCount = 0
                    for i in range(3):
                        for j in range(3):
                            row = firstIndexRow+i
                            col = firstIndexColumn+j
                            if placeCount == 2:
                                break
                            if soughtNumber in self.numberField[row][col]:
                                placeCount += 1
                                indexSoughtColumn = col
                                indexSoughtRow = row
                    if placeCount == 1:
                        self.numberField[indexSoughtRow][indexSoughtColumn].clear(
                        )
                        self.numberField[indexSoughtRow][indexSoughtColumn].add(
                            soughtNumber)
                        self.deleteExtraValues()
                        self.changes = True
                        self.SingleCand += 1

    def nakedPairs(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber-1):
                if len(self.numberField[i][j]) == 2:
                    matchingCells = {}
                    matchingCells[j] = self.numberField[i][j]
                    for nextCol in range(j+1, self.totalNumber):
                        if len(self.numberField[i][nextCol]) == 2 and self.numberField[i][nextCol] == self.numberField[i][j]:
                            matchingCells[nextCol] = self.numberField[i][nextCol]
                            for key in matchingCells.keys():
                                if key == j:
                                    continue
                            for col in range(self.totalNumber):
                                if col != j and col != nextCol:
                                    changesControl = len(
                                        self.numberField[i][col])
                                    self.numberField[i][col].difference_update(
                                        matchingCells[j])
                                    if len(self.numberField[i][col]) != changesControl:
                                        self.deleteExtraValues()
                                        self.changes = True
                                        self.NakedPairs += 1
                            break
                if len(self.numberField[j][i]) == 2:
                    matchingCells = {}
                    matchingCells[j] = self.numberField[j][i]
                    for nextRow in range(j+1, self.totalNumber):
                        if len(self.numberField[nextRow][i]) == 2 and self.numberField[nextRow][i] == self.numberField[j][i]:
                            matchingCells[nextRow] = self.numberField[nextRow][i]
                            for key in matchingCells.keys():
                                if key == j:
                                    continue
                                for row in range(self.totalNumber):
                                    if row != j and row != nextRow:
                                        changesControl = len(
                                            self.numberField[row][i])
                                        self.numberField[row][i].difference_update(
                                            matchingCells[j])
                                        if len(self.numberField[row][i]) != changesControl:
                                            self.deleteExtraValues()
                                            self.changes = True
                                            self.NakedPairs += 1
                            break
        for countBlock in range(self.totalNumber):
            fIndexRow = 3*(countBlock // 3)
            fIndexColumn = 3*(countBlock % 3)
            for index in range(self.totalNumber):
                if len(self.numberField[fIndexRow + (index // 3)][fIndexColumn + (index % 3)]) == 2:
                    matchingCells = {}
                    matchingCells[index] = self.numberField[fIndexRow +
                                                            (index // 3)][fIndexColumn + (index % 3)]
                    for nextCell in range(index+1, self.totalNumber):
                        if len(self.numberField[fIndexRow + (nextCell // 3)][fIndexColumn + (nextCell % 3)]) == 2 and len(self.numberField[fIndexRow+nextCell // 3][fIndexColumn+nextCell % 3].difference(matchingCells[index])) == 0:
                            matchingCells[nextCell] = self.numberField[fIndexRow +
                                                                       nextCell // 3][fIndexColumn+nextCell % 3]
                            for key in matchingCells.keys():
                                if key == index:
                                    continue
                                for cell in range(self.totalNumber):
                                    if cell != index and cell != nextCell:
                                        changesControl = len(
                                            self.numberField[fIndexRow+cell // 3][fIndexColumn+cell % 3])
                                        self.numberField[fIndexRow+cell // 3][fIndexColumn +
                                                                              cell % 3].difference_update(matchingCells[index])
                                        if len(self.numberField[fIndexRow+cell // 3][fIndexColumn+cell % 3]) != changesControl:
                                            self.deleteExtraValues()
                                            self.changes = True
                                            self.NakedPairs += 1
                            break

    def nakedTreesome(self):
        for i in range(self.totalNumber):
            count = 0
            for j in range(self.totalNumber):
                if len(self.numberField[i][j]) > 1:
                    count += 1
            if count > 3:
                for j in range(self.totalNumber-1):
                    if len(self.numberField[i][j]) == 3:
                        matchingCells = {}
                        matchingCells[j] = self.numberField[i][j]
                        for nextCol in range(j+1, self.totalNumber):
                            if self.numberField[i][nextCol].difference(self.numberField[i][j]) == 0:
                                matchingCells[j] = self.numberField[i][nextCol]
                        if len(matchingCells) == 3:
                            for col in range(self.totalNumber):
                                if not col in matchingCells.keys():
                                    controlChanges = self.numberField[i][col]
                                    self.numberField[i][col].difference_update(
                                        matchingCells[j])
                                    if self.numberField[i][col] != changesControl:
                                        self.deleteExtraValues()
                                        self.changes = True
                                        self.NakedThree += 1

    def hiddenPiars(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber-1):
                if len(self.numberField[i][j]) > 1:
                    matchingCells = {}
                    matchingCells[j] = self.numberField[i][j]
                    for nextCol in range(j+1, self.totalNumber):
                        intersect = self.numberField[i][j].intersection(
                            self.numberField[i][nextCol])
                        if len(intersect) == 2:
                            for chAllCol in range(self.totalNumber):
                                if chAllCol == nextCol or chAllCol == j:
                                    continue
                                if len(self.numberField[i][chAllCol].intersection(intersect)) > 0:
                                    intersect.clear()
                                    break
                        if len(intersect) == 2:
                            matchingCells[nextCol] = self.numberField[i][nextCol]
                    if len(matchingCells) == 2 and len(intersect) == 2:
                        for k in matchingCells.keys():
                            changesControl = len(self.numberField[i][k])
                            self.numberField[i][k].intersection_update(
                                intersect)
                            if len(self.numberField[i][k]) != changesControl:
                                self.deleteExtraValues()
                                self.changes = True
                                self.HidPair += 1
            for j in range(self.totalNumber-1):
                if len(self.numberField[j][i]) > 1:
                    matchingCells = {}
                    matchingCells[j] = self.numberField[j][i]
                    for nextRow in range(j+1, self.totalNumber):
                        intersect = self.numberField[j][i].intersection(
                            self.numberField[nextRow][i])
                        if len(intersect) == 2:
                            for chAllRow in range(self.totalNumber):
                                if chAllRow == nextRow or chAllRow == j:
                                    continue
                                if len(self.numberField[chAllRow][i].intersection(intersect)) > 0:
                                    intersect.clear()
                                    break
                        if len(intersect) == 2:
                            matchingCells[nextRow] = self.numberField[nextRow][i]
                    if len(matchingCells) == 2 and len(intersect) == 2:
                        for k in matchingCells.keys():
                            changesControl = len(self.numberField[k][i])
                            self.numberField[k][i].intersection_update(
                                intersect)
                            if len(self.numberField[k][i]) != changesControl:
                                self.deleteExtraValues()
                                self.changes = True
                                self.HidPair += 1
        for countBlock in range(self.totalNumber):
            fIndexRow = 3*(countBlock // 3)
            fIndexColumn = 3*(countBlock % 3)
            for index in range(self.totalNumber):
                if len(self.numberField[fIndexRow + (index // 3)][fIndexColumn + (index % 3)]) > 1:
                    matchingCells = {}
                    matchingCells[index] = self.numberField[fIndexRow +
                                                            (index // 3)][fIndexColumn + (index % 3)]
                    for nextCell in range(index+1, self.totalNumber):
                        intersect = self.numberField[fIndexRow + (index // 3)][fIndexColumn + (index % 3)].intersection(
                            self.numberField[fIndexRow + (nextCell // 3)][fIndexColumn + (nextCell % 3)])
                        if len(intersect) == 2:
                            for chAllCell in range(self.totalNumber):
                                if chAllCell == nextCell or chAllCell == index:
                                    continue
                                if len(self.numberField[fIndexRow + (chAllCell // 3)][fIndexColumn + (chAllCell % 3)].intersection(intersect)) > 0:
                                    intersect.clear()
                                    break
                        if len(intersect) == 2:
                            matchingCells[nextCell] = self.numberField[fIndexRow +
                                                                       (nextCell // 3)][fIndexColumn + (nextCell % 3)]
                    if len(matchingCells) == 2 and len(intersect) == 2:
                        for k in matchingCells.keys():
                            changesControl = len(
                                self.numberField[fIndexRow + (k // 3)][fIndexColumn + (k % 3)])
                            self.numberField[fIndexRow + (k // 3)][fIndexColumn + (
                                k % 3)].intersection_update(intersect)
                            if len(self.numberField[fIndexRow + (k // 3)][fIndexColumn + (k % 3)]) != changesControl:
                                self.deleteExtraValues()
                                self.changes = True
                                self.HidPair += 1

    def hiddenTriples(self):
        for i in range(self.totalNumber):
            for j in range(self.totalNumber-1):
                if len(self.numberField[i][j]) > 1:
                    for nextCol in range(j+1, self.totalNumber):
                        commonNums = self.numberField[i][j].intersection(
                            self.numberField[i][nextCol])
                        if len(commonNums) == 3:
                            matchingCells = {}
                            matchingCells[j] = self.numberField[i][j]
                            matchingCells[nextCol] = self.numberField[i][nextCol]
                            for chAllCol in range(self.totalNumber):
                                if chAllCol == nextCol or chAllCol == j:
                                    continue
                                if len(self.numberField[i][chAllCol].intersection(commonNums)) == 1:
                                    commonNums.clear()
                                    break
                                if len(self.numberField[i][chAllCol].intersection(commonNums)) == 2 or len(self.numberField[i][chAllCol].intersection(commonNums)) == 3:
                                    matchingCells[chAllCol] = self.numberField[i][chAllCol]
                            if len(matchingCells) == 3 and len(commonNums) != 0:
                                for k in matchingCells.keys():
                                    changesControl = len(
                                        self.numberField[i][k])
                                    self.numberField[i][k].intersection_update(
                                        commonNums)
                                    if len(self.numberField[i][k]) != changesControl:
                                        self.deleteExtraValues()
                                        self.changes = True
                                        self.HidTree += 1
        for j in range(self.totalNumber-1):
            if len(self.numberField[j][i]) > 1:
                for nextRow in range(j+1, self.totalNumber):
                    commonNums = self.numberField[j][i].intersection(
                        self.numberField[nextRow][i])
                    if len(commonNums) != 2 or len(commonNums) != 3:
                        continue
                    if len(commonNums) == 3:
                        matchingCells = {}
                        matchingCells[j] = self.numberField[j][i]
                        matchingCells[nextRow] = self.numberField[nextRow][i]
                        for chAllRows in range(self.totalNumber):
                            if chAllRows == nextRow or chAllRows == j:
                                continue
                            if len(self.numberField[chAllRows][i].intersection(commonNums)) == 1:
                                commonNums.clear()
                                break
                            if len(self.numberField[chAllRows][i].intersection(commonNums)) == 2 or len(self.numberField[chAllRows][i].intersection(commonNums)) == 3:
                                matchingCells[chAllRows] = self.numberField[chAllRows][i]
                        if len(matchingCells) == 3 and len(commonNums) != 0:
                            for k in matchingCells.keys():
                                changesControl = len(self.numberField[k][i])
                                self.numberField[k][i].intersection_update(
                                    commonNums)
                                if len(self.numberField[k][i]) != changesControl:
                                    self.deleteExtraValues()
                                    self.changes = True
                                    self.HidTree += 1
        for countBlock in range(self.totalNumber):
            fIndexRow = 3*(countBlock // 3)
            fIndexColumn = 3*(countBlock % 3)
            for index in range(self.totalNumber):
                for nextCell in range(index+1, self.totalNumber):
                    commonNums = self.numberField[fIndexRow + (index // 3)][fIndexColumn + (index % 3)].intersection(
                        self.numberField[fIndexRow + (nextCell // 3)][fIndexColumn + (nextCell % 3)])
                    if len(commonNums) != 2 or len(commonNums) != 3:
                        continue
                    if len(commonNums) == 3:
                        matchingCells = {}
                        matchingCells[index] = self.numberField[fIndexRow +
                                                                (index // 3)][fIndexColumn + (index % 3)]
                        matchingCells[nextCell] = self.numberField[fIndexRow +
                                                                   (nextCell // 3)][fIndexColumn + (nextCell % 3)]
                        for nextCell in range(index+1, self.totalNumber):
                            if chAllCell == nextCell or chAllCell == index:
                                continue
