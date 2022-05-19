# PT 1.11 E3 SSD Inference Benchmark

#### Stop and remove all containers
`docker stop $(docker ps -a -q)`

`docker rm $(docker ps -a -q)`

#### For credential setup
`aws ecr get-login-password --region us-west-2 | sudo docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-west-2.amazonaws.com`

#### Pull PT 1.11 E3 image
`sudo docker pull 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3` 

`sudo docker pull 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3`

### Run Docker Container for model preparation
`sudo docker run --name model_prepare --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3 bash`

### Setup model
`pip install scikit-image`

`python prepare_model.py`

`torch-model-archiver --model-name ssd --version 1.0 --serialized-file ssd.pt --handler object_detector`

`mkdir model_store`

`mv ssd.mar model_store/`

#### Run Docker Container for serving 
`sudo docker run --name benchmark_server --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3 bash`

`sudo docker run --name benchmark_server --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3 bash`

`torchserve --start --model-store model_store --models my_tc=ssd.mar --ncs`

#### Run Docker Container for invoking endpoint
`sudo docker run --name benchmark_client --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3 bash`

`sudo docker run --name benchmark_client --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3 bash`

#### Perform inference
`python measure_inference.py --dph <dollar-per-hour>`
