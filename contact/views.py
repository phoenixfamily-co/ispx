from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response

from category.models import Category
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.
@cache_page(60 * 15)
def contact_view(request):
    template = loader.get_template('contract.html')
    category = Category.objects.all()
    context = {
        'category': category
    }

    return HttpResponse(template.render(context, request))


def email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # اگر از ModelForm استفاده می‌کنید
            # form.save()

            # اطلاعات فرم
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            file = request.FILES.get('file')

            # ارسال ایمیل
            email_subject = f"تماس از {name}"
            email_body = f"نام: {name}\nشماره تماس: {phone}\nایمیل: {email}\n\nپیام:\n{message}"

            email_message = EmailMessage(
                email_subject,
                email_body,
                'customer@iranianshiningphoenix.com',  # فرستنده
                ['your_email@example.com']  # گیرنده
            )

            # اضافه کردن فایل ضمیمه
            if file:
                email_message.attach(file.name, file.read(), file.content_type)

            email_message.send()

            return Response(status=status.HTTP_200_OK)
    else:
        ContactForm()

    return Response(status=status.HTTP_400_BAD_REQUEST)
