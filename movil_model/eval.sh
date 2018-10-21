

python r../models/research/object_detection/eval.py \
    --logtostderr \
    --pipeline_config_path=model/model.config \
    --checkpoint_dir=model \
    --eval_dir=eval

