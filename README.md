# -Automated-Visual-Pollution-Classification
This project aims to develop an automated visual pollution classification system using Convolutional Neural Networks (CNNs) and OpenCV. The system utilizes a large-scale dataset of street imagery taken from a moving vehicle to train and test algorithms for the detection and evaluation of various visual pollutants, such as graffiti, faded signage, potholes, and garbage.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
What things you need to install the software and how to install them:

Python 3.6 or higher
TensorFlow
OpenCV
Numpy
Matplotlib
Installing
A step by step series of examples that tell you how to get a development env running:

Clone the repository
git clone https://github.com/amosamasu/-Automated-Visual-Pollution-Classification

Install the required packages
pip install -r requirements.txt
Usage
Train the model:
python train.py --dataset path/to/dataset --model path/to/model
Test the model:
python test.py --model path/to/model --image path/to/image

