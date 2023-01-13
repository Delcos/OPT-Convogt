#!/bin/bash

BASE_MODEL="hakurei/lit-125M"
DATASET="train-small.jsonl"
OUTPUT_DIR="models/convogpt-small"
EPOCHS=2
BATCH_SIZE=1
SAVE_STEPS=50
LEARNING_RATE=1e-5

accelerate launch src/training/sft.py \
    --model $BASE_MODEL \
    --dataset $DATASET \
    --output_dir $OUTPUT_DIR \
    --epochs $EPOCHS \
    --batch_size $BATCH_SIZE \
    --save_steps $SAVE_STEPS \
    --learning_rate $LEARNING_RATE