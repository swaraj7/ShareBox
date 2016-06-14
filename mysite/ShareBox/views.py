import httplib
import json
from django.http import HttpResponse
from ShareBox.models import Snippet
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
@csrf_exempt
def insert_db(request):
    output={}
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    name = body['snippet_name']
    privacy = body['snippet_privacy']
    expiry = body['snippet_expiry']
    snippet_data = body['snippet_file']
    new_snippet_box, created = Snippet.objects.get_or_create(
          snippet_name=name, snippet_privacy=privacy, snippet_expiry=expiry,
          snippet_file=snippet_data)
    new_snippet_box.save()
    url = "http://www/shareboxes.herokuapp.com/snippet/" + \
            str(new_snippet_box.id) + "/"
    output["url"] = url
    return HttpResponse(json.dumps(output),
                        content_type="application/json", status=201)


@require_http_methods(["GET", "DELETE"])
@csrf_exempt
def query_db(request, input_id):
    output = {}
    if request.method == "GET":
        try:
            output["snippet_file"] = Snippet.objects.get(
                id=input_id).snippet_file
            return HttpResponse(json.dumps(output),
                               content_type="application/json", status=200)
        except:
            output["snippet_file"] = "no snippet in database with give id , \
                    please check the url or the id provided at the end of url."
        return HttpResponse(json.dumps(output),
                            content_type="application/json", status=404)
    elif request.method == "DELETE":
        try:
            requested_file = Snippet.objects.get(id=input_id)
        except:
            output["status"] = " id is incorrect or snippet doesnot exists"
            return HttpResponse(json.dumps(output),
                                status=204)
        else:
            requested_file.delete()
            output["status"] = " file successfully deleted"
            return HttpResponse(json.dumps(output),
                                status=202)
