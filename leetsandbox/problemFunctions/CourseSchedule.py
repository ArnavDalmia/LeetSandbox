def courseScheduleFunctionality(numCourses, prerequisites):
    # Validate prerequisites
    for i in prerequisites:
        if i[0] not in range(numCourses) or i[1] not in range(numCourses):
            return False
    
    # Map each course to its prerequisites
    preMap = {}
    for i in range(numCourses):
        preMap[i] = []
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # Store all courses along the current DFS path
    visiting = set()

    def dfs(crs):
        if crs in visiting:
            # Cycle detected
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True

def main(numCourses, prerequisites):
    result = courseScheduleFunctionality(numCourses, prerequisites)
    
    output = f"""Number of courses: {numCourses}
Prerequisites: {prerequisites}"""
    
    if result:
        output += "\nResult: All courses can be finished"
    else:
        output += "\nResult: Cannot finish all courses (cycle detected)"
    
    return output

# EXAMPLE
# main(2, [[1,0]])
# main(2, [[1,0],[0,1]])