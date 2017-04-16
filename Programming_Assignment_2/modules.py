def filter(data, attr, value):
    results = []
    for datum in data:
        if datum[attr] == value:
            results.append(datum)
    return results
