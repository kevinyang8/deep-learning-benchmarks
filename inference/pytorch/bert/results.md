# PT 1.11 E3 BERT Inference Benchmark Results

## c5.18xlarge

### 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3
```
latency in milliseconds
model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|--------|------|--------|-------|---------|-------
bert          | 67.01 | 211.27| 257.06 | 45.68| 85.52  | 100   | 17.56   | 3.06 
```

### pytorch/torchserve:0.5.2-cpu
```
latency in milliseconds
model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|--------|------|--------|-------|---------|-------
bert          | 55.73 | 370.41| 380.61 | 44.27| 88.28  | 100   | 21.11   | 3.06 
```

## g4dn.16xlarge 

### 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3
```
latency in milliseconds
model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|--------|------|--------|-------|---------|-------
bert          | 15.10 | 22.75 |  23.01 | 14.93| 15.73  | 100   | 54.79   | 4.35 
```

### pytorch/torchserve:0.5.2-gpu
```
latency in milliseconds
model         |  p50  |  p99  |  p100  |  p0  |  mean  | count | k-inf/$ | $/hour
--------------|-------|-------|--------|------|--------|-------|---------|-------
bert          | 15.09 | 26.93 | 27.01  | 14.54| 16.22  | 100   | 54.85   | 4.35 
```