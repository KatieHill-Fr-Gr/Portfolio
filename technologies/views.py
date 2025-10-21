from rest_framework.generics import ListCreateAPIView
from .models import Technology
from .serializers.common import TechnologySerializer

class TechnologiesListView(ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer