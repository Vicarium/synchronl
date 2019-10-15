from django.db import models
from django.shortcuts import render


from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

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
                                           default="Synchronized Swimming Payment",
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
            else:
                amount = self.clean_amount(context["page"].payment_amount)

            context["page"].payment_amount = amount

            if not amount:
                context["error_message"] = "Invalid Payment Amount."
            else:
                context["error_message"] = None

        return context


    def clean_amount(self, amount):
        """Takes a monetary amount and returns it as cents with no symbols.

        Returns either int or Null if amount string is invalid.
        """

        # Strip out "$" symbols from start and end of string
        amount = amount.strip("$")

        # Append cents if not present
        if "." not in amount:
            amount += ".00"

        # Check result for valid amount. More specifically use a
        # regular expression checking for a string with only digits and
        # an optional decimal point plus one or two more digits
        match = re.match(r'\d+(?:\.\d{1,2})?$', amount)

        # If the amountis valid it strips the decimal point
        if match:
            return int(amount.replace('.',''))
        else:
            return None


    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)

            if form.is_valid():

                # Get context
                context = self.get_context(request)

                # If theres an error render form page with error message
                if context['error_message']:

                    form = self.get_form(page=self, user=request.user)
                    context['form'] = form

                    return render(
                        request,
                        self.get_template(request),
                        context
                    )

                self.process_form_submission(form)

                # render the landing_page
                # TODO: It is much better to redirect to it
                return render(
                    request,
                    self.get_landing_page_template(request),
                    context,
                    )
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
        )
