class MemoryString :
    def countCharacters(stripped):
        # The input will be in quotes : "input"
        # The surrounding quotes are code characters only
        codeCharacters = 2
        memoryCharacters = 0

        # Examine the text between the quotes - look for escaped characters and ascii characters
        index = 1
        memoryString = ""
        while (index < len(stripped) -1):
            if (stripped[index] == "\\") :
                if (stripped[index+1] == "\\" or stripped[index+1] == "\""):
                    # is escaped \ or "
                    # this block takes up 2 code characers and 1 memory charater
                    memoryString += stripped[index+1]
                    memoryCharacters += 1
                    codeCharacters += 2
                    # skip to the end of the block
                    index += 2
                else :
                    # is ascii: \x{hex}{hex}
                    # this block takes up 4 code characers and 1 memory charater
                    memoryString += "'"
                    codeCharacters += 4
                    memoryCharacters += 1
                    # skip to the end of the block
                    index += 4
            else :
                # is regular character
                memoryString += stripped[index]
                memoryCharacters += 1
                codeCharacters +=1
                index += 1

        #print ("{s}{i} --> {m}{j}".format(s=stripped, m=memoryString, i=codeCharacters, j=memoryCharacters))
        return {'memoryCharacters' : memoryCharacters, 'codeCharacters' : codeCharacters}
