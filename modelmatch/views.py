from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from approach.cal_match import find_match

def index(request):
    template = loader.get_template('modelmatch/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def calculator(request):
    template = loader.get_template('modelmatch/calculator.html')
    if request.method == "GET" and "arr_list" in request.GET:
        arr_list = list(map(lambda x: int(x), request.GET['arr_list'].replace(" ", "").split(",")))
        target = int(request.GET['target'])
        delta = int(request.GET['delta'])
        output = find_match(target, delta, arr_list)
        context = {
            'get': request.GET,
            'out': arr_list,
            'target': target,
            'delta': delta,
            'output': output,
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {}
        return HttpResponse(template.render(context, request))
