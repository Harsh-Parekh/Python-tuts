

class Sol:
    def Merger_log(self,nums_1,nums_2,m,n):
        a=0
        for i in range(3,len(nums_1)):
            if a<n:
                nums_1[i]=nums_2[a]
                a+=1
        return  nums_1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s=Sol()
meg=s.Merger_log(nums1,nums2,m,n)
print(meg)