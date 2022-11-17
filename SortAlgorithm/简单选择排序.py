# 按间距中的绿色按钮以运行脚本。
class SimpleSort:
    def SimpleSortMethod(self,nums:list)->list:
        """
        简单排序
        :param nums:
        :return: list
        """
        if not nums:
            return
        n=nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums



if __name__ == '__main__':
    print('简单选择排序:')
    nums=[7,5,6,3,1,0,9,4,8,2]
    ss= SimpleSort()
    ns =ss.SimpleSortMethod(nums)
    print(ns)
