
### Instalación de OpenCV y configuración del Virtualenv:

#### 1. Instalar OpenCV.

#### 2. Crear el virtualenv

#### 3. Crear un link a la instalación del OpenCV para poder utilizarlo desde el virtualenv:

Validar el path dado que contiene la versión de python y del SO

Parados en el path **${pwd}/cvtest/lib/python3.6/site-packages/** del virtual enviroment, vamos a crear un link a la instalación del opencv.


```
ln -S /usr/local/Cellar/opencv/3.4.3/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so cv2.so
```

#### 4. Modelos de OpenCV

```
/usr/local/Cellar/opencv/3.4.3/share/OpenCV/haarcascades
```


#### 5. Instalar dlib

```
git clone https://github.com/davisking/dlib.git

cd dlib
mkdir build; cd build; cmake ..; cmake --build .

cd ..
python3 setup.py install
```

El detalle en : https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf


#### 6. Instalar face_recognition

```
pip3 install face_recognition
```

### Face Recogniton

https://github.com/ageitgey/face_recognition#installing-on-mac-or-linux



### How install Tensorflow Object Detection API

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



### Preparando los imputs

Ejecutar el siguiente comando para generar el archivo trainval.txt necesario para crear archivo tfrecord:

```
# From the tensorflow/models/ directory
ls images | grep ".jpg" | sed s/.jpg// > annotations/trainval.txt
```

Crar el archivo labelpb.txt. En este caso con el siguiente contenido:

```
item {
 id: 1
 name: 'batimovil'
},
item {
 id: 2
 name: 'toreto'
}
```

### Crear un archivo tfrcord

```
python /Users/sapo/Development/workspace-python/cvtest/models/research/object_detection/dataset_tools/create_pet_tf_record.py \
    --label_map_path=label.pbtxt \
    --data_dir=`pwd` \
    --output_dir=`pwd` \
```

```
/Users/sapo/Development/workspace-python/cvtest/models/research/object_detection/dataset_tools
```

https://mc.ai/a-complete-transfer-learning-toolchain-for-semantic-segmentation/


Se utilizó este archivo:

https://github.com/priya-dwivedi/Deep-Learning/blob/master/tensorflow_toy_detector/create_pet_tf_record.py

Se creó el archivo y se modificó.

```
# from movil_model/
python create_pet_tf_record.py 
```
Este script sirve si se utiliza con la estructura de carpetas de movil_model.
Si la estructura de carpetas cambia, se deben modificar las siguientes líneas del archivo:

```
flags.DEFINE_string('data_dir', '', 'Root directory to raw pet dataset.')
flags.DEFINE_string('output_dir', 'data', 'Path to directory to output TFRecords.')
flags.DEFINE_string('label_map_path', 'data/label.pbtxt',
                    'Path to label map proto')
```


python create_coco_tf_record.py \
    --train_annotations_file=instances.json \
    --train_image_dir=images \
    --output_path=model2




## Cómo entrenar un modelo localemente

1. Armar la estructura de directorios recomenda por la comunidad. 

```
+data
  -label_map file
  -train TFRecord file
  -eval TFRecord file
+models
  + model
    -pipeline config file
    +train
    +eval
```    

[Fuente](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md)


2. Seleccionar el model que será reeentrenado

(https://github.com/tensorflow/models/blob/477ed41e7e4e8a8443bc633846eb01e2182dc68a/object_detection/g3doc/detection_model_zoo.md)

3. Crear un archivo de configuración para el modelo. Tomar de ejemplo alguno de los que se presentan aqui:

[Pipelines Config samples Files](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs)

El detalle aquí:
[Configuring the Object Detection Training Pipeline](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md)

*Nota*: Modificar los valores y paths que correspondan
Buscar *PATH_TO_BE_CONFIGURED* y cambiarlo por el path que corresponda.

4. Poner a entrenar el modelo.

Podemos crear un archivo bash con el siguiente contenido:

```
export PIPELINE_CONFIG_PATH=movil_model/model/model.config
export MODEL_DIR=movil_model/model/
export NUM_TRAIN_STEPS=50000
export SAMPLE_1_OF_N_EVAL_EXAMPLES=1

python models/research/object_detection/model_main.py \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --model_dir=${MODEL_DIR} \
    --num_train_steps=${NUM_TRAIN_STEPS} \
    --sample_1_of_n_eval_examples=$SAMPLE_1_OF_N_EVAL_EXAMPLES \
    --alsologtostderr
```

5. Testear el modelo entrenado

[Quick Start: Jupyter notebook for off-the-shelf inference](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_notebook.md)


### Links de Interés


* [Models](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

* [Pipelines Config samples Files](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs)

* [Quick Start: Distributed Training on the Oxford-IIIT Pets Dataset on Google Cloud](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_pets.md)

* [Running on Google Cloud ML Engine](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_cloud.md)

* [Running Locally](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md)

* [Google Images Download](https://github.com/hardikvasa/google-images-download)