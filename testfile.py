import os
import file_utils
import storage_utils
import date_utils
from model_utils import check_or_download_model

# ---- automatically check download and extract model files/folders
fake_request_obj = {"filename":"model-sd-21.tar"}
check_or_download_model(fake_request_obj)

# ---- date operations
# date_utils.print_now_readable()

# ---- storage operations
# bucket_name = "grftech_models"
# file_name = "todos.tar"
# file_path = os.path.abspath(file_name)
# storageUtils.upload_to_gcs(bucket_name, file_name, file_path)
# storageUtils.download_from_gcs(bucket_name, file_name, file_path)

# ---- file operations
#zip and extract file
# fileUtils.zip("todos.txt","todos")
# fileUtils.extract("todos.tar","./")
#zip and extract folder
# fileUtils.zip("model","model-sd-21")
# fileUtils.extract("model-sd-21.tar","./")
# fileUtils.list_all_files_in_folder("./")

# ---- HF operations
# download a model and save its files locally
# import os
# from diffusers import StableDiffusionPipeline
# HF_AUTH_TOKEN = "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"
# save_dir = os.path.join("model")
# model = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5",use_auth_token=HF_AUTH_TOKEN)#.to("cuda")
# model.save_pretrained(save_dir)