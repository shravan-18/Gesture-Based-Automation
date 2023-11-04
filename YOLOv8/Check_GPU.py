import tensorflow as tf
import torch

print(torch.cuda.is_available())

gpus = tf.config.experimental.list_physical_devices("GPU")
if len(gpus) > 0:
    print("GPUs Available:")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPU available!")
