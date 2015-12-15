class JsonCounter:
    #with open('input.json', encoding='utf-8') as data_file:
    #    data = json.loads(data_file.read())

#        print(data)

    def getTotalForObjectRecursive(jsonObject):
        print(type(jsonObject))
        total = 0
        if (type(jsonObject) is int) :
            print(jsonObject)
            return jsonObject

        if (type(jsonObject) is str):
            return 0    

        if (type(jsonObject) is dict):
            #print(jsonObject)
            for key in jsonObject:
                total += JsonCounter.getTotalForObjectRecursive(jsonObject[key])
            return total

        if (type(jsonObject) is list):
            #print(jsonObject)
            for item in jsonObject:
                total += JsonCounter.getTotalForObjectRecursive(item)
            return total

    def getTotalForObject(jsonObject):
        return JsonCounter.getTotalForObjectRecursive(jsonObject)
