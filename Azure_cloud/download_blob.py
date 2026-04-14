from azure.storage.blob import BlobServiceClient

connection_string = "CONNECTION_STRING"

container_name = "container"
blob_name = "test.txt"          
download_file = "downloaded_test.txt"   

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(download_file, "wb") as file:
    data = blob_client.download_blob()
    file.write(data.readall())

print("Download successful")