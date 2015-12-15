class JsonCounter:

    def getTotalForObjectRecursive(jsonObject):
        total = 0
        if (type(jsonObject) is str):
            return 0

        if (type(jsonObject) is int) :
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


class JsonCounterNoRed:

    def getTotalForObjectNoRedRecursive(jsonObject):
        type(jsonObject)
        total = 0
        if (type(jsonObject) is str):
            return 0

        if (type(jsonObject) is int) :
            return jsonObject

        if (type(jsonObject) is dict):
            if ("red" in jsonObject.values()) :
                return 0
            for key in jsonObject:
                total += JsonCounterNoRed.getTotalForObjectNoRedRecursive(jsonObject[key])
            return total

        if (type(jsonObject) is list):
            for item in jsonObject:
                total += JsonCounterNoRed.getTotalForObjectNoRedRecursive(item)
            return total

    def getTotalForObjectNoRed(jsonObject):
        return JsonCounterNoRed.getTotalForObjectNoRedRecursive(jsonObject)
