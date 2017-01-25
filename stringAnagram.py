def anagrams(stringArray):

    stringDict = {}
    for string in stringArray:
        stringDict[string] = ''.join(sorted(list(set(string))))

    uniqLetterGrp = {}
    for _, uniqueLetters in stringDict.items():
        if uniqueLetters not in uniqLetterGrp:
            uniqLetterGrp[uniqueLetters] = 1
        else:
            uniqLetterGrp[uniqueLetters] += 1

    return max(uniqLetterGrp.values())

if __name__ == "__main__":
    testArray = ['cats','caller','dogs','cellar','parrots','recall']
    testArray = ['disease','burned','viewer','praised','despair','burden', \
                'diapers','review']
    testArray = ['dogs','cats','chicken']
    print anagrams(testArray)
