

# Reentrenamiento de un modelo
Aquí las instrucciones para reentrenar un modelo agregando nuevas categorías.
Tener en cuenta que las imágenes de la carpeta *images* ya han sido procesadas para un tamaño más óptimo y se han generado los xml que describen los labels de las imágenes.

**Nota:** los archivos xml del folder *annotation/xmls* tienen en su interior el path de la imagen que describen. Esos paths no son tenidos en cuenta por el script create_pet_tf_record.py.

## 1. Generar el archivo trainval.txt
Para generar el arhivo se debe ejecutar lo siguiente:

```
ls images | grep ".JPEG" | sed s/.JPEG// > annotations/trainval.txt
```

## 2. Generar los arhivos TFR para el dataset
Tensorflow API wants the datasets to be in TFRecord file format.
Ejecutar entonces el script:

```
python create_pet_tf_record.py
```

Este script **funciona sin parámetros** para la esctructura que viene por defecto. Si la estructura es diferente, se deben editar las siguientes líneas del archivo *create_pet_tf_record.py*:

```
flags.DEFINE_string('data_dir', 'images', 'Root directory to raw pet dataset.')
flags.DEFINE_string('output_dir', 'data', 'Path to directory to output TFRecords.')
flags.DEFINE_string('label_map_path', 'data/label.pbtxt',
                    'Path to label map proto')
```

Al correr el script se deberían haber generado los archivos *pet_train.record* y *pet_val.record* dentro de la carpeta data. Estos archivos son los que luego utilizaremos para reentrenar el modelo.

## 3. Ahora si, a reentrenar (tarda mucho!)


Para poner a reentrenar el modelo, primero tenenos que:
* Seleccionar el modelo. [Link](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

* Elegir un archivo de configuración acorde a ese modelo. [Link](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs)

En este caso, elegí el modelo faster_rcnn_resnet101_coco_2018_01_28.
Modificamos el archivo de configuración seleccionado y lo colocamos en la carpeta model con el nombre model.config

En este archivo debemos modificar los paths que correspondan y el número de clases:

```
model {
  faster_rcnn {
    num_classes: 2
```


```
  fine_tune_checkpoint: "<SOME_PATH>/faster_rcnn_resnet101_coco_2018_01_28/model.ckpt"
```

```
  train_input_reader: {
  tf_record_input_reader {
    input_path: "data/pet_train.record*"
  }
  label_map_path: "data/label.pbtxt"
}
```

```
eval_input_reader: {
  tf_record_input_reader {
    input_path: "data/pet_val.record*"
  }
  label_map_path: "data/label.pbtxt"
  shuffle: false
  num_readers: 1
}
```

Antes de entrenar tener en cuenta lo siguiente:

**If you're using python3 , add list() to category_index.values() in model_lib.py about line 381 as this list(category_index.values()).**



Y ahora ejecutamos el archivo train.sh que contiene lo siguiente:

```
export PIPELINE_CONFIG_PATH=model/model.config
export MODEL_DIR=model/
export NUM_TRAIN_STEPS=10
export SAMPLE_1_OF_N_EVAL_EXAMPLES=1

python ../models/research/object_detection/model_main.py \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --model_dir=${MODEL_DIR} \
    --num_train_steps=${NUM_TRAIN_STEPS} \
    --sample_1_of_n_eval_examples=$SAMPLE_1_OF_N_EVAL_EXAMPLES \
    --alsologtostderr
```

Si fue todo bien, podemos analizar los resultados utilizando el tensorboard:

```
tensorboard --logdir=model 
```

### Otra opción es entrenarlo en la nube Google Cloud ML Engine


#### Links:

* [Running on Google Cloud ML Engine](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_cloud.md)

* [Quickstart for Debian and Ubuntu](https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu)

* [Buckets](https://cloud.google.com/storage/docs/creating-buckets)

* [getting-started-training-prediction](https://cloud.google.com/ml-engine/docs/tensorflow/getting-started-training-prediction)

* [Training an object detector using Cloud Machine Learning Engine](https://cloud.google.com/blog/products/gcp/training-an-object-detector-using-cloud-machine-learning-engine)

* Clave esto !!!:
[TensorFlow object detection training error with TPU](https://stackoverflow.com/questions/51430391/tensorflow-object-detection-training-error-with-tpu)


Ejecutar el archivo setupGCP.sh que contiene lo siguiente:

```
export PROJECT=$(gcloud config list project --format "value(core.project)")
export YOUR_GCS_BUCKET="gs://${PROJECT}-ml"

gsutil cp data/pet_train.record ${YOUR_GCS_BUCKET}/data/pet_train.record
gsutil cp data/pet_val.record ${YOUR_GCS_BUCKET}/data/pet_val.record
gsutil cp data/label.pbtxt \
    ${YOUR_GCS_BUCKET}/data/label.pbtxt

gsutil cp /Users/sapo/Development/workspace-python/faster_rcnn_resnet101_coco_2018_01_28/model.ckpt.* ${YOUR_GCS_BUCKET}/data/


<!-- # sed -i "s|PATH_TO_BE_CONFIGURED|"${YOUR_GCS_BUCKET}"/data|g" object_detection/samples/configs/faster_rcnn_resnet101_pets.config -->

Tener en cuenta los paths dentro de este archivo... hay que modificarlos para que corran en GCP.
gsutil cp model/model.config \
    ${YOUR_GCS_BUCKET}/data/model.config
```


```
# From tensorflow/models/research/
bash ../models/research/object_detection/dataset_tools/create_pycocotools_package.sh /tmp/pycocotools
python setup.py sdist
(cd slim && python setup.py sdist)
cd ../../../movil_model
bash trainGCP.sh
```

<hr>

## 4. Exportar el modelo.

Ejecutar el archivo **export_model.sh**. 
El archivo contiene el siguiente contenido:

```
INPUT_TYPE=image_tensor
PIPELINE_CONFIG_PATH=model/model.config
TRAINED_CKPT_PREFIX=model/model.ckpt-30
EXPORT_DIR=export

python ../models/research/object_detection/export_inference_graph.py \
    --input_type=${INPUT_TYPE} \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
    --output_directory=${EXPORT_DIR}
```
Notar que el parámetro *TRAINED_CKPT_PREFIX* debe tener el nombre del modelo (el último generado) y no un folder.


<hr>

## 5. Evaluación del modelo generado

Testear el modelo entrenado

[Quick Start: Jupyter notebook for off-the-shelf inference](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_notebook.md)
