import os
import file_utils
import storage_utils
from pathlib import Path

def check_or_download_model(request_json):
    
    # do nothing if model folder is already present
    if Path('model').is_dir():
        print("Model found")
        return

    # if file zip does not exist, then download it
    file_name = request_json['filename'] if request_json and 'filename' in request_json else "model-sd-21.tar"
    file_path = os.path.abspath(file_name)
    
    if not Path(file_name).exists():
        print("About to download model file: "+ file_name)
        bucket_name = "grftech_models"
        storage_utils.download_from_gcs(bucket_name, file_name, file_path)
    
    # if model folder does not exist, but model zip does, then extract
    if ".tar" in file_name: #skip extraction of ckpt files
        print("Extracting model file: "+ file_name)
        file_utils.extract(file_path,"./")
        file_utils.delete(file_path)
        