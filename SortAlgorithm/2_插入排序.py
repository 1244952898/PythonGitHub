class InsertionSort:
    def func(self, numList: list) -> list:
        """
        插入排序
        :param numList:
        :return:
        """
        for i in range(1,len(numList)):
            temp = numList[i]
            j=i-1
            while j>=0:
                if numList[j] <= temp:
                    break
                numList[j+1]=numList[j]
                j-=1
            numList[j + 1] = temp
        return  numList

if __name__ == '__main__':
    print('简单选择排序:')
    nums = [7, 5, 6, 3, 1, 0, 9, 4, 8, 2]
    ss = InsertionSort()
    ns = ss.func(nums)
    print(ns)