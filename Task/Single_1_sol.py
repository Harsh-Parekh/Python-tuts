class Sol:
    def Single(self,list):
        ret_ls=[]
        for i in list:
            counter=nums.count(i)
            if counter==1:
                ret_ls.append(i)
        if len(ret_ls)==0:
            return -1
        else:
            return ret_ls
            
nums=list(map(int,input('Enter list by space :').split()))

s=Sol()
ret_val=s.Single(nums)

print("The singel element present in list are :",ret_val)
