import pylcs

class DynamicProgramming:
    def lcs_dp(first_text, second_text):
        m = len(first_text)
        n = len(second_text)

        L = [[None] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif first_text[i - 1] == second_text[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        return L[m][n]

class LcsRecursion:
    def lcs_recursion(X, Y, m, n):
        if m == 0 or n == 0:
            return 0
        elif X[m - 1] == Y[n - 1]:
            return 1 + LcsRecursion.lcs_recursion(X, Y, m - 1, n - 1);
        else:
            return max(LcsRecursion.lcs_recursion(X, Y, m, n - 1), LcsRecursion.lcs_recursion(X, Y, m - 1, n));


class LcsHuntSzimanski:
    def lcs_Hunt_and_Szymanski(first_text, second_text):

        if len(first_text) > len(second_text):
            first_text, second_text = second_text, first_text
        equal = {}

        if '' == first_text:
            return 0;

        for i in range(0, len(second_text)):
            equal[i + 1] = LcsHuntSzimanski.list_of_indices(second_text[i], first_text)[::-1]

        threshold = [len(first_text) + 1 for _ in range(0, len(second_text) + 1)]
        threshold[0] = 0
        for i in range(0, len(second_text)):
            for j in equal[i + 1]:
                k = LcsHuntSzimanski.look_for_threshold_index(j,
                                                              threshold)  # look for k such that threshold[k-1] < j <= threshold[k]:
                if j < threshold[k]:
                    threshold[k] = j

        result = 0
        for k in range(len(second_text), 0, -1):
            if len(first_text) + 1 != threshold[k]:
                result = k
                break
        return result

    def list_of_indices(c, s):

        result = []
        i = 0
        while i < len(s):
            if type(s) == list:
                try:
                    i = s[i:].index(c) + i + 1
                except ValueError:
                    i = 0
            else:
                i = s.find(c, i) + 1

            if 0 != i:
                result.append(i - 1)
            else:
                break
        return result

    def look_for_threshold_index(j, threshold, left=None, right=None):

        if (None, None) == (left, right):
            left, right = 0, len(threshold) - 1

        if left > right:
            raise ValueError('Value in left higher than right')
        elif left + 1 == right or left == right:
            return right
        else:
            mid = int((left + right) / 2)
            if j <= threshold[mid]:
                left, right = left, mid
            else:
                left, right = mid, right
            return LcsHuntSzimanski.look_for_threshold_index(j, threshold, left, right)


class Wunsch:

    def longestCommonSubsequence( text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        R = len(text1) + 1
        C = len(text2) + 1

        skip_cost = subs_cost = 0  # Usually negative
        match = 1

        # These will have to change based on the skip_cost.
        # I am assuming the cost = 0. Read Wiki for more info.
        prev = [0] * C

        cur = [0] * C

        for r in range(1, R):
            for c in range(1, C):
                if text1[r - 1] == text2[c - 1]:
                   prev[c - 1] += match
                else:
                   prev[c - 1] += subs_cost
                cur[c] = max(prev[c - 1] + skip_cost, prev[c], cur[c - 1] + skip_cost)
            prev = cur
            cur = [0] * C
        return prev[-1]

