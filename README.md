# Face Detection and Image Classification


## Table of contents 
* [Getting Started](#Getting-Started) 
* [Prerequisites](#Prerequisites) 
* [Installation](#Installation)
* [Usage](#Usage)
* [Image Classification](#Image-Classification)
* [Acknowledgments](#Acknowledgments)
* [Contributing](#Contributing)

### **This project uses machine learning techniques to perform two tasks:**.

1) Face Detection: Given an input image or video stream, the program detects faces in the image and frames them with a rectangle.
2) Image Classification: Given an input image, the program identifies what is depicted in the image by classifying it into one of several categories.
The project is written in Python and utilizes several open-source libraries, including OpenCV, TensorFlow, and Keras. These libraries are commonly used in machine learning and computer vision applications.

## Getting Started

### Prerequisites
Before you can use this program, you will need to install several software packages. Here's what you'll need:

**Python:** This program requires Python 3.x, which can be downloaded and installed from [Python](https://www.python.org/downloads/) official website. 

**OpenCV:** OpenCV is a computer vision library that is used for the face detection portion of this project. You can install OpenCV by running the following command in your terminal:

``` pip install opencv-python-headless ```

**TensorFlow:** TensorFlow is a machine learning library that is used for the image classification portion of this project. You can install TensorFlow by running the following command in your terminal:

``` pip install tensorflow ```

**Keras:** Keras is a high-level neural networks API that is used for the image classification portion of this project. You can install Keras by running the following command in your terminal:

``` pip install keras ```

## Installation
Once you have installed the required software packages, you can download and install this program. Here's how:

* Open a terminal window.
* Navigate to the directory where you want to install this program.
* Clone the repository by running the following command in your terminal:

``` git clone https://github.com/RAPZ0D/Face-detection-and-Image-Classification.git ```

## Usage
There are two ways to use this program: face detection and image classification. Here's how to use each of them:

### Install required packages
``` pip install -r requirements.txt ```

### Face Detection
To run face detection on an input image, follow these steps:

* Navigate to the directory where you installed this program.
* Open a terminal window.
* Run the following command:

``` python face_detection.py --image path/to/image.jpg ```

Replace **path/to/image.jpg** with the path to the image you want to analyze.


To run face detection on a video stream, follow these steps:

* Navigate to the directory where you installed this program.
* Open a terminal window.
* Run the following command:

``` python face_detection.py ```

**This will start the program and open your computer's default camera. The program will detect faces in real-time and frame them with a rectangle.**

### Image Classification
To run image classification on an input image, follow these steps:

* Navigate to the directory where you installed this program.
* Open a terminal window.
* Run the following command:

``` python image_classification.py --image path/to/image.jpg ```

Replace **path/to/image.jpg** with the path to the image you want to analyze.

The program will analyze the input image and identify what is depicted in the image by classifying it into one of several categories.

### Acknowledgments
This program builds on the work of many other programmers and researchers in the fields of computer vision and machine learning. Specifically, the face detection portion of this program is based on the [OpenCV Face Detection tutorial](https://docs.opencv.org/3.4/df/d6c/tutorial_js_face_detection_camera.html) and the image classification portion is based on the [TensorFlow Image Classification tutorial](https://www.tensorflow.org/tutorials/images/classification). We would like to express our gratitude to all the developers and researchers who have contributed to the development and availability of these libraries, tutorials, and models. Without their hard work and dedication, this project would not have been possible.

### Contributing
We welcome contributions to this project from anyone interested in improving it. If you would like to contribute, please fork this repository and make your changes in a separate branch. Then, submit a pull request explaining the changes you've made and why they are valuable. We will review your changes and merge them if they meet our standards.

### Contact
If you have any questions or concerns about this project, please contact us at [email address]. We would be happy to hear from you.
