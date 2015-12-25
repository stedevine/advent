import string

def get_test_input():
    return list([{"start": "H", "end": "HO"}, {"start":"H", "end":"OH"},{"start":"O", "end":"HH"}])

def get_input():
    input = list()
    f = open('input.txt','r')
    for line in f:
        words = line.split(" => ")
        input.append({"start" : words[0], "end" : words[1].strip("\n")})

    return input

def store_distinct_molecules(index, molecule, replacementMap, distinctMolecules):
    elementToReplace = molecule[index]
    if (index < len(molecule) -1 and molecule[index+1] in string.ascii_lowercase):
        elementToReplace += molecule[index+1]

    print(elementToReplace)
    replacements = [x for x in replacementMap if x["start"] == elementToReplace]
    print(replacements)
    for r in replacements:
        # replace the element with the updated element
        molecule[index] = r["end"]
        if (len(elementToReplace) == 2):
            molecule[index+1] = ""
        updatedMolecule = "".join(molecule)
        if not updatedMolecule in distinctMolecules:
            distinctMolecules.append(updatedMolecule)
        #distinctMolecules.add("".join(molecule))

    #print(distinctMolecules)
    return len(distinctMolecules)

dm = list()
distinctMolecules = set()
replacementMap = get_input()
#print(replacementMap)
#print(replacementMap)


molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
#molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSi"
print(len(molecule))
for i in range(len(molecule)):
    store_distinct_molecules(i, list(molecule), replacementMap, dm)
print(len(dm))
#print(len(distinctMolecules))
