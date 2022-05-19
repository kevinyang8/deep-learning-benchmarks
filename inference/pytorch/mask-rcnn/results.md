# PT 1.11 E3 Mask-RCNN Inference Benchmark Results

## c5.18xlarge

### 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3
```
model         |  p50  |  p99  |  p100 |  p0   |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|-------|-------|--------|-------|---------|-------
mask-rcnn     |1326.94|1527.41|1822.91|1165.04| 1338.53| 100   | 0.89    | 3.06 
```

### pytorch/torchserve:0.5.2-cpu
```
latency in milliseconds
model         |  p50  |  p99  |  p100 |  p0   |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|-------|-------|--------|-------|---------|-------
mask-rcnn     |1223.62|1402.57|1502.68|1048.12| 1222.64| 100   | 0.96    | 3.06 
```

## g4dn.16xlarge 

### 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3
```
latency in milliseconds
model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|--------|------|--------|-------|---------|-------
mask-rcnn     | 135.21| 138.20| 143.21 |132.51| 135.14 | 100   | 6.12    | 4.35 
```

### pytorch/torchserve:0.5.2-gpu
```
latency in milliseconds
model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|--------|------|--------|-------|---------|-------
mask-rcnn     | 145.54| 147.85| 149.48 |143.74| 145.62 | 100   | 5.69    | 4.35 
```