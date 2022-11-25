class ShellSort:

    def func(self, numList: list) -> list:
        """
        希尔排序
        :param numList:
        :return:
        """
        increment = len(numList)
        while increment > 1:
            increment //= 2
            for begin in range(increment):
                for i in range(begin + increment, len(numList), increment):
                    temp = numList[i]
                    j = i - increment
                    while j >= 0:
                        if numList[j] > temp:
                            numList[j + increment] = numList[j]
                            j = j - increment
                        else:
                            break
                    numList[j + increment] = temp
        return numList


if __name__ == '__main__':
    print('希尔排序:')
    nums = [7, 5, 6, 3, 1, 0, 9, 4, 8, 2]
    ss = ShellSort()
    ns = ss.func(nums)
    print(ns)
