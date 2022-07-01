class Solution(object):
    def targetIndices(self, nums, target):
        a=sorted(nums)

        low=0
        high=len(a)-1
        list=[]
        while low<=high:
            mid=(high+low)//2
            if len(a)>mid and a[mid]==target:
                list.append(mid)
                a.pop(mid)
            elif len(a)>mid and a[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return list[::-1]
        
