from rest_framework import generics
from .serializers import ContactSerializer
from django.core.mail import EmailMessage
# from django.conf import settings
from IranianShiningPhoenix import settings
from rest_framework.response import Response
from rest_framework import status
from .models import ContactInfo


# Create your views here.

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

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
