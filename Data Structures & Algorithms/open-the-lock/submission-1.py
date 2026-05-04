class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ret = 0

        seen = set(deadends)
        if "0000" in seen:
            return -1
        seen.add("0000")
        q = deque(["0000"])
        count = 0

        while q:
            n = len(q)

            for _ in range(n):
                curr = q.popleft()

                if curr == target:
                    return count

                for i in range(len(curr)):
                    nxtval = (int(curr[i]) + 1) % 10
                    preval = (int(curr[i]) + 9) % 10
                    nxt = curr[:i] + str(nxtval) + curr[i + 1:]
                    pre = curr[:i] + str(preval) + curr[i + 1:]

                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
                    if pre not in seen:
                        seen.add(pre)
                        q.append(pre)
            
            count += 1
        
        return -1
                    

