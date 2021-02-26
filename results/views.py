from django.shortcuts import render


def Results(request):
    best_link = request.session.get('best_link')
    if request.method == 'GET':
        return render(request, "results.html", {"context": best_link})
