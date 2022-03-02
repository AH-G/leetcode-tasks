class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0 and m==0:
            print("if is engaged")
            nums1=[]
        elif n==0:
            nums1=nums1
        elif m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        elif nums1[m-1]<=nums2[0]:
            for i in range(n):
                nums1[m+i]=nums2[i]
        else:
            for i in range(n):
                nums1[m+i]=nums2[i]
            nums1.sort()
