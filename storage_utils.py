from google.cloud import storage

default_project = "cryptic-now-370823"

def upload_to_gcs(bucket_name, file_name, file_path):
    # Initialize the client
    storage_client = storage.Client(project=default_project)
    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)
    # Create a new blob
    blob = bucket.blob(file_name)
    # Upload the file
    blob.upload_from_filename(file_path)
    print(f"File {file_name} has been uploaded to {bucket_name}.")
    
def download_from_gcs(bucket_name, file_name, file_path):
    # Initialize the client
    storage_client = storage.Client(project=default_project)
    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)
    # Create a new blob
    blob = bucket.blob(file_name)
    # Upload the file
    blob.download_to_filename(file_path)
    print(f"File {file_name} has been downloaded from {bucket_name}.")
