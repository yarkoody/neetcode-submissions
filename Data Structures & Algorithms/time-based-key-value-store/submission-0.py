from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not self.dic[key]: 
            return ""
        arr = self.dic[key]
        left = 0
        right = len(arr) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
        


        
