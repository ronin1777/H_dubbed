from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from bucket import bucket
from media.models import MediaModel
from media.serializers import MediaSerializers
from movies.permisions import IsAdminOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BucketObjectSerializer
from .tasks import delete_object_task, download_object_task


class MediaCreateListView(ListCreateAPIView):
    queryset = MediaModel.objects.all()
    serializer_class = MediaSerializers
    permission_classes = [IsAdminOrReadOnly]


class MediaUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = MediaModel.objects.all()
    serializer_class = MediaSerializers
    permission_classes = [IsAdminOrReadOnly]


class BucketHome(APIView):
    def get(self, request):
        objects = bucket.get_objects()
        serializer = MediaSerializers(objects, many=True)
        return Response(serializer.data)


class DeleteBucketObject(APIView):
    def get(self, request, key):
        delete_object_task.delay(key)
        return Response(status=status.HTTP_202_ACCEPTED)


class DownloadBucketObject(APIView):
    def get(self, request, key):
        download_object_task.delay(key)
        return Response(status=status.HTTP_202_ACCEPTED)
