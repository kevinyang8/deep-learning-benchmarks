# PT 1.11 E3 BERT Inference Benchmark

The `serve` directory is the `pytorch/serve` directory. Pulled here since we are using the BERT model from the `examples` directory there. There is code there to pull the model and create a `.mar` file for `torchserve`.

#### Stop and remove all containers
`docker stop $(docker ps -a -q)`
`docker rm $(docker ps -a -q)`

#### For credential setup
`aws ecr get-login-password --region us-west-2 | sudo docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-west-2.amazonaws.com`

#### Pull PT 1.11 E3 image
`sudo docker pull 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3` 

#### Run Docker Container
`sudo docker run --name benchmark_bert --gpus=all -v ~/deep-learning-benchmarks/inference/:/inference/ -it 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.11.0-gpu-py38-cu115-ubuntu20.04-e3 bash`

#### First step need to install HuggingFace Transformers 
`conda install -c huggingface transformers -y`

#### Clone pytorch/serve repo and download bert model
`git clone https://github.com/pytorch/serve.git`

`cd examples/Huggingface_Transformers`

`python Download_Transformer_models.py`

`torch-model-archiver --model-name BERTSeqClassification --version 1.0 --serialized-file Transformer_model/pytorch_model.bin --handler ./Transformer_handler_generalized.py --extra-files "Transformer_model/config.json,./setup_config.json,./Seq_classification_artifacts/index_to_name.json"`

#### Move model to model_store dir and start torchserve endpoint
`mkdir model_store`

`mv serve/examples/Huggingface_Transformers/BERTSeqClassification.mar model_store`

`mv serve/examples/Huggingface_Transformers/Seq_classification_artifacts/sample_text_captum_input.txt .`

`torchserve --start --model-store model_store --models my_tc=BERTSeqClassification.mar --ncs` 
