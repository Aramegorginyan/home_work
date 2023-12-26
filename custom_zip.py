def custom_zip(*iterables):
    result = []

    min_length = min(len(iterable) for iterable in iterables)

    for i in range(min_length):
        result.append(tuple(iterable[i] for iterable in iterables))

    return result

#print(list(zip([1,2],[4],[7,8,9])))
print(custom_zip([1,2,3],["a","b"],[5,2,3]))