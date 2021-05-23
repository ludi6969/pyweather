def __min_temp(data):
    ct = float(data[0][2])
    for i in data:
        tmp = float(i[2])
        if tmp < ct:
            ct = tmp
    return ct

def __min_df(data):
    cdf = float(data[0][3])
    for i in data:
        tmp = float(i[3])
        if tmp < cdf:
            cdf = tmp
    return cdf


def min(data):
    min_temp = __min_temp(data)
    min_df = __min_df(data)
    return (min_temp, min_df)

def __max_temp(data):
    ct = float(data[0][2])
    for i in data:
        tmp = float(i[2])
        if tmp > ct:
            ct = tmp
    return ct

def __max_df(data):
    cdf = float(data[0][3])
    for i in data:
        tmp = float(i[3])
        if tmp > cdf:
            cdf = tmp
    return cdf


def max(data):
    max_temp = __max_temp(data)
    max_df = __max_df(data)
    return (max_temp, max_df)

def __average_temp(data):
    a = 0
    for i in data:
        a += float(i[2])
    return a/len(data)

def __average_df(data):
    a = 0
    for i in data:
        a += float(i[3])
    return a/len(data)

def average(data):
    avg_temp = __average_temp(data)
    avg_df = __average_df(data)
    return (avg_temp, avg_df)

