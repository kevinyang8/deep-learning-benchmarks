import time
import numpy as np

def measure(f, a, model, loops, dph):
    times = [] # in milliseconds
    for i in range(loops):            
        startTime = time.time()
        f(*a)
        endTime = time.time()
        times.append((endTime - startTime) * 1000)

    print('----')
    print("latency in milliseconds")
    header = "model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour"
    hline  = "--------------|-------|-------|--------|------|--------|-------|---------|-------"
    md_format = "{} | {:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f} | {} | {:.2f} | {:.2f} "
    print(header)
    print(hline)
    p50 = np.percentile(times,50)
    mean = np.mean(times)
    k_inf_per_dollar = 3600/p50/float(dph) if dph else 0
    md_line = md_format.format(model,
        p50,
        np.percentile(times,99),
        np.percentile(times,100),
        np.percentile(times,0),        
        mean,
        len(times), k_inf_per_dollar, float(dph) if dph else 0)
    print(md_line)
    return {'p50': p50, 'mean': mean}

import argparse

def get_dph():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dph", help = "dollar per hour")
    args = parser.parse_args()
    if args.dph:
        print("dollar per hour: {}".format(args.dph))
    return args.dph