
class TimeMap:
    def __init__(self):
        self.store = {}  # hashmap for key: [contains [value, timestamp] pairs]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = ((l + r) // 2)
            if values[m][1] == timestamp:
                res = values[m][0]
                break
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

def main():
    output = "TimeMap operations demonstration:\n"
    
    # Create TimeMap
    timemap = TimeMap()
    output += "Created TimeMap\n"
    
    # Test operations
    operations = [
        ("set", "foo", "bar", 1),
        ("get", "foo", 1),
        ("get", "foo", 3),
        ("set", "foo", "bar2", 4),
        ("get", "foo", 4),
        ("get", "foo", 5),
        ("set", "love", "high", 10),
        ("set", "love", "low", 20),
        ("get", "love", 5),
        ("get", "love", 10),
        ("get", "love", 15),
        ("get", "love", 20),
        ("get", "love", 25)
    ]
    
    for op in operations:
        if op[0] == "set":
            _, key, value, timestamp = op
            timemap.set(key, value, timestamp)
            output += f"Set: key='{key}', value='{value}', timestamp={timestamp}\n"
            output += f"  Store state: {timemap.store}\n"
        elif op[0] == "get":
            _, key, timestamp = op
            result = timemap.get(key, timestamp)
            output += f"Get: key='{key}', timestamp={timestamp} -> '{result}'\n"
            
            # Show the binary search process for this get
            values = timemap.store.get(key, [])
            if values:
                output += f"  Available values for '{key}': {values}\n"
                l, r = 0, len(values) - 1
                found_value = ""
                while l <= r:
                    m = (l + r) // 2
                    if values[m][1] <= timestamp:
                        found_value = values[m][0]
                        output += f"    Checking index {m}: timestamp {values[m][1]} <= {timestamp}, update result to '{found_value}'\n"
                        l = m + 1
                    else:
                        output += f"    Checking index {m}: timestamp {values[m][1]} > {timestamp}, search left\n"
                        r = m - 1
    
    return output.rstrip()

# EXAMPLE
# main()
