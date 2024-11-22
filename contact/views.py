from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from django.views.generic import FormView

from category.models import Category
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import ContactForm


# Create your views here.
@cache_page(60 * 15)
def contact_view(request):
    template = loader.get_template('contract.html')
    category = Category.objects.all()
    context = {
        'category': category
    }

    return HttpResponse(template.render(context, request))


class EmailView(APIView):
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.data, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            file = form.cleaned_data.get('file')

            email_subject = f"تماس از {name}"
            email_body = f"نام: {name}\nشماره تماس: {phone}\nایمیل: {email}\n\nپیام:\n{message}"

            email_message = EmailMessage(
                email_subject,
                email_body,
                'customer@iranianshiningphoenix.com',  # فرستنده
                ['ceo@iranianshiningphoenix.com']  # گیرنده
            )

            if file:
                email_message.attach(file.name, file.read(), file.content_type)

            email_message.send()

            return Response({"message": "ایمیل با موفقیت ارسال شد"}, status=200)

        return Response({"error": form.errors}, status=400)

