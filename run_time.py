import time
from algorithm import DynamicProgramming
from algorithm import LcsRecursion
from algorithm import LcsHuntSzimanski
from algorithm import Wunsch

class time_calculate:
    def time_recursion(str1, numList):
        timeStart = time.time();
        for i in numList:
            LcsRecursion.lcs_recursion(str1, str(i), len(str1), len(str(i)));
        timeEnd = time.time()
        recursion_time = timeEnd - timeStart;
        return recursion_time;
    def time_dynamic(str1, numList):
        timeStart = time.time();
        for i in numList:
            DynamicProgramming.lcs_dp(str1, str(i));
        timeEnd = time.time()
        run_time = timeEnd - timeStart;
        return run_time;

    def time_szimanski(str1, numList):
        timeStart = time.time();
        for i in numList:
           LcsHuntSzimanski.lcs_Hunt_and_Szymanski(str1, str(i));
        timeEnd = time.time()
        run_time = timeEnd - timeStart;
        return run_time;
    def time_wunsch(str1, numList):
        timeStart = time.time();
        for i in numList:
            Wunsch.longestCommonSubsequence(str1, str(i));
        timeEnd = time.time()
        run_time = timeEnd - timeStart;
        return run_time;