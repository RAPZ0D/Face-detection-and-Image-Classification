# Face Detection and Image Classification


## Table of contents 
* [Getting Started](#Getting-Started) 
* [Prerequisites](#Prerequisites) 
* [Installation](#Installation)
* [Usage](#Usage)
* [Face Detection](#Face-Detection)
* [Image Classification](#Image-Classification)
* [Acknowledgments](#Acknowledgments)
* [Contributing](#Contributing)
* [Links](#Links)

### **This project uses machine learning techniques to perform two tasks:**.

1) **Face Detection:** This is a live Face Detection that uses your desktop/laptop camera and detects faces in the camera and displays the output. It uses OPENCV library to perform this Face Detection.

![FACE](https://user-images.githubusercontent.com/100001521/233773507-137f3680-69c6-460c-bd80-f559c57252dd.jpeg)


2) **Image Classification:** The Image Classification we have worked on detects weather the image provided is of a Happy person or a Sad Person. Given an input image, the program identifies what is depicted in the image by classifying it into one of several categories, it takes the image shape and breaks it down to a numpy array, then we do the same process to the dataset and train the neural network. Once this is completed we can read in a random image and it will detect weather the given person is Happy or Sad. The project is written in Python and utilizes several open-source libraries, including OpenCV, TensorFlow, and Keras. These libraries are commonly used in machine learning and computer vision applications.

![DOG CAT](https://user-images.githubusercontent.com/100001521/233773652-4651d914-48a8-489b-92fb-f3c602b22811.jpeg)


## Getting Started

### Prerequisites
Before you can use this program, you will need to install several software packages. Here's what you'll need:

**Python:** This program requires Python 3.x, which can be downloaded and installed from [Python](https://www.python.org/downloads/) official website. 

**OpenCV:** OpenCV is a computer vision library that is used for the Face Detection and Image Classification part this project. You can install OpenCV by running the following command in your terminal:

``` pip install opencv-python ```


![OpenCV](https://user-images.githubusercontent.com/100001521/233774150-e8f64546-99fe-4505-98b1-197172b70359.jpeg)


**TensorFlow:** TensorFlow is a machine learning library that is used for the image classification portion of this project. You can install TensorFlow by running the following command in your terminal:

``` pip install tensorflow ```

![TF](https://user-images.githubusercontent.com/100001521/233774204-25896e44-a21d-4c59-a681-914e478f9603.png)



**Keras:** Keras is a high-level neural networks API that is used for the image classification portion of this project, this library helps us build a Neural Network for Training. You can install Keras by running the following command in your terminal:

``` pip install keras ```

![KERAS](https://user-images.githubusercontent.com/100001521/233774286-17cc50a6-861a-4250-b898-d1a3015ea1f2.png)


## Installation
Once you have installed the required software packages, you can download and install this program. Here's how:

* Open a terminal window.
* Navigate to the directory where you want to install this program.
* Clone the repository by running the following command in your terminal:

``` git clone https://github.com/RAPZ0D/Face-detection-and-Image-Classification.git ```

**OR**

You can even download the **.zip** file directly from github itself and save it in your required folder, after that you can extract it there and get this whole code avaliable.

## Usage
There are two ways to use this program: face detection and image classification. Here's how to use each of them:

### Install required packages
``` pip install -r requirements.txt ```

### Face Detection
![FACES](https://user-images.githubusercontent.com/100001521/233774653-d2d64f06-84ad-4329-83e5-3a208d0f47eb.jpeg)
![MULTIPLE FACES](https://user-images.githubusercontent.com/100001521/233774658-0602f8d2-552c-445c-ac21-f89773d86677.jpeg)

To run face detection on a video stream, follow these steps:

* Navigate to the directory where you installed this program.
* Open a terminal window.
* Run the following command:

``` python main.py```

**This will start the program and open your computer's default camera. The program will detect faces in real-time and frame them with a rectangle.**

### Image Classification
![CLASS](https://user-images.githubusercontent.com/100001521/233774696-96187906-2b0a-4363-a80f-dfd79e6a9e66.jpeg)
![Deep learning](https://user-images.githubusercontent.com/100001521/233774801-649a602e-cace-49bc-a408-0cb1e8e6e44a.jpeg)
![TRAINING](https://user-images.githubusercontent.com/100001521/233774705-83fcf0a0-3005-4738-a480-55479b349c3d.png)

The image classification is program is completed in an **.ipynb file** so that means you don't need a terminal to run the code, you will only need the required libraries and the image data to run this program 
Make sure that you have saved the location of the data properly so that you can use it with ease. 
To run image classification on an input image, follow these steps:

* Open the Happy/Sad Detection.ipynb file 
* The whole program is completed with markdown and code
* Go through this code once so you can view the output and you can get an idea what is being done here
* Once you have viewed everything, now when you load the data from the local file or cloud based IDE make sure you load the data with the correct path 
* In the current program we have used **Google Colab** and imported **Google Drive** and then we have copied the path of the data and uploaded it.
* We highly recommend you to use Google Colab because it has built in **Tensorflow** and many other required libraries, it is not necessary to use Colab you can even use other IDE's such as **Jupyter Notebook**, **VSCode**, etc. but just remember to download the required libraries otherwise the code may not run 

``` Happy/Sad Detection.ipynb```


The program will analyze the input image and identify what is depicted in the image by classifying it into one of several categories.

### Acknowledgments
This program builds on the work of many other programmers and researchers in the fields of computer vision and machine learning. Specifically, the face detection portion of this program is based on the [OpenCV Face Detection tutorial](https://docs.opencv.org/3.4/df/d6c/tutorial_js_face_detection_camera.html) and the image classification portion is based on the [TensorFlow Image Classification tutorial](https://www.tensorflow.org/tutorials/images/classification). We would like to express our gratitude to all the developers and researchers who have contributed to the development and availability of these libraries, tutorials, and models. Without their hard work and dedication, this project would not have been possible.

### Contributing
We welcome contributions to this project from anyone interested in improving it. If you would like to contribute, please fork this repository and make your changes in a separate branch. Then, submit a pull request explaining the changes you've made and why they are valuable. We will review your changes and merge them if they meet our standards.

### Contact
If you have any questions or concerns about this project, please contact us at [Contributor 1 email address ](joel.mendonsa30@gmail.com) [Contributor 2 email address](iwuchukwu.johnpaul@gmail.com). We would be happy to hear any solutions, recommendations or any advices that you have.

### Links 
These are the links we are providing you from where we have started our research, our recommended github link from where we had the idea for this project and even the link for our dataset 
* ![Research Data link](https://arxiv.org/pdf/1710.07557v1.pdf)
* ![Github Repo link](https://github.com/oarriaga/face_classification)
* ![Image data link access](https://drive.google.com/drive/folders/14Xnyjp4x-Flj3qfSc-7oZtN9uZiBCMVX)

