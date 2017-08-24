from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel

import re



class FormField(AbstractFormField):
    page = ParentalKey('PaymentPage', related_name='form_fields')


class PaymentPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    payment_amount = models.TextField(verbose_name='Payment Amount',
                                      blank=True,
                                      help_text='Optional: Used to set a required payment amount. Must use full amount with cents and no dollar sign, for example use 21.00 for $21 dollars.'
                                     )
    payment_description = models.TextField(verbose_name="Payment Description",
                                           blank=False,
                                           default="Synchro Online Payment",
                                           help_text='The payment description that will show up for the bill.'
                                          )

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('payment_amount'),
            FieldPanel('payment_description'),
        ], "Payment Information"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(PaymentPage, self).get_context(request, *args, **kwargs)

        # check if this is the form submission then cleans and sets page.payment_amount
        if request.method == 'POST':
            if not context["page"].payment_amount:
                amount = self.clean_amount(request.POST.get("payment-amount"))
                context["page"].payment_amount = amount
            else:
                amount = self.clean_amount(context["page"].payment_amount)
                context["page"].payment_amount = amount

        return context


    def clean_amount(self, amount):
        
        if "." not in amount:
            amount += ".00"

        # Regular expressions checking for a string with only digits and
        # an optional decimal point plus one or two more digits
        match = re.match(r'\d+(?:\.\d{1,2})?$', amount)

        # If the amountis valid it strips the decimal point
        if match:
            return int(amount.replace('.',''))
        else:
            return 0
