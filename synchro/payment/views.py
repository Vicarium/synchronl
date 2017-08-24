from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            return None


    def post(self, request, payment_amount):

        # Testing Secret Key, replace with live key in production
        stripe.api_key = "sk_live_Bh53yf5cTyWc4whGyczJyGUt"

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
            context = {'error_text': charge_result[1].message}
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

            except stripe.CardError as ce:
                # charge failed
                return False, ce

            return True, response
