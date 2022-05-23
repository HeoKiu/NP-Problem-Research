class GreedySolution:
    def subset_sum(l, k):  # l = list values, k is subset sum
        l = sorted(l, reverse=True)
        subset = set([])
        for i in l:
            if k >= i and i not in subset:
                k -= i
                subset.add(i)
            if k == 0:
                break
        return subset