from django.conf import settings
import requests
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from orders.models import Order


def payment_process(request):
    # get order id from session
    order_id = request.session.get('order_id')
    # ger the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f"#{order.id} : {order.user.first_name}  {order.user.first_name}",
        'callback_url': '127.0.0.1:8000',
    }

    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
    # print('>>>  ',res.json()['data'])###برای مثال ممکنه در حالت واقعی متفاوت باشه#
# >>>   {'code':100, 'message':'Success', 'zarinpal_authority':'A00000000000000000000000000350631138', 'fee_type':'Merchant', 'fee':'15000'}

    data = res.json()['data']
    authority = data['zarinpal_authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse('Error from zarinpal')



