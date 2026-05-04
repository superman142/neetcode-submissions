class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        ss={}
        tt={}
        for i in range(0,len(s)):
            ss[s[i]]=1+ss.get(s[i],0)
            tt[t[i]]=1+tt.get(t[i],0)
        for c in ss:
            if ss[c]!=tt.get(c):
                return False
        return True