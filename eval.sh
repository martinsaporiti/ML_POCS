# From the tensorflow/models/ directory
python models/research/object_detection/legacy/eval.py \
    --logtostderr \
    --pipeline_config_path=movil_model/models/model/model.config \
    --checkpoint_dir=movil_model/models/model/ \
    --eval_dir=movil_model/models/model/evals