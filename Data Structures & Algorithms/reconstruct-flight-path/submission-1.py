class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = defaultdict(list)

        for frm, to in tickets:
            adjList[frm].append(to)
        
        ret = ["JFK"]

        def dfs(frm):
            if len(ret) == len(tickets) + 1:
                return True
            
            for i, nei in enumerate(adjList[frm]):
                ret.append(nei)
                adjList[frm].pop(i)
                if dfs(nei): return True
                ret.pop()
                adjList[frm].insert(i, nei)

            return False

        dfs("JFK")
        return ret
