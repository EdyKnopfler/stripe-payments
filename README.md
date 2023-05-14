# Teste de pagamentos com Stripe

Projeto usando API e CLI do gateway de pagamento Stripe. Simula seleção de produto pela URL e checkout.

Usamos a [CLI do Stripe](https://stripe.com/docs/stripe-cli?locale=pt-BR) para monitorar os pagamentos e acionar os webhooks localmente.

Requer a configuração de uma conta no Stripe no modo de teste. Neste teste suas chaves de acesso devem ser informadas em `kollinstec/views.py`:
* `stripe.api_key`: use a chave gerada para o modo de testes
* `webhook_secret`: para redirecionamento local a CLI irá lhe dar uma chave; ou informe a chave da sua configuração de webhook

## Pacotes de sistema

```bash
sudo apt-get install python3-dev libmysqlclient-dev
```

## Construir e rodar

```bash
docker compose build
docker compose up -d
```

## Monitorar pagamentos e acionar o webhook localmente

Aqui você terá a chave para preencher a variável `webhook_secret`.

```bash
stripe listen --forward-to localhost:8000/processar-pagamento
```

## Simulando uma compra

Acesse `http://localhost:8000/comprar-match/<qualquer nome ou id>`

Ex.: <http://localhost:8000/comprar-match/fifa2023>

Clique no belíssimo link de pagamento que o redirecionará para a página de checkout do Stripe. Na volta, o webhook deverá printar no terminal os metadados do jogo:

```json
{
   "description": "jogo",
   "name": "fifa2023"
}
