import conekta

conekta.api_key = 'key_AbQS7grJpeu6hNTxmY5fBQ'

data = {

    "line_items": [{
      "name": "Concert Tickets",
      "unit_price": 139800,
      "quantity": 5
  }],
  "shipping_lines": [{
      "amount": 7500,
      "carrier": "Correos de Mexico"
  }],
  "currency": "MXN",
  "customer_info": {
    "name": "Ramiro Ramirez",
    "email": "r2@mail.com",
    "phone": "+5218181818181"
  },
  "shipping_contact":{
     "phone": "5555555555",
     "receiver": "Mama Lucha",
     "address": {
       "street1": "Guerrero Salvador 423",
       "city": "Cuadrada",
       "state": "Ciudad de Mexico",
       "country": "MX",
       "postal_code": "99999",
     }
   },
  "charges":[{
    "payment_method": {
      "type": "spei"
    }
  }]
    }

order = conekta.Order.create(data)

print ("Order No.: " + order.id)

