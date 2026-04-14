from django.http import JsonResponse
from .cosmos_service import CosmosService

def get_movies(request):
    service = CosmosService()
    movies = service.get_all_movies()

    cleaned_movies = []

    for m in movies:
        cleaned_movies.append({
            "id": m.get("id"),
            "title": m.get("title"),
            "genre": m.get("genre"),
            "reviews": m.get("reviews", [])
        })

    return JsonResponse(cleaned_movies, safe=False, json_dumps_params={"indent": 2})