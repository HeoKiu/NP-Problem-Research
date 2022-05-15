from bruteforce import BruteForceSolution
from approximation import ApproximateSolution
from memoization import MemoizationSolution;
from reverse import ReverseSolution
import timeit
import time
data = []
with open("testcase/testcase-20.txt") as file:
    for line in file:
        line = line.strip()
        data.append(int(line))

target = 10000
time0 = time.time()
bf =BruteForceSolution.subsetsum(data, target)
time1 = time.time()
so = MemoizationSolution.stackoverflow(data, target)
time2 = time.time()
he = ApproximateSolution.approx_with_accounting_and_duplicates(data,target)
time3 = time.time()
re = ReverseSolution.solve(target,data)
time4 = time.time()

print('Brute force:', bf, time1 - time0)
print('Memoization', so, time2 - time1)
print('Approximate:', he, time3 - time2)
print('Reverse:', re, time4 - time3)
