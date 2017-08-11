from django.http import HttpResponseRedirect
from django.views import View

import stripe
import re


class StripePaymentView(View):

    def clean_amount(self, amount):
        # Regular expressions checking for a string with only digits and
        # an optional decimal point plus one or two more digits
        match = re.match(r'\d+(?:\.\d{1,2})?$', amount)

        # If the amountis valid it strips the decimal point
        if match:
            return int(amount.replace('.',''))
        else:
            return 0


    def post(self, request):

        # Testing Secret Key, replace with live key in production
        stripe.api_key = "sk_test_wS0FFI9b3H0MRN0MStur2u2Z"

        # Get the payment token ID submitted by the form:
        token = request.POST['stripeToken']

        # Get the amount from the url keywords

        # Charge the user's card:
        charge = stripe.Charge.create(
        amount=self.clean_amount(self.kwargs['amount'])
        currency="cad",
        description="Example charge",
        source=token,
        )

        return HttpResponseRedirect('/')
