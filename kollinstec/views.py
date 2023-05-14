from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import stripe

# TODO 
# configuar keys via envvars
# refatorar o código

stripe.api_key = '...'

# dado pela Stripe CLI
webhook_secret = '...'

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
                    "unit_amount": 1500,  # R$ 15,00
                    "product_data": {
                        # buscamos no BD a partir de tipo e nome
                        "name": nome,
                        "description": tipo,
                    }
                },
                "quantity": 1,
            },
        ],
        metadata={
            "name": nome,
            "description": tipo,
        },
        mode="payment",
    )
    return HttpResponseRedirect(session.url)

@csrf_exempt
def payment_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'], expand=['line_items'])

        # Aqui processamos a venda
        print(session.metadata)

    return HttpResponse('de hoje tá pago')
