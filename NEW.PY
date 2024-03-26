strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(stringsList):
    groupDict = {}
    for string in stringsList:
        sortedString = "".join(sorted(string))
        if sortedString not in groupDict:
            groupDict[sortedString]=[]
        groupDict[sortedString].append(string)
    return list(groupDict.values())

print(groupAnagram(strs))