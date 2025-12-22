from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactSerializer


@api_view(['POST'])
def contact_view(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        name = serializer.validated_data('name')
        email = serializer.validated_data('email')
        message = serializer.validated_data('message')

        try:
            send_mail(
                subject=f"New Contact Form Message",
                message=f"From: {name} ({email})\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return Response(
                {"message": "Your message has been sent"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Failed to send msessage. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
