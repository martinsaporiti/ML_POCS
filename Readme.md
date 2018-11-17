# Repositorio con Pruebas de Conceptos de Machine Learning.

## Instalación de OpenCV y configuración del Virtualenv:

### 1. Instalar OpenCV.

```
brew install opencv
```

Instalar también las dependencias (pueden instalarse directamente en el virtual enviroment):

```
pip install numpy scipy scikit-image matplotlib scikit-learn
```


### 2. Crear el virtualenv

### 3. Crear un link a la instalación del OpenCV para poder utilizarlo desde el virtualenv:

Validar el path dado que contiene la versión de python y del SO

Parados en el path **${pwd}/cvtest/lib/python3.6/site-packages/** del virtual enviroment, vamos a crear un link a la instalación del opencv.


```
ln -S /usr/local/Cellar/opencv/3.4.3/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so cv2.so
```

### 4. Modelos de OpenCV

```
# Los modelos propios de OpenCV se encuentran en la carpeta:
/usr/local/Cellar/opencv/3.4.3/share/OpenCV/haarcascades
```


### 5. Instalar dlib

Necesitamos instalar CMake

```
brew install cmake
```
Luego instalamos dlib

```
git clone https://github.com/davisking/dlib.git

cd dlib
mkdir build; cd build; cmake ..; cmake --build .

cd ..
python3 setup.py install
```

El detalle en : https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf


### 6. Instalar face_recognition

```
pip3 install face_recognition
```

## Face Recogniton

https://github.com/ageitgey/face_recognition#installing-on-mac-or-linux



## How install Tensorflow Object Detection API

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
https://datasciencecampus.github.io/Installing-tensorflow-object-detection-API-notes/

```
git clone https://github.com/tensorflow/models.git
```
```
brew install protobuf
```

```
# From tensorflow/models/research/
protoc object_detection/protos/*.proto --python_out=.
```

```
# From tensorflow/models/research/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```
Testing:

```
python object_detection/builders/model_builder_test.py
```


### Models

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md


### Links de Interés


* [Models](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

* [Pipelines Config samples Files](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs)

* [Quick Start: Distributed Training on the Oxford-IIIT Pets Dataset on Google Cloud](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_pets.md)

* [Running on Google Cloud ML Engine](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_cloud.md)

* [Running Locally](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md)

* [Google Images Download](https://github.com/hardikvasa/google-images-download)
