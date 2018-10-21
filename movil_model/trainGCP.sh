export PROJECT=$(gcloud config list project --format "value(core.project)")
export YOUR_GCS_BUCKET="gs://${PROJECT}-ml"

gcloud ml-engine jobs submit training `whoami`_object_detection_`date +%s` \
    --job-dir=${YOUR_GCS_BUCKET}/train \
    --packages=../models/research/dist/object_detection-0.1.tar.gz,/tmp/pycocotools/pycocotools-2.0.tar.gz,../models/research/slim/dist/slim-0.1.tar.gz \
    --module-name=object_detection.model_main \
    --config=config.yaml \
    -- \
    --pipeline_config_path=${YOUR_GCS_BUCKET}/data/model.config \
    --num_train_steps=100 \
    --model_dir=${YOUR_GCS_BUCKET}/train \
    --sample_1_of_n_eval_examples=1