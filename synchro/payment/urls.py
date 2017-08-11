from django.conf.urls import url, include

from payment.views import StripePaymentView

urlpatterns = [
    url(r'^stripe?amount=(?P<amount>\S+)$',
        StripePaymentView.as_view(),
        name='stripe_payment',
        ),
]
