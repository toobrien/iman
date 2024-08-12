from    math                    import  log
from    numpy                   import  mean, std
import  polars                  as      pl
import  plotly.graph_objects    as      go
from    sys                     import  argv


pl.Config.set_tbl_cols(-1)


if __name__ == "__main__":

    mode    = argv[1]

    df      = pl.read_csv("/Users/taylor/trading/databento/csvs/ES.c.0.csv")
    df      = df.with_columns(pl.col("ts_event").str.slice(0,19).str.replace(" ", "T").str.strptime(pl.Datetime, format = "%Y-%m-%dT%H:%M:%S"))
    df      = df.filter(
                (pl.col("ts_event").dt.hour() >= 19) &
                (pl.col("ts_event").dt.hour() <= 20)
            )
    df      = df.with_columns(pl.col("ts_event").dt.date().alias("date"))
    groups  = df.group_by([ "date" ], maintain_order = True)
    x       = []
    t       = []
    c_      = []

    for date, group in groups:

        o = group[0]["open"][0]
        c = group[-1]["close"][0]

        ret = log(c / o)

        t.append(str(date[0]))
        x.append(ret)
        c_.append(c)
    
    if mode == "hist":

        fig = go.Figure()

        fig.add_trace(
            go.Histogram(
                x = x
            )
        )

        mu      = mean(x)
        sigma   = std(x)

        print(f"mean:   {mu:0.4f}")
        print(f"stdev:  {sigma:0.4f}")

        for i in range(len(x)):

            z = (x[i] - mu) / sigma

            print(f'{t[i]:15}{x[i]:10.4f}{z:10.2f}')

        fig.show()

    elif mode == "reg":

        thresh  = 0.011816485813358531

        x       = x[:-1]
        t       = t[:-1]
        shift   = c_[1:]
        c_      = c_[:-1]
        y       = [ log(shift[i] / c_[i]) for i in range(len(c_)) ]

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                {
                    "x":    x,
                    "y":    y,
                    "mode": "markers",
                    "text": t
                }
            )
        )

        fig.show()

        selected = []

        for i in range(len(x)):

            if x[i] >= thresh:

                selected.append(y[i])
        
        pos = sum([ 1 for i in selected if i > 0])

        print(f"t_days: {len(x) + 1}")
        print(f"thresh: {thresh:0.4f}")
        print(f"pos:    {pos} / {len(selected)}")
        print(f"mu:     {mean(selected):0.4f}")
        print(f"sigma:  {std(selected):0.4f}")