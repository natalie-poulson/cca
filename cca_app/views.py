from django.shortcuts import render
import json
from django.http import JsonResponse

def api (request):
    # Open json file
    json_file = open('cca_app/data/cca_mock_courses.json')

    # Deserialize to a Python Object
    data = json.load(json_file)

    # send a JSON-encoded response
    return JsonResponse(data)