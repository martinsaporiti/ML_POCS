export PROJECT=$(gcloud config list project --format "value(core.project)")
export YOUR_GCS_BUCKET="gs://${PROJECT}-ml"

# gsutil cp data/pet_train.record ${YOUR_GCS_BUCKET}/data/pet_train.record
# gsutil cp data/pet_val.record ${YOUR_GCS_BUCKET}/data/pet_val.record
# gsutil cp data/label.pbtxt \
#     ${YOUR_GCS_BUCKET}/data/label.pbtxt

# gsutil cp /Users/sapo/Development/workspace-python/faster_rcnn_resnet101_coco_2018_01_28/model.ckpt.* ${YOUR_GCS_BUCKET}/data/


# sed -i "s|PATH_TO_BE_CONFIGURED|"${YOUR_GCS_BUCKET}"/data|g" object_detection/samples/configs/faster_rcnn_resnet101_pets.config

gsutil cp model/model.config \
    ${YOUR_GCS_BUCKET}/data/model.config



# From model/research
# python setup.py sdist
# cd slim && python setup.py sdist

# # From tensorflow/models/research/
# bash object_detection/dataset_tools/create_pycocotools_package.sh /tmp/pycocotools
# python setup.py sdist
# cd slim && python setup.py sdist
# cd ../../../movil_model
# bash trainGCP.sh