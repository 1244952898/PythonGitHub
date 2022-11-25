class MergeSort:
    def __int__(self):
        self.nums = None

    def func(self, numList: list) -> list:
        """
        归并排序
        :param numList:
        :return:
        """
        self.nums = numList
        print(0, len(numList) - 1)
        self.merge_sort(0, len(numList) - 1)
        return self.nums

    def merge_sort(self, begin, end):
        print(begin, end)
        if begin < end:
            mid = begin + (end - begin) // 2
            self.merge_sort(begin, mid)
            self.merge_sort(mid + 1, end)
            self.merge(begin, mid, mid + 1, end)

    def merge(self, lb, le, rb, re):
        tempList = [0] * (re - lb + 1)
        tempIndex = 0
        templ, tempr = lb, rb
        while templ <= le and tempr <= re:
            if self.nums[templ] < self.nums[tempr]:
                tempList[tempIndex] = self.nums[templ]
                templ += 1
            else:
                tempList[tempIndex] = self.nums[tempr]
                tempr += 1
            tempIndex += 1

        if templ <= le:
            tempList[tempIndex:] = self.nums[templ:le + 1]
        elif tempr <= re:
            tempList[tempIndex:] = self.nums[tempr:re + 1]
        self.nums[lb: re + 1] = tempList[0:]


if __name__ == '__main__':
    print('归并排序:')
    nums = [7, 5, 6, 3, 1, 0, 9, 4, 8, 2]
    ss = MergeSort()
    ns = ss.func(nums)
    print(ns)
