import sys
import os
from selenium import webdriver
import numpy as np
import inspect
import copy


URL = 'https://sudoku.org.ua/'

EASY_RB_ID = 'enhe0'        # Easy Radio Button id
NORMAL_RB_ID = 'enhe1'      # Normal Radio Button id
HARD_RB_ID = 'enhe2'        # Hard Radio Button id
EXTREME_RB_ID = 'enhe3'     # Extreme Radio Button id
MINIMAL_RB_ID = 'enhe4'     # Minimal Radio Button id

# Number of fields generated of varying complexity
EASY_DIFF_NUM = 5
NORMAL_DIFF_NUM = 5
HARD_DIFF_NUM = 5
EXTREME_DIFF_NUM = 5
MINIMAL_DIFF_NUM = 5


def print_test_res(puzzle, filDir1, filDir2):

    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

    import solvingMethods
    from solvingMethods import SolvingMethods

    filDir1.write(str(puzzle))
    filDir1.write("\n")
    filDir1.write("*********************")
    filDir1.write("\n")

    puzzle = np.array(puzzle).tolist()
    solving = SolvingMethods(puzzle)
    puzzleSolving = solving.Solve()
    puzzleSolving = np.array(puzzleSolving)
    puzzleSolving = np.reshape(puzzleSolving, (9, 9))
    filDir2.write(str(puzzleSolving))
    filDir2.write("\n")
    filDir2.write("*********************")
    filDir2.write("\n")
    pass


def pars_test():

    driver = webdriver.Edge('parserTest/msedgedriver.exe')
    driver.get(URL)

    filDir1 = open('parserTest/testFi.txt', 'w')
    filDir2 = open('parserTest/testRes.txt', 'w')

    sys.path.append('/parserTest/fieldParser')
    from fieldParser import field_parse

    filDir1.write('\n' + 'EASY' + '\n')
    filDir2.write('\n' + 'EASY' + '\n')

    for num in range(EASY_DIFF_NUM):
        puzzle = field_parse(EASY_RB_ID, driver)
        print_test_res(puzzle, filDir1, filDir2)

    filDir1.write('\n' + 'NORMAL' + '\n')
    filDir2.write('\n' + 'NORMAL' + '\n')

    for num in range(NORMAL_DIFF_NUM):
        puzzle = field_parse(NORMAL_RB_ID, driver)
        print_test_res(puzzle, filDir1, filDir2)

    filDir1.write('\n' + 'HARD' + '\n')
    filDir2.write('\n' + 'HARD' + '\n')

    for num in range(HARD_DIFF_NUM):
        puzzle = field_parse(HARD_RB_ID, driver)
        print_test_res(puzzle, filDir1, filDir2)

    filDir1.write('\n' + 'EXTREME' + '\n')
    filDir2.write('\n' + 'EXTREME' + '\n')

    for num in range(EXTREME_DIFF_NUM):
        puzzle = field_parse(EXTREME_RB_ID, driver)
        print_test_res(puzzle, filDir1, filDir2)

    filDir1.write('\n' + 'MINIMAL' + '\n')
    filDir2.write('\n' + 'MINIMAL' + '\n')

    for num in range(EXTREME_DIFF_NUM):
        puzzle = field_parse(MINIMAL_RB_ID, driver)
        print_test_res(puzzle, filDir1, filDir2)


pars_test()
