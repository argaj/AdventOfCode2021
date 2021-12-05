def load(filename, data_type=None):
    with open(filename, 'r') as f:
        data = [line.rstrip('\n') for line in f]
    if data_type:
        return [data_type(x) for x in data]
    return data