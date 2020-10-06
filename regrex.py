# test = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

def extractor(raw_data):
    
    refined_data = []
    for i in raw_data["orders"]:
        refined_data.append(i["id"])

    refined_data.append(raw_data["errors"][0]["code"])

    return refined_data

# print(extractor(test))