#In this file I implemented new algorithm(Hunt_Szimansky) and compare, test all of three solution.
import time;
import pylcs;
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

def lcs_recursion(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursion(X, Y, m - 1, n - 1);
    else:
        return max(lcs_recursion(X, Y, m, n - 1), lcs_recursion(X, Y, m - 1, n));
def lcs_Hunt_and_Szymanski(s1, s2):

    # let s1 be the shortest string
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    equal = {}

    if '' == s1:
        return 0;

    for i in range(0, len(s2)):
        equal[i + 1] = list_of_indices(s2[i], s1)[::-1]

    threshold = [len(s1) + 1 for _ in range(0, len(s2) + 1)]
    threshold[0] = 0
    for i in range(0, len(s2)):
        for j in equal[i + 1]:
            k = look_for_threshold_index(j, threshold)  # look for k such that threshold[k-1] < j <= threshold[k]:
            if j < threshold[k]:
                threshold[k] = j


    result = 0
    for k in range(len(s2), 0, -1):
        if len(s1) + 1 != threshold[k]:
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
        return look_for_threshold_index(j, threshold, left, right)
# X = "AGGTAB"
# Y = "GXTXAYBBCATA"
# timeStart_first = time.time();
# print("Length of LCS is", lcs_recursion(X, Y, len(X), len(Y)));
# timeEnd_first = time.time();
# print("total time:", timeEnd_first - timeStart_first)
# timeStart_second = time.time();
# print("Length of LCS is", lcs_dp(X, Y));
# timeEnd_second = time.time();
# print("total time:", timeEnd_second - timeStart_second);
def test_all_algo(str1, numList):
    index = 0;
    for i in numList:
        if (lcs_recursion(str1, str(i), len(str1), len(str(i))) == lcs_Hunt_and_Szymanski(str1, str(i)) == lcs_dp(str1, str(i)) == pylcs.lcs(str1, str(i))):
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

str1 = "0123456789"

test_all_algo(str1, numList);
#time test 1
timeStart = time.time()
for i in numList:
    # print("LCS_recursion",lcs_recursion(str1, str(i),len(str1),len(str(i))))
    lcs_recursion(str1, str(i), len(str1), len(str(i)));

timeEnd = time.time()
recursion_time =  timeEnd - timeStart;

#time test 2

timeStart_second = time.time();

for i in numList:
    # print("LCS_dp",lcs_dp(str1, str(i)))
    lcs_dp(str1, str(i));
timeEnd_second = time.time();

dp_time = timeEnd_second - timeStart_second;

#time test 3

timeStart_third = time.time()

for i in numList:
    # print("LCS_Hunt_Szymanski",lcs_Hunt_and_Szymanski(str1, str(i)))
    lcs_Hunt_and_Szymanski(str1, str(i))
timeEnd_third = time.time();
Hunt_szymanski_time =  timeEnd_third - timeStart_third;

#time test 4

timeStart_forth = time.time()

for i in numList:
    # print("LCS_Hunt_Szymanski",lcs_Hunt_and_Szymanski(str1, str(i)))
    pylcs.lcs(str1, str(i))
timeEnd_forth = time.time();
pylcs_time =  timeEnd_forth - timeStart_forth;

print("first solution", recursion_time);
print("second solution", dp_time);
print("third solution", Hunt_szymanski_time);
print("pylcs solution", pylcs_time)

