from django.http import HttpResponse
from ShareBox.models import Snippet
from django.views.decorators.csrf import csrf_exempt
import requests
import httplib
import json

@csrf_exempt
def insert_db(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['snippet_name']
        privacy = body['snippet_privacy']
        expiry = body['snippet_expiry']
        snippet_data = body['snippet_file']
        new_snippet_box , created = Snippet.objects.get_or_create(snippet_name=name, snippet_privacy=privacy, snippet_expiry=expiry, snippet_file=snippet_data)
        new_snippet_box.save()
        output = {}
        url = "http://www/shareboxes.herokuapp.com/snippet/id/" + str(new_snippet_box.id)
        output["url"] = url
        print url
    return HttpResponse(json.dumps(output))

def query_db(request, input_id):
    if request.method == "GET":
        output = {}
        try:
            output["snippet_file"] = Snippet.objects.get(id=input_id).snippet_file
        except:
            output["snippet_file"] = "no snippet in database with give id , please check the url or the id provided at the end of url."
        return HttpResponse(json.dumps(output))


