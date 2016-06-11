from django.http import HttpResponse
import requests
import httplib
import file_sender


def index(reques):
    return HttpResponse("this is an index page")


def send_data(request, snippet_data):
    not_empty = bool(snippet_data)
    if not_empty is False:
        raise "BucketEmptyError"
    else
        requests.post("http://www.shareboxes.herokuapp.com/share", data=snippet_data)
        retrun HttpResponse("Data Uploaded")
    
