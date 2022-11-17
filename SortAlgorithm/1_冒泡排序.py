class BubbleSort:
    def func(self, numList: list) -> list:
        """
        冒泡排序
        :param numList:
        :return:
        """
        if not list:
            return numList
        for i in range(len(numList)):
            for j in range(len(numList) - 1 - i):
                if numList[j] > numList[j+1]:
                    numList[j], numList[j + 1] = numList[j + 1], numList[j]
        return numList


if __name__ == '__main__':
    print('简单选择排序:')
    nums = [7, 5, 6, 3, 1, 0, 9, 4, 8, 2]
    ss = BubbleSort()
    ns = ss.func(nums)
    print(ns)
