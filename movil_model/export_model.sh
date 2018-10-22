

INPUT_TYPE=image_tensor
PIPELINE_CONFIG_PATH=model/model.config
TRAINED_CKPT_PREFIX=model/model.ckpt-30
EXPORT_DIR=export

python ../models/research/object_detection/export_inference_graph.py \
    --input_type=${INPUT_TYPE} \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
    --output_directory=${EXPORT_DIR}