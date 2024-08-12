from util import get_continuous, r
from math import log


if __name__ == "__main__":

    es      = get_continuous("ES")
    dates   = [ rec[r.date] for rec in es ]
    settles = [ rec[r.settle] for rec in es ]
    logs    = [ log(settles[i] / settles[i - 1]) for i in range(1, len(settles)) ]
    dates   = dates[1:]

    print("date,change")

    for i in range(len(dates)):

        print(f"{dates[i]},{logs[i]}")

    pass