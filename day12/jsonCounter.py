class JsonCounter:
    #with open('input.json', encoding='utf-8') as data_file:
    #    data = json.loads(data_file.read())

#        print(data)

    def getTotalForObjectRecursive(jsonObject):
        total = 0
        if (type(jsonObject) is int) :
            print(jsonObject)
            return jsonObject

        if (type(jsonObject) is dict):
            for key in jsonObject:
                total += JsonCounter.getTotalForObjectRecursive(jsonObject[key])
            return total

        if (type(jsonObject) is list):
            for item in jsonObject:
                total += JsonCounter.getTotalForObjectRecursive(item)
            return total

    def getTotalForObject(jsonObject):
        return JsonCounter.getTotalForObjectRecursive(jsonObject)
