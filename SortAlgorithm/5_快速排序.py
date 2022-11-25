class QuickSort:

    def __init__(self):
        self.nums = None

    def func(self, num_list: list) -> list:
        """
        快速排序
        :param num_list:
        :return:
        """
        self.nums = num_list
        self.quick_sort(0, len(num_list) - 1)
        return self.nums

    def quick_sort(self, begin, end):
        if begin < end:
            mid = self.partition(begin, end)
            self.quick_sort(begin, mid)
            self.quick_sort(mid + 1, end)

    def partition(self, begin, end) -> int:
        """

        :param begin:
        :param end:
        :return:
        """
        print(begin, end, self.nums)
        mid = begin + (end - begin) // 2
        if self.nums[begin] > self.nums[end]:
            self.nums[begin], self.nums[end] = self.nums[end], self.nums[begin]

        if self.nums[mid] > self.nums[end]:
            self.nums[begin], self.nums[end] = self.nums[end], self.nums[begin]
        elif self.nums[mid] > self.nums[begin]:
            self.nums[begin], self.nums[mid] = self.nums[mid], self.nums[begin]
        temp = self.nums[begin]

        while begin < end:
            while begin < end and temp <= self.nums[end]:
                end -= 1
            if begin < end and temp > self.nums[end]:
                self.nums[begin] = self.nums[end]
                begin += 1
            while begin < end and self.nums[begin] <= temp:
                begin += 1
            if begin < end and self.nums[begin] > temp:
                self.nums[end] = self.nums[begin]
                end -= 1
        self.nums[begin] = temp
        return begin


if __name__ == '__main__':
    print('归并排序:')
    nums = [7, 5, 6, 3, 1, 0, 9, 4, 8, 2]
    ss = QuickSort()
    ns = ss.func(nums)
    print(ns)
