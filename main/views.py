from django.http import HttpResponseRedirect
from django.shortcuts import render

def Home(request):
    query = request.POST.get('query')
    request.session['query'] = query
    if request.method == 'POST':
        return HttpResponseRedirect("http://127.0.0.1:8000/results/")
    return render(request, "home.html")

def Results(request):
    return render(request, "results.html")
