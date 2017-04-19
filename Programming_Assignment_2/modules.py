def filter(data, attr, value):
    results = []
    for datum in data:
        if datum[attr] == value:
            results.append(datum)
    return results


def pure_check(data, attr):
    if len(data) != 0:
        value = data[0][attr]
        for datum in data:
            if datum[attr] != value:
                return None
        return value
    else:
        return None


