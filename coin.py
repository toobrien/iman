from    numpy                   import  arange, cumsum
import  plotly.graph_objects    as      go
from    random                  import  choices

if __name__ == "__main__":

    n = 1_000_000
    x = choices([1, -1], weights = [ 0.5, 0.5], k = n)

    y_cum = cumsum(x)
    y_avg = y_cum[1:] / arange(1, n)

    fig = go.Figure()

    traces = [
        ( y_avg, "average", "#FF00FF" ),
        ( y_cum, "total", "#0000FF")
    ]

    for trace in traces:
    
        fig.add_trace(
            go.Scattergl(
                {
                    "x":    [ i for i in range(n) ],
                    "y":    trace[0],
                    "name": trace[1],
                    "line": { "color": trace[2] } 

                }
            )
        )

    fig.show()