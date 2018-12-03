from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from pathlib import Path
from django.http import Http404


def api (request):
    try:
        file_path = Path('cca_app/data/cca_mock_courses.json')

        json_file = open(file_path)
        data = json.load(json_file)

    except FileNotFoundError:
        raise Http404("File does not exist")

    return JsonResponse(data)

    # if file_path.exists():
    #     json_file = open(file_path)
    #     # Deserialize to a Python Object
    #     data = json.load(json_file)
    #     # send a JSON-encoded response
    #     return JsonResponse(data)

    # else:
    #     return HttpResponse(status=500)