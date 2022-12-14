import operator

class ApproximateSolution:
    def approx_with_accounting_and_duplicates(array, target):
        c = .01

        solution = [(0, [])]
        for x in sorted(array):
            first_array = []
            for y, y_list in solution:
                first_array.append((x + y, y_list + [x]))
            union_first_second = first_array + solution
            union_first_second = ApproximateSolution.sort_by_col(union_first_second, 0)
            y, y_list = union_first_second[0]
            solution = [(y, y_list)]

            for z, z_list in union_first_second:
                lower_bound = (float(y) + c * float(target) / float(len(array)))
                if lower_bound < z <= target:
                    y = z
                    solution.append((z, z_list))

        return ApproximateSolution.sort_by_col(solution, 0)[-1]

    def sort_by_col(table, col=0):
        return sorted(table, key=operator.itemgetter(col))
