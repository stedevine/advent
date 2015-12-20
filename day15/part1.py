total_tea_spoons = 100

def test_combinations():
    combinations=[]
    for i in range (1, total_tea_spoons-1):
        for j in range (1, total_tea_spoons-1):
            if (i + j == total_tea_spoons):
                        #print ("{i} + {j} + {k} + {l}".format(i=i, j=j, k=k, l=l))
                combinations.append({"i":i, "j":j})
    return combinations


def possible_combinations():
    combinations=[]
    for i in range (1, total_tea_spoons-1):
        for j in range (1, total_tea_spoons-1):
            for k in range (1, total_tea_spoons-1):
                for l in range (1, total_tea_spoons-1):
                    if (i + j + k  + l == total_tea_spoons):
                        #print ("{i} + {j} + {k} + {l}".format(i=i, j=j, k=k, l=l))
                        combinations.append({"i":i, "j":j, "k":k, "l":l})
    return combinations

def get_ingredients():
    ingredients = []
    f = open('input.txt','r')
    for line in f:
        words = line.split(" ")
        ingredients.append({"name" : words[0].strip(":"), "cap" : int(words[2].strip(",")), "dur":int(words[4].strip(",")), "fla": int(words[6].strip(",")), "tex": int(words[8].strip(","))})

    return ingredients

def get_properties(combination, ingredients):
    total_cap = (combination["i"] * ingredients[0]["cap"]) + (combination["j"] * ingredients[1]["cap"]) + (combination["k"] * ingredients[2]["cap"]) + (combination["l"] * ingredients[3]["cap"])
    total_dur = (combination["i"] * ingredients[0]["dur"]) + (combination["j"] * ingredients[1]["dur"]) + (combination["k"] * ingredients[2]["dur"]) + (combination["l"] * ingredients[3]["dur"])
    total_fla = (combination["i"] * ingredients[0]["fla"]) + (combination["j"] * ingredients[1]["fla"]) + (combination["k"] * ingredients[2]["fla"]) + (combination["l"] * ingredients[3]["fla"])
    total_tex = (combination["i"] * ingredients[0]["tex"]) + (combination["j"] * ingredients[1]["tex"]) + (combination["k"] * ingredients[2]["tex"]) + (combination["l"] * ingredients[3]["tex"])
    #print(total_cap)
    #print(total_dur)
    #print(total_fla)
    #print(total_tex)
    #print (total_cap * total_dur * total_fla * total_tex)
    return max(0,total_cap) * max(0,total_dur) * max(0,total_fla) * max(0,total_tex)

max_score = 0
ingredients = get_ingredients()
#print(ingredients)
combinations=possible_combinations()
#print (combinations)
for combination in combinations:
    print("{c} {s}".format(c=combination,s=get_properties(combination, ingredients)))
    max_score= max(max_score, get_properties(combination, ingredients))
    #get_properties({"i" : 44, "j" : 56}, ingredients)

print(max_score)
#combinations=possible_combinations()
#print(combinations)
