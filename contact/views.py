from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from .serializers import ContactSerializer
from django.core.mail import EmailMessage
from IranianShiningPhoenix import settings
from .models import ContactInfo


# Create your views here.
@cache_page(60 * 15)
def contract_view(request):
    template = loader.get_template('contract.html')
    context = {}

    return HttpResponse(template.render(context, request))


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        # id = serializer.validated_data['id']
        name = serializer.validated_data['name']
        number = serializer.validated_data['number']
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']
        file = serializer.validated_data.get('file', None)

        email_subject = f"New Service Request from {name}"
        email_body = f"Name: {name}\nNumber: {number}\nEmail: {email}\nMessage:\n{message}"

        email_message = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.COMPANY_EMAIL],
        )
        if file:
            email_message.attach(file.name, file.read(), file.content_type)
        email_message.send()
        return contact

    def create(self, request, *args, **kwargs):
        # Handle file in the request data if any
        if 'file' in request.data:
            request.data['file'] = request.FILES.get('file')

        return super().create(request, *args, **kwargs)

    def perform_update(self, serializer):
        contact = serializer.save()

        # id = serializer.validated_data['id']
        name = serializer.validated_data.get('name', contact.name)
        number = serializer.validated_data.get('number', contact.number)
        email = serializer.validated_data.get('email', contact.email)
        message = serializer.validated_data.get('message', contact.message)
        file = serializer.validated_data.get('file', None)

        email_subject = f"Update contact(:{name}) previous information."
        email_body = f"Name: {name}\nNumber: {number}\nEmail: {email}\nMessage:\n{message}"

        email_message = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.COMPANY_EMAIL],
        )
        if file:
            email_message.attach(file.name, file.read(), file.content_type)
        email_message.send()
        return contact

    def update(self, request, *args, **kwargs):
        # Handle file in the request data if any
        if 'file' in request.data:
            request.data['file'] = request.FILES.get('file')

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if 'file' in request.data:
            request.data['file'] = request.FILES.get('file')

        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
