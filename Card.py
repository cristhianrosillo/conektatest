import conekta

conekta.api_key = 'key_AbQS7grJpeu6hNTxmY5fBQ'

data = {
    "line_items": [{
          "name": "Unicorn",
          "unit_price": 57500,
          "quantity": 3
      }],
    
      "shipping_lines": [{
          "amount": 0,
          "carrier": "NULL"
      }],
    
      "currency": "MXN",
    
      "customer_info": {
       "customer_id": "cus_2hLRiYxabtaRMTCug"
      },
    
      "shipping_contact":{
       "phone": "+525555555555",
       "receiver": "Linus Torvalds",
       
       "address": {
         "street1": "### No name Street",
         "city": "Dunthorpe",
         "state": "Oregon",
         "country": "USA",
         "postal_code": "34198",
         }
       
     },

    "charges":[{
      "payment_method": {
        "type":"default"
      }
    }]
    
}

order = conekta.Order.create(data)

print ("Order No.: " + order.id)
print("Status: " + order.payment_status)
print("$ " + str(order.amount/100) + order.currency)
