from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from advertisements.models import Advertisement


class AdvertisementStatusView(APIView):
    def post(self, request, *args, **kwargs):
        advertisement = get_object_or_404(Advertisement, pk=kwargs['pk'])
        advertisement.status = 'accepted'
        advertisement.save()

        return Response("success")

    def delete(self, request, *args, **kwargs):
        print(request.data)
        advertisement = get_object_or_404(Advertisement, pk=kwargs['pk'])
        advertisement.status = 'reject'
        advertisement.save()

        return Response("success")


