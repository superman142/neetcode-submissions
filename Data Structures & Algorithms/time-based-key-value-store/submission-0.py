class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        keyMap = self.store[key]

        timestamps = [t for t, _ in keyMap]

        def findKey(nums, target):
            l = 0
            r = len(nums)

            while l < r:
                mid = (l + r) // 2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            
            return l - 1

        nearestKey = findKey(timestamps, timestamp)

        return "" if nearestKey < 0 else keyMap[nearestKey][1]
        
        
