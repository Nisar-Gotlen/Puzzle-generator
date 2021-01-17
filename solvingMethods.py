class SolvingMethod(object):

    def __init__(self, startField):
        self.totalNumber = 9
        self.startField = startField
        self.numberField = self.prepareField()
        self.solvedField = [[0 for i in range(self.totalNumber)] for j in range(self.totalNumber)]
        self.done = False
        self.changes = False
        self.difficult = 0
        self.SingleCand = 0
        self.NakedPairs = 0
        self.NakedThree = 0
        self.HidPair = 0
        self.HidTree = 0
        self.SingleCandControl = 0
        self.NakedPairsControl = 0
        self.NakedThreeControl = 0
        self.HidPairControl = 0
        self.HidTreeControl = 0
        self.DeleteExtraVal = 0

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
                            chCell2 = len(self.numberField[chv][j])
                        self.numberField[i][chv].discard(num)
                        self.numberField[chv][j].discard(num)
                        self.numberField[i][j].add(num)
                        if not self.changes:
                            if chCell1 != len(self.numberField[i][chv]) or chCell2 != len(self.numberField[chv][j]):
                                self.DeleteExtraVal +=1
                                self.changes = True
                    self.numberField[i][j].add(num)
                    firstIndexRow = 3*(i//3)
                    firstIndexColumn = 3*(j//3)
                    for chvr in range(3):
                        for chvc in range(3):
                            if not self.changes:
                                chCell = len(self.numberField[firstIndexRow + chvr][firstIndexColumn + chvc])
                            self.numberField[firstIndexRow + chvr][firstIndexColumn + chvc].discard(num)
                            self.numberField[i][j].add(num)
                            if not self.changes:
                                if chCell != len(self.numberField[firstIndexRow + chvr][firstIndexColumn + chvc]):
                                    self.DeleteExtraVal +=1
                                    self.changes = True

    # name is taken from https://www.conceptispuzzles.com/ru/index.aspx?uri=puzzle/sudoku/techniques
    def singleCandidates(self):
        self.SingleCandControl +=1
        for j in range(self.totalNumber):  # row
            for k in range(1, self.totalNumber+1):
                soughtNumber = k
                for i in range(self.totalNumber):
                    if len(self.numberField[i][j]) == 1:
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
                        self.deleteExtraValues()
                        self.numberField[indexSoughtRow][j].clear()
                        self.numberField[indexSoughtRow][j].add(soughtNumber)
                        self.deleteExtraValues()
                        self.changes = True
                        self.changes = True
        for i in range(self.totalNumber):  # column
            for k in range(1, self.totalNumber+1):
                soughtNumber = k
                for j in range(self.totalNumber):
                    if len(self.numberField[i][j]) == 1:
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
                        if len(self.numberField[row][col]) == 1:
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
                        self.numberField[indexSoughtRow][indexSoughtColumn].clear()
                        self.numberField[indexSoughtRow][indexSoughtColumn].add(
                            soughtNumber)
                        self.deleteExtraValues()
                        self.changes = True
                        self.SingleCand += 1
    

    def nakedPairs(self):
        self.NakedPairsControl +=1
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
        self.NakedThreeControl +=1
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
        self.HidPairControl +=1
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
        self.HidTreeControl += 1
        for i in range(self.totalNumber):
            indexSaver = {}
            for k in range(1,self.totalNumber+1):
                for j in range(self.totalNumber):
                    if len(self.numberField[i][j]) >1:
                        if k in self.numberField[i][j]:
                            if indexSaver.get(k) == None:
                                indexSaver[k] = []
                            indexSaver[k].append([i,j])
            compareInd = []
            if len(indexSaver) >= 3:
                rememberDel = []
                keysInd = []
                commonNums = []
                finded = False
                for k in indexSaver.keys():
                    keysInd.append(k)
                    if len(indexSaver[k]) > 3 and len(indexSaver[k]) == 1:
                        if k not in rememberDel:
                            rememberDel.append(k)
                for k1 in range(len(keysInd)):
                    if not finded and len(indexSaver[keysInd[k1]]) < 4 and len(indexSaver[k]) != 1:
                        compareInd = indexSaver[keysInd[k1]]
                        for k2 in range(k1+1, len(keysInd)):
                            marker = True
                            for c in indexSaver[keysInd[k2]]:
                                if c in compareInd:
                                    continue
                                marker = False
                            if marker:
                                for k3 in range(k2+1,len(keysInd)):
                                    marker2 = True
                                    for c in indexSaver[keysInd[k3]]:
                                        if c in compareInd:
                                            finded = True
                                        else:
                                            finded = False
                                            break
                                    if finded:
                                        commonNums.append(keysInd[k3])
                                        break
                                if finded:
                                    commonNums.append(keysInd[k2])
                                    break
                        if finded:
                            commonNums.append(keysInd[k1])
                            continue
                        else: 
                            if keysInd[k1] not in rememberDel:
                                rememberDel.append(keysInd[k1])
                    else: 
                        if keysInd[k1] not in rememberDel and keysInd[k1] not in commonNums:
                            rememberDel.append(keysInd[k1])
                if len(rememberDel) != 0:
                    for c in rememberDel:
                        indexSaver.pop(c)
            if len(compareInd) == 3 and len(indexSaver) == 3:
                for k in indexSaver.keys():
                    commonNums.append(k)
                for c in compareInd:
                    changesControl = len(self.numberField[c[0]][c[1]])
                    self.numberField[c[0]][c[1]].intersection_update(commonNums)
                    if len(self.numberField[c[0]][c[1]]) != changesControl:
                        self.deleteExtraValues()
                        self.changes = True
                        self.HidTree += 1
            indexSaver = {}
            for k in range(1,self.totalNumber+1):
                for j in range(self.totalNumber):
                    if len(self.numberField[j][i]) >1:
                        if k in self.numberField[j][i]:
                            if indexSaver.get(k) == None:
                                indexSaver[k] = []
                            indexSaver[k].append([j,i])
            compareInd = []
            if len(indexSaver) >= 3:
                rememberDel = []
                keysInd = []
                commonNums = []
                finded = False
                for k in indexSaver.keys():
                    keysInd.append(k)
                    if len(indexSaver[k]) > 3 or len(indexSaver[k]) ==1:
                        if k not in rememberDel:
                            rememberDel.append(k)
                for k1 in range(len(keysInd)):
                    if not finded and len(indexSaver[keysInd[k1]]) < 4 and len(indexSaver[k]) != 1:
                        compareInd = indexSaver[keysInd[k1]]
                        for k2 in range(k1+1, len(keysInd)):
                            marker = True
                            for c in indexSaver[keysInd[k2]]:
                                if c in compareInd:
                                    continue
                                marker = False
                            if marker:
                                for k3 in range(k2+1,len(keysInd)):
                                    marker2 = True
                                    for c in indexSaver[keysInd[k3]]:
                                        if c in compareInd:
                                            finded = True
                                        else:
                                            finded = False
                                            break
                                    if finded:
                                        commonNums.append(keysInd[k3])
                                        break
                                if finded:
                                    commonNums.append(keysInd[k2])
                                    break
                        if finded:
                            commonNums.append(keysInd[k1])
                            continue
                        else: 
                            if keysInd[k1] not in rememberDel:
                                rememberDel.append(keysInd[k1])
                    else: 
                            if keysInd[k1] not in rememberDel and keysInd[k1] not in commonNums:
                                rememberDel.append(keysInd[k1])
                if len(rememberDel) != 0:
                    for c in rememberDel:
                        indexSaver.pop(c)
            if len(compareInd) == 3 and len(indexSaver) == 3:
                for c in compareInd:
                    changesControl = len(self.numberField[c[0]][c[1]])
                    self.numberField[c[0]][c[1]].intersection_update(commonNums)
                    if len(self.numberField[c[0]][c[1]]) != changesControl:
                        self.deleteExtraValues()
                        self.changes = True
                        self.HidTree += 1
        for countBlock in range(self.totalNumber):
            fIndexRow = 3*(countBlock // 3)
            fIndexColumn = 3*(countBlock % 3)
            indexSaver = {}
            for k in range(1, self.totalNumber+1):
                for index in range(self.totalNumber):
                    if len(self.numberField[fIndexRow + (index // 3)][fIndexColumn + (index % 3)]) >1:
                        if k in self.numberField[fIndexRow + (index // 3)][fIndexColumn + (index % 3)]:
                            if indexSaver.get(k) == None:
                                indexSaver[k] = []
                            indexSaver[k].append([fIndexRow + (index // 3),fIndexColumn + (index % 3)])
            compareInd = []
            if len(indexSaver) >= 3:
                rememberDel = []
                keysInd = []
                commonNums = []
                finded = False
                for k in indexSaver.keys():
                    keysInd.append(k)
                    if len(indexSaver[k]) > 3 and len(indexSaver[k]) == 1:
                        if k not in rememberDel:
                            rememberDel.append(k)
                for k1 in range(len(keysInd)):
                    if not finded and len(indexSaver[keysInd[k1]]) < 4 and len(indexSaver[k]) != 1:
                        compareInd = indexSaver[keysInd[k1]]
                        for k2 in range(k1+1, len(keysInd)):
                            marker = True
                            for c in indexSaver[keysInd[k2]]:
                                if c in compareInd:
                                    continue
                                marker = False
                            if marker:
                                for k3 in range(k2+1,len(keysInd)):
                                    marker2 = True
                                    for c in indexSaver[keysInd[k3]]:
                                        if c in compareInd:
                                            finded = True
                                        else:
                                            finded = False
                                            break
                                    if finded:
                                        commonNums.append(keysInd[k3])
                                        break
                                if finded:
                                    commonNums.append(keysInd[k2])
                                    break
                        if finded:
                            commonNums.append(keysInd[k1])
                            continue
                        else: 
                            if keysInd[k1] not in rememberDel:
                                rememberDel.append(keysInd[k1])
                    else: 
                        if keysInd[k1] not in rememberDel and keysInd[k1] not in commonNums:
                            rememberDel.append(keysInd[k1])
                if len(rememberDel) != 0:
                    for c in rememberDel:
                        indexSaver.pop(c)
            if len(indexSaver) == 3 and len(compareInd) == 3:
                for k in indexSaver.keys():
                    commonNums.append(k)
                for c in compareInd:
                    changesControl = len(self.numberField[c[0]][c[1]])
                    self.numberField[c[0]][c[1]].intersection_update(commonNums)
                    if len(self.numberField[c[0]][c[1]]) != changesControl:
                        self.deleteExtraValues()
                        self.changes = True
                        self.HidTree += 1

class SolvingMethods(SolvingMethod):
    def __init__(self, startField):
        SolvingMethod.__init__(self, startField)
        self.solvingProcces()

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


class SolvingMethodsKiller(SolvingMethod):
    def __init__(self, startField, killerBox, countKillBox, areaSum):
        SolvingMethod.__init__(self, startField)
        self.killerBox = killerBox
        self.countKillBox = countKillBox
        self.areaSum = areaSum
        self.missingNumsCount = 0
        self.uniqAmCount  = 0
        self.balancerCount = 0
        self.solvingProcces()

    def solvingProcces(self):
        while not self.done:
            self.countMissingNums()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.deleteExtraValues()
            if self.checksolving():
                break
            if self.changes:
                self.changes = False
                continue
            self.uniqAmounts()
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

    def countMissingNums(self):
        for num in range(1, self.countKillBox):
            controlSum = self.areaSum[num]
            emptyCell = 0
            for i in range(self.totalNumber):
                for j in range(self.totalNumber):
                    if self.killerBox[i][j] == num:
                        if len(self.numberField[i][j]) == 1:
                            for k in self.numberField[i][j]:
                                controlSum -= k
                        else:
                            emptyCell +=1
            if emptyCell == 1 and controlSum > 0:
                for i in range(self.totalNumber):
                    for j in range(self.totalNumber):
                        if self.killerBox[i][j] == num:
                            if len(self.numberField[i][j]) != 1:
                                self.numberField[i][j].clear()
                                self.numberField[i][j].add(controlSum)
                                self.changes = True
                                self.missingNumsCount +=1
                                break
                        if self.changes:
                            break

    def uniqAmounts(self):
        for num in range(1, self.countKillBox):
            indexCell = []
            countcells = 0
            controlSum = self.areaSum[num]
            for i in range(self.totalNumber):
                for j in range(self.totalNumber):
                    if killerBox[i][j] == num:
                        if len(self.numberField[i][j]) == 1:
                            for k in self.numberField[i][j]:
                                controlSum -= k
                        else:
                            list = [i,j]
                            indexCell.append(list)
                            countcells +=1
            allowAddition = int(controlSum - (((countcells + 1) * countcells) / 2))
            if allowAddition >= 0 and controlSum != 0:
                allowedNum = allowAddition + countcells
                if allowedNum < self.totalNumber:
                    for k in range(allowedNum+1,self.totalNumber+1):
                        for counter in range(countcells):
                            changesControl = len(self.numberField[indexCell[counter][0]][indexCell[counter][1]])
                            self.numberField[indexCell[counter][0]][indexCell[counter][1]].discard(k)
                            if len(self.numberField[indexCell[counter][0]][indexCell[counter][1]]) != changesControl:
                                self.changes = True
                                self.uniqAmCount +=1
                            if (controlSum % 2) == 0 and countcells ==2:
                                delNum = int(controlSum / 2)
                                changesControl = len(self.numberField[indexCell[counter][0]][indexCell[counter][1]])
                                self.numberField[indexCell[counter][0]][indexCell[counter][1]].discard(delNum)
                                if len(self.numberField[indexCell[counter][0]][indexCell[counter][1]]) != changesControl:
                                    self.changes = True
                                    self.uniqAmCount +=1
                            if allowAddition == 1:
                                delNum = countcells
                                changesControl = len(self.numberField[indexCell[counter][0]][indexCell[counter][1]])
                                self.numberField[indexCell[counter][0]][indexCell[counter][1]].discard(delNum)
                                if len(self.numberField[indexCell[counter][0]][indexCell[counter][1]]) != changesControl:
                                    self.changes = True
                                    self.uniqAmCount +=1
            #балансер
            self.balancer(controlSum, num, indexCell)

    def balancer(self, controlSum, numOfCell, indexCell):
        countcells = len(indexCell)
        allowAddition = int(controlSum - (((countcells + 1) * countcells) / 2))
        allowedNum = allowAddition + countcells
        if countcells == 2:
            iterationSet = set()
            for k in self.numberField[indexCell[0][0]][indexCell[0][1]]:
                iterationSet.add(k)
            for possibleNum in iterationSet:
                if (controlSum - possibleNum) not in self.numberField[indexCell[1][0]][indexCell[1][1]]:
                    self.numberField[indexCell[0][0]][indexCell[0][1]].discard(possibleNum)
            iterationSet.clear()
            for k in self.numberField[indexCell[1][0]][indexCell[1][1]]:
                iterationSet.add(k)
            for possibleNum in iterationSet:
                i = indexCell[1][0]
                j = indexCell[1][1]
                if (controlSum - possibleNum) not in self.numberField[indexCell[0][0]][indexCell[0][1]]:
                    self.numberField[i][j].discard(possibleNum)
        elif countcells > 2:
            self.balanerTriples(controlSum, indexCell, True)

    def balanerTriples(self, controlSum, indexCell, first):
        countcells = len(indexCell)
        allowAddition = int(controlSum - (((countcells + 1) * countcells) / 2))
        allowedNum = allowAddition + countcells
        if controlSum < 0:
            return False
        if countcells == 1:
            if controlSum in self.numberField[indexCell[0][0]][indexCell[0][1]]:
                return True
            return False
        for counter in range(countcells):
            copynumCell = []
            for k in self.numberField[indexCell[counter][0]][indexCell[counter][1]]:
                copynumCell.append(k)
            allBalanced = False
            for k in copynumCell:
                copyindexCell = []
                for i in range(len(indexCell)):
                    if i == 0:
                        continue
                    copyindexCell.append(indexCell[i])
                if not (self.balanerTriples(controlSum - k, copyindexCell, False)):
                    if first:
                        self.numberField[indexCell[counter][0]][indexCell[counter][1]].discard(k)
                        self.changes = True
                        self.uniqAmCount +=1
                else:
                    allBalanced = True
            return allBalanced


p = [
    [0, 0, 0, 0, 0, 1, 0, 3, 0],
    [2, 3, 1, 0, 9, 0, 0, 0, 0],
    [0, 6, 5, 0, 0, 3, 1, 0, 0],
    [6, 7, 8, 9, 2, 4, 3, 0, 0],
    [1, 0, 3, 0, 5, 0, 0, 0, 6],
    [0, 0, 0, 1, 3, 6, 7, 0, 0],
    [0, 0, 9, 3, 6, 0, 5, 7, 0],
    [0, 0, 6, 0, 1, 9, 8, 4, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0]
]

puzzle = [
    [9, 0, 1, 5, 0, 0, 0, 4, 6],
    [4, 2, 5, 0, 9, 0, 0, 8, 1],
    [8, 6, 0, 0, 1, 0, 0, 2, 0],
    [5, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 1, 9, 0, 0, 0, 4, 6, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 9, 6, 0, 4, 0, 2, 5, 3],
    [2, 0, 0, 0, 6, 0, 8, 1, 7],
    [0, 0, 0, 0, 0, 1, 6, 9, 4]
]

sol = SolvingMethods(puzzle)
for i in sol.numberField:
    print(i)
print(sol.SingleCand)
print(sol.NakedPairs)
print()
print(sol.NakedPairsControl)
print(sol.NakedThreeControl)
print(sol.HidPairControl)
print(sol.HidTreeControl)
print(sol.DeleteExtraVal)
print(sol.Solve())
