from django.http import HttpResponse
from django.template import loader


def home(request):
    return HttpResponse("Aqui irá a home page da Kollins Tec.")

def comprar_match(request, jogo):
    template = loader.get_template("kollinstec/comprar_match.html")
    return HttpResponse(template.render({'jogo': jogo}, request))
