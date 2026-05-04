class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # find peak
        def findPeak():
            lo = 1
            hi = mountainArr.length() - 2

            while lo <= hi:
                mid = (lo + hi) // 2
                
                curr = mountainArr.get(mid)
                prev = mountainArr.get(mid - 1)
                nxt = mountainArr.get(mid + 1)

                if prev < curr < nxt:
                    lo = mid + 1
                elif prev > curr > nxt:
                    hi = mid - 1
                else:
                    return (mid, curr)
        
        peak, peakVal = findPeak()

        if peakVal == target:
            return peak
        
        if target > peakVal:
            return -1

        lo = 0
        hi = peak - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            midVal = mountainArr.get(mid)

            if target < midVal:
                hi = mid - 1
            elif target > midVal:
                lo = mid + 1
            else:
                return mid


        lo = peak + 1
        hi = mountainArr.length() - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            midVal = mountainArr.get(mid)

            if target > midVal:
                hi = mid - 1
            elif target < midVal:
                lo = mid + 1
            else:
                return mid
        
        return -1
