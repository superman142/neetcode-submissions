class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for x in d:    
            res.append(d[x])
        res.sort()

        for j in range(k):
            for x in d:
                if d[x]==res[len(res)-1]:
                    ans.append(x)
                    res.pop()
                if len(ans)==k:
                    return ans 

