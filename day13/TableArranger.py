class TableArranger:

    def swap(input, i, j):
        temp = input[i]
        input[i] = input[j]
        input[j] = temp


    def permuteRecursive(input, index):
        if index == len(input):
            print ("".join(input))

        for i in range(index, len(input)):
            #print("".join(input))
            TableArranger.swap(input, index, i)
            TableArranger.permuteRecursive(input, i + 1)
            #TableArranger.swap(input, i, index)


    def findCombinations(input):
        TableArranger.permuteRecursive(list(input),0)

TableArranger.findCombinations("123")
