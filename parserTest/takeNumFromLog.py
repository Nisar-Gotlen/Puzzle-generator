
from bdb import bar
import numpy

filDir = open('parserTest/sample.log', 'r')
zeros_EASY = numpy.array([])
zeros_NORMAL = numpy.array([])
zeros_HARD = numpy.array([])
zeros_EXTREME = numpy.array([])

EASY_SingleCand = numpy.array([])
EASY_NakedPairs = numpy.array([])
EASY_NakedThree = numpy.array([])
EASY_HidPair = numpy.array([])
EASY_HidTree = numpy.array([])
EASY_DeleteExtraVal = numpy.array([])

NORMAL_SingleCand = numpy.array([])
NORMAL_NakedPairs = numpy.array([])
NORMAL_NakedThree = numpy.array([])
NORMAL_HidPair = numpy.array([])
NORMAL_HidTree = numpy.array([])
NORMAL_DeleteExtraVal = numpy.array([])

HARD_SingleCand = numpy.array([])
HARD_NakedPairs = numpy.array([])
HARD_NakedThree = numpy.array([])
HARD_HidPair = numpy.array([])
HARD_HidTree = numpy.array([])
HARD_DeleteExtraVal = numpy.array([])

EXTREME_SingleCand = numpy.array([])
EXTREME_NakedPairs = numpy.array([])
EXTREME_NakedThree = numpy.array([])
EXTREME_HidPair = numpy.array([])
EXTREME_HidTree = numpy.array([])
EXTREME_DeleteExtraVal = numpy.array([])

k = 0
for line in filDir:
    if k == 0:
        l = line.split()
        if l[0] == "EASY":
            zeros_EASY = numpy.append(zeros_EASY, int(l[2]))
        elif l[0] == "NORMAL":
            zeros_NORMAL = numpy.append(zeros_NORMAL, int(l[2]))
        elif l[0] == "HARD":
            zeros_HARD = numpy.append(zeros_HARD, int(l[2]))
        elif l[0] == "EXTREME":
            zeros_EXTREME = numpy.append(zeros_EXTREME, int(l[2]))

    elif k == 1:
        l = line.split()
        if l[0] == "EASY":
            EASY_SingleCand = numpy.append(EASY_SingleCand, int(l[2]))
        elif l[0] == "NORMAL":
            NORMAL_SingleCand = numpy.append(NORMAL_SingleCand, int(l[2]))
        elif l[0] == "HARD":
            HARD_SingleCand = numpy.append(HARD_SingleCand, int(l[2]))
        elif l[0] == "EXTREME":
            EXTREME_SingleCand = numpy.append(EXTREME_SingleCand, int(l[2]))

    elif k == 2:
        l = line.split()
        if l[0] == "EASY":
            EASY_NakedPairs = numpy.append(EASY_NakedPairs, int(l[2]))
        elif l[0] == "NORMAL":
            NORMAL_NakedPairs = numpy.append(NORMAL_NakedPairs, int(l[2]))
        elif l[0] == "HARD":
            HARD_NakedPairs = numpy.append(HARD_NakedPairs, int(l[2]))
        elif l[0] == "EXTREME":
            EXTREME_NakedPairs = numpy.append(EXTREME_NakedPairs, int(l[2]))

    elif k == 3:
        l = line.split()
        if l[0] == "EASY":
            EASY_NakedThree = numpy.append(EASY_NakedThree, int(l[2]))
        elif l[0] == "NORMAL":
            NORMAL_NakedThree = numpy.append(NORMAL_NakedThree, int(l[2]))
        elif l[0] == "HARD":
            HARD_NakedThree = numpy.append(HARD_NakedThree, int(l[2]))
        elif l[0] == "EXTREME":
            EXTREME_NakedThree = numpy.append(EXTREME_NakedThree, int(l[2]))

    elif k == 4:
        l = line.split()
        if l[0] == "EASY":
            EASY_HidPair = numpy.append(EASY_HidPair, int(l[2]))
        elif l[0] == "NORMAL":
            NORMAL_HidPair = numpy.append(NORMAL_HidPair, int(l[2]))
        elif l[0] == "HARD":
            HARD_HidPair = numpy.append(HARD_HidPair, int(l[2]))
        elif l[0] == "EXTREME":
            EXTREME_HidPair = numpy.append(EXTREME_HidPair, int(l[2]))

    elif k == 5:
        l = line.split()
        if l[0] == "EASY":
            EASY_HidTree = numpy.append(EASY_HidTree, int(l[2]))
        elif l[0] == "NORMAL":
            NORMAL_HidTree = numpy.append(NORMAL_HidTree, int(l[2]))
        elif l[0] == "HARD":
            HARD_HidTree = numpy.append(HARD_HidTree, int(l[2]))
        elif l[0] == "EXTREME":
            EXTREME_HidTree = numpy.append(EXTREME_HidTree, int(l[2]))

    elif k == 6:
        l = line.split()
        if l[0] == "EASY":
            EASY_DeleteExtraVal = numpy.append(EASY_DeleteExtraVal, int(l[2]))
        elif l[0] == "NORMAL":
            NORMAL_DeleteExtraVal = numpy.append(
                NORMAL_DeleteExtraVal, int(l[2]))
        elif l[0] == "HARD":
            HARD_DeleteExtraVal = numpy.append(HARD_DeleteExtraVal, int(l[2]))
        elif l[0] == "EXTREME":
            EXTREME_DeleteExtraVal = numpy.append(
                EXTREME_DeleteExtraVal, int(l[2]))

    if k != 6:
        k += 1
    else:
        k = 0
print("zeros_EASY min " + str(numpy.amin(zeros_EASY)) +
      " max " + str(numpy.amax(zeros_EASY)))


print("zeros_NORMAL min " + str(numpy.amin(zeros_NORMAL)) +
      " max " + str(numpy.amax(zeros_NORMAL)))
print("zeros_HARDL min " + str(numpy.amin(zeros_HARD)) +
      " max " + str(numpy.amax(zeros_HARD)))
print("zeros_EXTREME min " + str(numpy.amin(zeros_EXTREME)) +
      " max " + str(numpy.amax(zeros_EXTREME)))

print("EASY_SingleCand min " + str(numpy.amin(EASY_SingleCand)) +
      " max " + str(numpy.amax(EASY_SingleCand)))
print("EASY_NakedPairs min " + str(numpy.amin(EASY_NakedPairs)) +
      " max " + str(numpy.amax(EASY_NakedPairs)))
print("EASY_NakedThree min " + str(numpy.amin(EASY_NakedThree)) +
      " max " + str(numpy.amax(EASY_NakedThree)))
print("EASY_HidPair min " + str(numpy.amin(EASY_HidPair)) +
      " max " + str(numpy.amax(EASY_HidPair)))
print("EASY_HidTree min " + str(numpy.amin(EASY_HidTree)) +
      " max " + str(numpy.amax(EASY_HidTree)))
print("EASY_DeleteExtraVal min " + str(numpy.amin(EASY_DeleteExtraVal)) +
      " max " + str(numpy.amax(EASY_DeleteExtraVal)))

print("NORMAL_SingleCand min " + str(numpy.amin(NORMAL_SingleCand)) +
      " max " + str(numpy.amax(NORMAL_SingleCand)))
print("NORMAL_NakedPairs min " + str(numpy.amin(NORMAL_NakedPairs)) +
      " max " + str(numpy.amax(NORMAL_NakedPairs)))
print("NORMAL_NakedThree min " + str(numpy.amin(NORMAL_NakedThree)) +
      " max " + str(numpy.amax(NORMAL_NakedThree)))
print("NORMAL_HidPair min " + str(numpy.amin(NORMAL_HidPair)) +
      " max " + str(numpy.amax(NORMAL_HidPair)))
print("NORMAL_HidTree min " + str(numpy.amin(NORMAL_HidTree)) +
      " max " + str(numpy.amax(NORMAL_HidTree)))
print("NORMAL_DeleteExtraVal min " + str(numpy.amin(NORMAL_DeleteExtraVal)) +
      " max " + str(numpy.amax(NORMAL_DeleteExtraVal)))

print("HARD_SingleCand min " + str(numpy.amin(HARD_SingleCand)) +
      " max " + str(numpy.amax(HARD_SingleCand)))
print("HARD_NakedPairs min " + str(numpy.amin(HARD_NakedPairs)) +
      " max " + str(numpy.amax(HARD_NakedPairs)))
print("HARD_NakedThree min " + str(numpy.amin(HARD_NakedThree)) +
      " max " + str(numpy.amax(HARD_NakedThree)))
print("HARD_HidPair min " + str(numpy.amin(HARD_HidPair)) +
      " max " + str(numpy.amax(HARD_HidPair)))
print("HARD_HidTree min " + str(numpy.amin(HARD_HidTree)) +
      " max " + str(numpy.amax(HARD_HidTree)))
print("HARD_DeleteExtraVal min " + str(numpy.amin(HARD_DeleteExtraVal)) +
      " max " + str(numpy.amax(HARD_DeleteExtraVal)))

print("EXTREME_SingleCand min " + str(numpy.amin(EXTREME_SingleCand)) +
      " max " + str(numpy.amax(EXTREME_SingleCand)))
print("EXTREME_NakedPairs min " + str(numpy.amin(EXTREME_NakedPairs)) +
      " max " + str(numpy.amax(EXTREME_NakedPairs)))
print("EXTREME_NakedThree min " + str(numpy.amin(EXTREME_NakedThree)) +
      " max " + str(numpy.amax(EXTREME_NakedThree)))
print("EXTREME_HidPair min " + str(numpy.amin(EXTREME_HidPair)) +
      " max " + str(numpy.amax(EXTREME_HidPair)))
print("EXTREME_HidTree min " + str(numpy.amin(EXTREME_HidTree)) +
      " max " + str(numpy.amax(EXTREME_HidTree)))
print("EXTREME_DeleteExtraVal min " + str(numpy.amin(EXTREME_DeleteExtraVal)) +
      " max " + str(numpy.amax(EXTREME_DeleteExtraVal)))
