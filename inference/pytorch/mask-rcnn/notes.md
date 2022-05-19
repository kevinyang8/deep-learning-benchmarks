# PT 1.11 E3 Mask-RCNN Inference Benchmark

The `serve` directory is the `pytorch/serve` directory. Pulled here since we are using the Mask-RCNN model from the `examples` directory there. There is code there to pull the model and create a `.mar` file for `torchserve`.

#### Stop and remove all containers
`docker stop $(docker ps -a -q)`

`docker rm $(docker ps -a -q)`

#### For credential setup
`aws ecr get-login-password --region us-west-2 | sudo docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-west-2.amazonaws.com`

#### Pull PT 1.11 E3 image
`sudo docker pull 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3` 

`sudo docker pull 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3`

#### Run Docker Container for serving 
`sudo docker run --name benchmark_server --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3 bash`

`sudo docker run --name benchmark_server --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it pytorch/torchserve:0.5.2-gpu bash`

`sudo docker run --name benchmark_server --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3 bash`

#### Clone pytorch/serve repo and download Mask-RCNN model
`git clone https://github.com/pytorch/serve.git`

`wget https://download.pytorch.org/models/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth`

`torch-model-archiver --model-name maskrcnn --version 1.0 --model-file serve/examples/object_detector/maskrcnn/model.py --serialized-file maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth --handler object_detector --extra-files serve/examples/object_detector/index_to_name.json`

`mkdir model_store`

`mv maskrcnn.mar model_store/`

`mv serve/examples/object_detector/persons.jpg .`

`torchserve --start --model-store model_store --models maskrcnn=maskrcnn.mar`

#### Run Docker Container for invoking endpoint
`sudo docker run --name benchmark_client --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3 bash`

`sudo docker run --name benchmark_client --gpus=all --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it pytorch/torchserve:0.5.2-gpu bash`

`sudo docker run --name benchmark_client --network=host -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-cpu-py38-ubuntu20.04-e3 bash`

#### Perform inference
`python measure_inference.py --dph <dollar-per-hour>`
