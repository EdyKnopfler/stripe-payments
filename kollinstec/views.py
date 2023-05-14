from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import stripe

stripe.api_key = 'sk_test_51N492lGdLPxaw6poID4phJ72YwG7ZoZtQkWVDBRVqG2ugBSTGwpSyDEXq1mnjb4wDlNRNK5gXrTBWrCHWGbgkibS00qudpJ3gM'

PAYMENT_LINK = 'https://buy.stripe.com/test_cN2bLsgUU8PP4PC144'


def home(request):
    return HttpResponse("Aqui irá a home page da Kollins Tec.")

def comprar_match(request, jogo):
    template = loader.get_template("kollinstec/comprar_match.html")
    return HttpResponse(
        template.render(
            {'jogo': {'nome': jogo, 'link_stripe': PAYMENT_LINK}},
            request))

def pagar(request, tipo, nome):
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price_data": {
                    "currency": "brl",
                    "unit_amount": 1500,  # em 1/100
                    "product_data": {
                        # buscamos no BD a partir de tipo e nome
                        "name": nome,
                        "description": tipo,
                    }
                },
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    return HttpResponseRedirect(session.url)

