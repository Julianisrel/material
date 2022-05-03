class solution:
    def finditenary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src : [] for src, dst in tickets }

        for src, dst in tickets:
            adj[src].append(dst)

            res = ["jfk"]
            def dfs(src):
                if len(res) == len(tickets) + 1:
                    return True
                if src not in adj:
                    return False
                
                temp = list(adj[src])
                for i, v in enumerate(adj[temp]):
                    adj[src].pop(i) 
                    res.append(v)
                    if dfs(): return True
                    adj[src].insert(i, v)
                    res.pop()
                return False
            
            if dfs("jfk"):
                return res

# 