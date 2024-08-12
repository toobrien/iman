import  plotly.graph_objects    as      go
from    numpy                   import  cumsum
from    numpy.random            import  normal
from    random                  import  randint
from    sys                     import  argv


if __name__ == "__main__":

    mode            = argv[1]
    years           = 4
    n               = 256 * years
    n_jumps         = 4 * years
    sigma           = 0.0050
    jump_sigma      = 0.0400
    jumps           = cumsum(normal(loc = 0, scale = jump_sigma, size = n_jumps))
    jump_locations  = sorted([ randint(0, n - 1) for _ in range(n_jumps) ])
    noise           = cumsum(normal(loc = 0, scale = sigma, size = n))
    value           = [ 0 ] * n
    x               = [ i for i in range(n) ]
    fig             = go.Figure()
    prev            = jump_locations[0]

    for i in range(n_jumps):

        for j in range(prev, jump_locations[i]):

            value[j] = jumps[i]
        
        prev = jump_locations[i]

    for i in range(jump_locations[i], n):

        value[i] = jumps[-1]

    if mode == "A":

        noise = noise + value

    elif mode == "B":

        for location in jump_locations:

            noise[location:] -= (noise[location] - value[location])

        pass

    traces = [
        ( noise, "price", "#0000FF" ),
        ( value, "value", "#FF00FF" )
    ]

    for trace in traces:

        fig.add_trace(
            go.Scatter(
                {
                    "x":    x,
                    "y":    trace[0],
                    "name": trace[1],
                    "mode": "lines",
                    "line": { "color": trace[2] }
                }
            )
        )

    fig.show()
