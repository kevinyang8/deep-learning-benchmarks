# PT 1.11 E3 BERT Inference Benchmark

The `serve` directory is the `pytorch/serve` directory. Pulled here since we are using the BERT model from the `examples` directory there. There is code there to pull the model and create a `.mar` file for `torchserve`.

#### For credential setup
`aws ecr get-login-password --region us-west-2 | sudo docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-west-2.amazonaws.com`

#### Pull PT 1.11 E3 image
`sudo docker pull 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3` 
