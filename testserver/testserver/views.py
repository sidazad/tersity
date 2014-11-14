"""

@author Sid Azad

"""


from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json


def index(request):
    print "index"
    #signup_user(request)
    return render_to_response("base.html", {}, RequestContext(request))


def load_template(request):
    return render_to_response(request.GET.get("name"), {}, RequestContext(request))


def login_user(request):
    return HttpResponse(json.dumps({'status': 'ok'}), mimetype='application/json')