export PIPELINE_CONFIG_PATH=model/model.config
export MODEL_DIR=model/
export NUM_TRAIN_STEPS=30
export SAMPLE_1_OF_N_EVAL_EXAMPLES=1

SECONDS=0

python ../models/research/object_detection/model_main.py \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --model_dir=${MODEL_DIR} \
    --num_train_steps=${NUM_TRAIN_STEPS} \
    --sample_1_of_n_eval_examples=$SAMPLE_1_OF_N_EVAL_EXAMPLES \
    --alsologtostderr

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
