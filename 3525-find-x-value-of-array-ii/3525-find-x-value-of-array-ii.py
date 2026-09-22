class Solution:
    def resultArray(self, nums, k, queries):
        n=len(nums)
        t=[(1,[0]*k) for _ in range(4*n)]

        def merge(a,b):
            p,c=a
            q,d=b
            z=c[:]
            for r in range(k):
                z[p*r%k]+=d[r]
            return p*q%k,z

        def build(i,l,r):
            if l==r:
                v=nums[l]%k
                t[i]=(v,[int(j==v) for j in range(k)])
                return
            m=(l+r)//2
            build(i*2,l,m)
            build(i*2+1,m+1,r)
            t[i]=merge(t[i*2],t[i*2+1])

        def update(i,l,r,x,v):
            if l==r:
                v%=k
                t[i]=(v,[int(j==v) for j in range(k)])
                return
            m=(l+r)//2
            if x<=m: update(i*2,l,m,x,v)
            else: update(i*2+1,m+1,r,x,v)
            t[i]=merge(t[i*2],t[i*2+1])

        def query(i,l,r,ql):
            if l>=ql:
                return t[i]
            m=(l+r)//2
            if ql>m: return query(i*2+1,m+1,r,ql)
            return merge(query(i*2,l,m,ql),t[i*2+1])

        build(1,0,n-1)
        ans=[]
        for idx,val,start,x in queries:
            update(1,0,n-1,idx,val)
            ans.append(query(1,0,n-1,start)[1][x])
        return ans