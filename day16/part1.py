def get_sues():
    sues = []
    f = open('input.txt','r')
    for line in f:
        words = line.split(" ")
        sues.append({"Sue" : words[1].strip(":"), words[2].strip(":") : int(words[3].strip(",")), words[4].strip(":") : int(words[5].strip(",")), words[6].strip(":") : int(words[7])})

    return sues

def remove_items(item_name, count, sues):
    for sue in sues:
        not_sues = [sues.index(s) for s in sues if (item_name in s) and s[item_name] != count]

    for not_sue in sorted(not_sues, reverse=True):
        del sues[not_sue]


#test_sues = [{"sue" : 1, "goldfish" : 2},{"sue" : 2, "goldfish" : 5}, {"sue" : 3}, {"sue" : 4, "goldfish" : 2}]
sues = get_sues()

remove_items("children", 3, sues)
remove_items("cats", 7, sues)
remove_items("samoyeds", 2, sues)
remove_items("pomeranians", 3, sues)
remove_items("akitas", 0, sues)
remove_items("vizslas", 0, sues)
remove_items("goldfish", 5, sues)
remove_items("trees", 3, sues)
remove_items("cars", 2, sues)
remove_items("perfumes", 1, sues)
print(sues)
