class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        self.num=nums
        self.li=list(set(self.num))
        self.li.sort()
        self.di={}
        for i in range(1,len(self.li)-1):
            if (li[0]+1)!=li[1]:
                self.di[0]=li[0]
            elif li[-1]!=(li[-2]+1):
                self.di[len(self.li)-1]=li[-1]
            elif li[i]!=(li[i-1]+1) and li[i]!=(li[i+1]-1):
                self.di[i]=li[i]