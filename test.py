from bruteforce import BruteForceSolution
from memoization import MemoizationSolution
from approximation import ApproximateSolution
from reverse import ReverseSolution

def test_1():
    arr = [97, 8, 36, 67, 3, 42, 29, 9, 96, 18, 74, 15];
    k = 421;
    assert BruteForceSolution.subsetsum(arr, k) == True, "test failed"
    assert MemoizationSolution.stackoverflow(arr, k) == True, "test failed"
    assert ApproximateSolution.approx_with_accounting_and_duplicates(arr, k) == (
        421, [9, 36, 42, 67, 74, 96, 97]), "test failed"
    assert ReverseSolution.solve(k, arr) == [15, 74, 18, 96, 9, 42, 3, 67, 97], "test failed"


def test_2():
    arr = [25, 12, 29, 43, 46, 29];
    k = 685;
    assert BruteForceSolution.subsetsum(arr, k) == False, "test failed"
    assert MemoizationSolution.stackoverflow(arr, k) == False, "test failed"


def test_3():
    arr = [46, 18, 95, 92, 42, 94];
    k = 88;
    assert BruteForceSolution.subsetsum(arr, k) == True, "test failed"
    assert MemoizationSolution.stackoverflow(arr, k) == True, "test failed"
    assert ApproximateSolution.approx_with_accounting_and_duplicates(arr, k) == (88, [42, 46]), "test failed"
    assert ReverseSolution.solve(k, arr) == [42, 46], "test failed"


def test_4():
    arr = [51, 76, 99, 44, 60, 70, 29, 11, 38, 22, 72, 50, 54, 49, 25, 70];
    k = 516;
    assert BruteForceSolution.subsetsum(arr, k) == True, "test failed"
    assert MemoizationSolution.stackoverflow(arr, k) == True, "test failed"


def test_5():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 18;
    assert BruteForceSolution.subsetsum(arr, k) == True, "test failed"
    assert MemoizationSolution.stackoverflow(arr, k) == True, "test failed"
    assert ApproximateSolution.approx_with_accounting_and_duplicates(arr, k) == (18, [5, 6, 7]), "test failed"
    assert ReverseSolution.solve(k, arr) == [7, 6, 5], "test failed"


def test_6():
    arr = [7436, 2251, 6495, 1753, 1422, 6304, 6432, 5330, 6124,
           2360, 1282, 3640, 2803, 8009, 4948, 5731, 7898, 7118, 154, 1483, 6787,
           9759, 6270]
    k = 53185;
    assert MemoizationSolution.stackoverflow(arr, k) == True, "test failed"
    assert ApproximateSolution.approx_with_accounting_and_duplicates(arr, k) == (
        53175, [1483, 1753, 4948, 5731, 6124, 6304, 6432, 6495, 6787, 7118]), "test failed"
    assert ReverseSolution.solve(k, arr) == [6270, 9759, 6787, 1483, 154, 7118, 8009, 3640, 1282, 6432,
                                             2251], "test failed"

def test_7():
    arr = [2048, 2057, 4106, 6161, 4117, 2076, 6174, 4128, 6178, 6181, 4133, 8233, 4138, 6197, 6201, 4155, 8253, 2112,
           6209, 4166, 6217, 4170, 8267, 8268, 2126, 4174, 6224, 4177, 2130, 8275, 8278, 2134, 6235, 2147, 8291, 100,
           102, 8297, 8301, 6256, 112, 8304, 113, 2162, 6262, 125, 4221, 4224, 131, 6275, 135, 136, 6280, 139, 4238,
           4239, 4241, 6290, 4243, 2196, 8341, 8342, 151, 4253, 6302, 6301, 2208, 160, 8355, 6308, 4260, 169, 171,
           6315,
           4269, 175, 6321, 8369, 8371, 182, 8375, 6328, 185, 4282, 188, 189, 191, 6336, 200, 6345, 6351, 4306, 8403,
           4308, 2258, 4314, 222, 6367, 225, 4322, 226, 8423, 6376, 4330, 239, 8435, 245, 6390, 6391, 2299, 6396, 6397,
           8445, 252, 2308, 262, 6409, 269, 4366, 270, 272, 4369, 2322, 274, 2326, 2331, 8476, 285, 6430, 4385, 4386,
           8483, 6436, 2339, 4390, 2342, 296, 8481, 6433, 6441, 2348, 6450, 307, 4404, 2354, 2358, 6459, 8508, 318,
           4418, 324, 4420, 8518, 2375, 2381, 334, 335, 2385, 2386, 337, 4438, 343, 8537, 4444, 4447, 2401, 4451, 357,
           8550, 4455, 7805, 6505, 8554, 363, 366, 4470, 4476, 6526, 388, 2438, 392, 2441, 8590, 4497, 2450, 6546,
           4499,
           2452, 2454, 409, 2459, 2467, 424, 6569, 2475, 8624, 8626, 436, 6583, 4537, 4540, 8639, 2496, 2499, 4547,
           8649]
    k = 100000;
    assert ApproximateSolution.approx_with_accounting_and_duplicates(arr, k) == (99998,
                                                                                 [136, 334, 388, 392, 436, 6583, 7805,
                                                                                  8233, 8267, 8291, 8301, 8341, 8371,
                                                                                  8476, 8481, 8537,
                                                                                  8626]), "test failed"
    assert ReverseSolution.solve(k, arr) == [8649, 4547, 2499, 2496, 8639, 4540, 4537, 6583, 436, 8626, 8624, 2475,
                                             6569, 424, 2467, 2459, 409, 2454, 2452, 4499, 6546, 2450, 4497, 392, 388,
                                             366, 363, 343, 171, 100], "test failed"
