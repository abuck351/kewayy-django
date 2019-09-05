from django.shortcuts import render


def index(request):
    context = {}
    context['name'] = 'Aaron'
    return render(request, 'kewayy_app/index.html', context)
