def __min_temp(data):
    ct = float(data[0][2])
    r = data[0]
    for i in data:
        tmp = float(i[2])
        if tmp < ct:
            ct = tmp
            r = i
    return r

def __min_df(data):
    cdf = float(data[0][3])
    r = data[0]
    for i in data:
        tmp = float(i[3])
        if tmp < cdf:
            cdf = tmp
            r = i
    return r


def min(data):
    min_temp = __min_temp(data)
    min_df = __min_df(data)
    return (min_temp, min_df)

from database import Db

db = Db('./db.db')
db.insert('10.1', '50')
db.insert('100.1', '0')
data = db.getAll()
# print(data)
print(min(data))