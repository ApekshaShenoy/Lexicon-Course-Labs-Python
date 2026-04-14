from azure.cosmos import CosmosClient

URI = "YOUR_URI"
KEY = "YOUR_KEY"

DATABASE_NAME = "MoviesDB"
CONTAINER_NAME = "movies"

class CosmosService:
    def __init__(self):
        client = CosmosClient(URI, credential=KEY)
        self.database = client.get_database_client(DATABASE_NAME)
        self.container = self.database.get_container_client(CONTAINER_NAME)

    def get_all_movies(self):
        return list(self.container.read_all_items())

    def add_movie(self, movie_data):
        return self.container.create_item(body=movie_data)