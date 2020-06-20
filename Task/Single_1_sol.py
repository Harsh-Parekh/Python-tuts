nums = [1,1,2,3,3,4,4,8,8]
class Sol:
    def Single(self,list):
        for i in list:
            counter=nums.count(i)
            if counter==1:
                return i
            else:
                return -1

s=Sol()
ret_val=s.Single(nums)
print(ret_val)