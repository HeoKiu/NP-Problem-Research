class MemoizationSolution:
    def stackoverflow(x_list, target):
        memo = dict()
        result, _ = MemoizationSolution.get_one_subset(x_list, x_list, target, memo)
        if not result:
            return False
        else:
            return True
    def get_one_subset(v, w, S, memo):
        subset = []
        id_subset = []
        for i, (x, y) in enumerate(zip(v, w)):
            if MemoizationSolution.find_all_subset(v, i + 1, S - x, memo) > 0:
                subset.append(x)
                id_subset.append(y)
                S -= x
        return subset, id_subset

    def find_all_subset(v, i, S, memo):
        if i >= len(v):
            return 1 if S == 0 else 0
        if (i, S) not in memo:
            count = MemoizationSolution.find_all_subset(v, i + 1, S, memo)
            count += MemoizationSolution.find_all_subset(v, i + 1, S - v[i], memo)
            memo[(i, S)] = count
        return memo[(i, S)]

