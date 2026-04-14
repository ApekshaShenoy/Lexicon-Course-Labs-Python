from azure.storage.blob import BlobServiceClient

connection_string = "CONNECTION_STRING"

container_name = "container"
file_path = "test.txt"
blob_name = "test.txt"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client(container_name)

with open(file_path, "rb") as data:
    container_client.upload_blob(name=blob_name, data=data, overwrite=True)

print("File uploaded successfully")