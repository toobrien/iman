import polars as pl

pl.Config.set_tbl_rows(-1)
pl.Config.set_tbl_cols(-1)


if __name__ == "__main__":

    df = pl.read_csv("./Performance.csv")

    print(df)
