from algorithm import DynamicProgramming
from algorithm import LcsRecursion
import sys
from algorithm import LcsHuntSzimanski
from algorithm import Wunsch
from run_time import time_calculate
import pylcs
from test import test

sys.setrecursionlimit(10000)

def test_all_algorithm(str1, numList):
    index = 0;
    for i in numList:
        if (LcsRecursion.lcs_recursion(str1,str(i),len(str1),len(str(i))) == LcsHuntSzimanski.lcs_Hunt_and_Szymanski(str1,str(i)) == DynamicProgramming.lcs_dp(str1, str(i)) == Wunsch.longestCommonSubsequence(str1, str(i)) == pylcs.lcs(str1, str(i)) ):
            index += 1;
            print('Test', index, 'passed');
        else:
            index +=1;
            print('Test', index, 'failed');

numList = []

fileName = "random.txt"
numFile = open(fileName, 'r')

lines = numFile.read()

linesSplit = lines.split()
for i in linesSplit:
    numList.append(int(i))
numFile.close()
str1 = "1903481321343214"
test.test_all_algorithm(str1, numList)
print(time_calculate.time_recursion(str1,numList))
print(time_calculate.time_dynamic(str1, numList))
print(time_calculate.time_szimanski(str1,numList))
print(time_calculate.time_wunsch(str1,numList))