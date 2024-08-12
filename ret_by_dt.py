
from polars import col, read_parquet
from sys    import argv

PATH = "~/trading/daily/data/futc"

if __name__ == "__main__":

    dates   = open("./dates.txt").read().split("\n")
    sym     = argv[1]
    month   = argv[2]
    year    = argv[3]
    df      = read_parquet(f"{PATH}/{sym}.parquet")

    rows = df.filter(
        (col("month") == month) &
        (col("year") == year)
    ).rows()

    for i in range(len(rows)):

        row     = rows[i]
        date    = row[5]

        if date in dates:

            print(f"{date},{rows[i - 1][9]}")
