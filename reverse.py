class ReverseSolution:

    def solve(MAX, inputList):
        solutionIndexList = []
        solutionValueList = []
        currentIndexList = []
        currentValueList = []
        fullSize = len(inputList)
        maxScore = 0
        startIndex = fullSize
        sum = 0
        while ((len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0):

            startIndex = startIndex - 1

            for i in range(startIndex, -1, -1):

                currentValue = inputList[i]

                tempSum = sum + currentValue

                if (tempSum == MAX):
                    sum = tempSum
                    currentIndexList.append(i)
                    currentValueList.append(currentValue)
                    break

                elif (tempSum > MAX):
                    continue

                elif (tempSum < MAX):
                    sum = tempSum
                    currentIndexList.append(i)
                    currentValueList.append(currentValue)
                    continue

            if (maxScore < sum):
                maxScore = sum

                solutionIndexList = []
                solutionValueList = []

                for y in currentIndexList:
                    solutionIndexList.append(y)
                for y in currentValueList:
                    solutionValueList.append(y)

            if (maxScore == MAX):
                break

            if (len(currentValueList) != 0):
                lastVal = currentValueList.pop()
                sum = sum - lastVal

            if (len(currentIndexList) != 0):
                lastIndex = currentIndexList.pop()
                startIndex = lastIndex

            if (len(currentIndexList) == 0 and (startIndex == 0)):
                break
        return solutionValueList