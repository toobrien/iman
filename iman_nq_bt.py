from    bisect  import  bisect_left
from    util    import  get_dbn_df
from    time    import  time


def test(tp: float, sl: float):

    i       = 0
    n       = len(rows)
    total   = 0
    won     = 0

    while i < n:

        row = rows[i]
        ts  = row[0]

        if "06:30:00" not in ts:

            i += 1

            continue

        else:

            entry   = row[1]
            tp_     = entry + tp
            sl_     = entry - sl
            j       = i

            while j < n:

                cur     = rows[j]
                vals    = [ cur[1], cur[2], cur[3], cur[4] ]
                max_p   = max(vals)
                min_p   = min(vals) 

                if max_p >= tp_ or min_p >= tp_:

                    won     += 1
                    total   += 1
                    i       =  j + 1

                    break
                
                elif min_p <= sl_ or max_p <= sl_:

                    total   += 1
                    i       =  j + 1

                    break

                j += 1
    
    print(f"{tp:>10.2f}{sl:>10.2f}{total:>10.2f}{won:>10.2f}{total - won:>10.2f}{won / total:>10.2f}")


if __name__ == "__main__":

    t0      = time()
    rows    = get_dbn_df("NQ", "America/Los_Angeles").select([ "ts", "open", "high", "low", "close" ]).rows()
    ts      = [ row[0] for row in rows ]
    start   = bisect_left(ts, "2022-08-12T")
    rows    = rows[start:]
    
    print(f"\n{rows[0][0]} - {rows[-1][0]}\n")
    print(f"{'tp':>10}{'sl':>10}{'n trades':>10}{'wins':>10}{'losses':>10}{'win pct':>10}\n")
    
    test(40., 20.)
    test(17., 17.)

    print(f"\n{time() - t0:0.1f}s")