from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("comprar-match/<str:jogo>", views.comprar_match, name="comprar_match"),
    path("pagar/<str:tipo>/<str:nome>", views.pagar, name="pagamento"),
    path("processar-pagamento", views.payment_webhook, name="payment_webhook"),
]