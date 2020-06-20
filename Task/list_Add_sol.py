class Sol:
    def cal_ls(self,A,K):
        s=''
        for i in A:
            s+=str(i)
        ret_val=int(s)+K
        ret_ls=[]
        for k in str(ret_val):
            ret_ls.append(k)

        return ret_ls

A = [1,2,0,0]
K = 34

s=Sol()
ans_1=s.cal_ls(A,K)
print(ans_1)