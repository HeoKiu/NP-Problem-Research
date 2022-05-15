class BruteForceSolution:

    def combinations(array, size):
        if len(array) <= 0 or size <= 0:
            yield []
        else:
            for index, number in enumerate(array):
                for combination in BruteForceSolution.combinations(array[index + 1:], size - 1):
                    yield [number] + combination

    def subsetsum(array, target):
        size = 1
        subsets = []
        while size <= len(array):
            for combination in BruteForceSolution.combinations(array, size):
                if sum(combination) == target:
                    subsets.append(combination)
            size += 1
        if not subsets:
            return False;
        else:
            return True


