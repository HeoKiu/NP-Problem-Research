from algorithm import DynamicProgramming
from algorithm import LcsRecursion
from algorithm import LcsHuntSzimanski
from algorithm import Wunsch
import pylcs

class test:
    def test_all_algorithm(str1, numList):
        index = 0;
        for i in numList:
            if (LcsRecursion.lcs_recursion(str1, str(i), len(str1),
                                           len(str(i))) == LcsHuntSzimanski.lcs_Hunt_and_Szymanski(str1,
                                                                                                   str(i)) == DynamicProgramming.lcs_dp(
                str1, str(i)) == Wunsch.longestCommonSubsequence(str1, str(i)) == pylcs.lcs(str1, str(i))):
                index += 1;
                print('Test', index, 'passed');
            else:
                index += 1;
                print('Test', index, 'failed');
