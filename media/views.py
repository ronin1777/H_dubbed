from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from media.models import MediaModel
from media.serializers import MediaSerializers
from movies.permisions import IsAdminOrReadOnly


# Create your views here.
class MediaCreateListView(ListCreateAPIView):
    queryset = MediaModel.objects.all()
    serializer_class = MediaSerializers
    permission_classes = [IsAdminOrReadOnly]


class MediaUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = MediaModel.objects.all()
    serializer_class = MediaSerializers
    permission_classes = [IsAdminOrReadOnly]
