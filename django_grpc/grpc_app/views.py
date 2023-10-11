from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataStorage


class IOTReceiveAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(DataStorage.objects.all().values_list("iot_data", flat=True))

    def post(self, request, *args, **kwargs):
        DataStorage.objects.create(iot_data=request.data)
        return Response(request.data)

