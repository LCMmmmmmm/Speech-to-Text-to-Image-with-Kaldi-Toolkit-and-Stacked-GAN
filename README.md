# Speech-to-Text-to-Image-with-Kaldi-Toolkit-and-Stacked-GAN
The misc folder contains some functions which are used in the training process.

datasets.py, preprocess_birds.py and preprocess_flowers.py are used to preprocess the dataset. 

custom_ops.py contains the conv2d function, batch normalization function, eta, which are fine-tuned based on tensorflow's library function.

config.py contains some hyper parameters to train the model.

The stage1 folder is used to train the first stage GAN. 

model.py sets the model to be trained and trainer.py controls the training process.

cfg folder contains the hyper parameters used in the first stage.

The stage2 folder is used to train the second stage GAN. 

model.py sets the model to be trained and trainer.py controls the training process.

cfg folder contains the hyper parameters used in the second stage.

Before running the program, the image dataset needs to be downloaded and preprocessed in the Data folder, and the text dataset needs to be embedded by the text encoder in the models folder.

Command:

python stageI/run_exp.py --cfg stageI/cfg/birds.yml --gpu 0

python stageII/run_exp.py --cfg stageII/cfg/birds.yml --gpu 0


The program is based on Han Zhang's work.

https://github.com/hanzhanggit/StackGAN

@inproceedings{han2017stackgan,
Author = {Han Zhang and Tao Xu and Hongsheng Li and Shaoting Zhang and Xiaogang Wang and Xiaolei Huang and Dimitris Metaxas},
Title = {StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks},
Year = {2017},
booktitle = {{ICCV}},
}
