from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.conf import settings

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
            return None


    def post(self, request, payment_amount):

        synchronl_api_key = settings.SYNCHRONL_API_KEY
        summit_api_key = settings.SUMMIT_API_KEY

        # Set which api key to use
        site_title = request.POST['site_title']

        if site_title == "Summit Synchro":
            stripe.api_key = summit_api_key
        else:
            stripe.api_key = synchronl_api_key


        # Get the payment token ID submitted by the form:
        token = request.POST['stripeToken']

        # Get payment description from form
        description = request.POST.get('payment_description', 'Synchro online payment')

        # Get and clean the amount from the url keywords
        cleaned_amount = self.clean_amount(payment_amount)


        # Charge with the gathered information and get a result tuple
        charge_result = self.charge(
            price_in_cents=cleaned_amount,
            payment_description=description,
            stripe_token = token
        )

        if charge_result[0]:
            context = {'thank_you_text': request.POST['thank_you_text']}
            return render(request, 'payment/payment_page_success.html', context)
        else:
            print("render error")
            context = {'error_message': charge_result[1]._message}
            return render(request, 'payment/payment_error_page.html', context)


    def charge(self, price_in_cents, payment_description, stripe_token):
            """
            Takes a the price and credit card details: number, exp_month,
            exp_year, cvc.

            Returns a tuple: (Boolean, Class) where the boolean is if
            the charge was successful, and the class is response (or error)
            instance.
            """

            try:
                response = stripe.Charge.create(
                    amount=price_in_cents,
                    currency="cad",
                    description=payment_description,
                    source=stripe_token,
                )

            except stripe.StripeError as se:
                # charge failed
                return False, se

            return True, response
