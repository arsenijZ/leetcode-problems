def longestCommonPrefix(strs) -> str:
        output = ""
        if strs[0] == "":
            return output
        elif len(strs) == 1:
            return strs[0]

        for index in range(0,len(min(strs))):
            print("index:", index)
            letter = strs[0][index]
            print("letter:", letter)
            for word in strs:
                print("word:", word)
                if letter != word[index]:
                    return output
            output+=letter
        return output

strs = ["ab", "a"]
print(longestCommonPrefix(strs))