import conekta

conekta.api_key = 'key_AbQS7grJpeu6hNTxmY5fBQ'

data = {
      "line_items": [
          {
              "name": "Item 1",
              "description": "Imported From Mex.",
              "unit_price": 215200,
              "quantity": 3,
              "sku": "item_1",
              "category": "other",
              "type" : "physical",
              "tags" : ["test"]
          }
      ],
      "shipping_lines":[
        {
          "amount": 0,
          "tracking_number": "Track ##",
          "carrier": "Amazon Services",
          "method": "Bicycle",
          "metadata": {
             "random_key": "random_value"
          }
        }],
      "customer_info":{
          "name": "Lady Wu",
          "phone": "+528164726351",
          "email": "ladyWu@mail.fun",
          "corporate": False,
          "vertical_info": {}
        },
      "shipping_contact":{
          "phone" : "+528164726352",
          "receiver": "Elton Jhon",
          "between_streets": "Other Street",
          "address": {
              "street1": "742 Evergreen Terrace",
              "state": "Springfield",
              "country": "US",
              "postal_code": "23912",
              "metadata":{ "soft_validations": True}
          }
      },
      "fiscal_entity":{
        "tax_id": "LWU092378721",
        "name": "Nike SA de CV",
        "address": {
            "street1": "250 Alexis St",
            "internal_number": "19",
            "external_number": "91",
            "city": "Red Deer",
            "state": "Alberta",
            "country": "CA",
            "postal_code": "33242"
        }
      },
      "charges": [{
        "payment_method":{
          "type":"oxxo_cash"
        },
        "amount": 645600
      }],
      "currency" : "mxn",
      "metadata" : {"test" : "extra info"}
    }

order = conekta.Order.create(data)

print (order.id)
