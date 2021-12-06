from django.http.response import HttpResponseBadRequest, HttpResponseBase
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.

# AUTHORIZE RAZORPAY CLIENTS WITH API KEYS
razorpay_client = razorpay.Client(
    auth=("KEY ID", "KEY SECRET"))


def index(request):
    currency = 'INR'
    amount = 10000

    # CREATE A RAZORPAY ORDER FROM SERVER SIDE
    razorpay_order = razorpay_client.order.create(
        dict(amount=amount, currency=currency, payment_capture='0'))

    # ORDER ID OF NEWLY CREATED ORDER
    razorpay_order_id = razorpay_order['id']

    # CONTEXT DATA TO PASS THE DETAILS TO FRONTEND
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': 'KEY ID',
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': 'paymenthandler/',
    }

    return render(request, 'index.html', context=context)

# CSRF EXEMPT DECORATOR IS NEEDED BECAUSE POST REQUEST WILL BE MADE BY RAZORPAY


@csrf_exempt
def paymenthandler(request):

    if request.method == 'POST':

        try:

            # GET THE REQUIRED PARAMETERS FROM POST REQUEST
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            }

            # VERIFY THE PAYMENT SIGNATURE
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)

            if result is None:

                amount = 10000

                try:

                    # CAPTURE THE PAYMENT
                    razorpay_client.payment.capture(payment_id, amount)

                    # RENDER SUCCESS PAGE
                    return render(request, 'success.html')

                except:

                    # IF THERE IS AN ERROR WHILE CAPTURING THE PAYMENT
                    return render(request, 'failure.html')

            else:

                # IF SIGNATURE VERIFICATION FAILS
                return render(request, 'failure.html')

        except:

            # IF WE DONT FIND THE PARAMETERS IN POST REQUEST
            return HttpResponseBadRequest()

    else:

        # IF OTHER THAN POST REQUEST IS MADE
        return HttpResponseBadRequest()
