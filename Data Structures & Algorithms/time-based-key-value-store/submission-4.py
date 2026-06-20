class TimeMap:
    #key: key
        #key: time
        #value: value 

    def __init__(self):
        self.store = {} #key : list of [value,time]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store.keys():
            self.store[key].append([value,timestamp])
        else: 
            self.store[key] = [[value,timestamp]]
        return None

    def get(self, key: str, timestamp: int) -> str:
        #key exists and len(value) == 1 --> return value 
        if key in self.store.keys() and len(self.store[key]) == 1:
            if timestamp < self.store[key][0][1]:
                return ""
            return self.store[key][0][0]

        #key exists and len(value) > 1 --> binary search --> return value
        elif key in self.store.keys() and len(self.store[key]) > 1:
            values = self.store[key]
            res = ""
            l = 0
            r = len(values) - 1
            while l<=r:
                m = (l+r)//2
                if values[m][1] <= timestamp: 
                    res = values[m][0]
                    l = m + 1
                else: #values[m] >= timestamp
                    r = m -1
            return res
         #key doesn't exist --> return ""
        else:
            return ""
                

        
