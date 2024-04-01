class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0 : return
        
        len1 = len(nums1)
        end_index = len1 - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[end_index] = nums1[m-1]
                m -=1
            else:
                nums1[end_index] = nums2[n-1]
                n -=1
            
            end_index -=1

        while n > 0:
            nums1[end_index] = nums2[n]
            n -=1
            end_index -=1
        

        