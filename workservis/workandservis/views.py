from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Workservis
from .serializers import WorkservisSerializer


# class WorkservisAPIView(generics.ListAPIView):
#     queryset = Workservis.objects.all()
#     serializer_class = WorkservisSerializer

# class WorkservisAPIView(APIView):
#     def get(self, request):
#         lst = Workservis.objects.all().values()
#         return Response({'list services' : list(lst)})
#
#     def post(self,request):
#         servis_new = Workservis.objects.create(
#             title = request.data['title'],
#             description = request.data['description'],
#             price = request.data['price'],
#             cat_id = request.data['cat_id']
#
#         )
#         return Response({'servis_new' : model_to_dict(servis_new)})
class WorkservisListAPI(generics.ListCreateAPIView):
    queryset = Workservis.objects.all()
    serializer_class = WorkservisSerializer

class WorkservisUpdateAPI(generics.UpdateAPIView):
    queryset = Workservis.objects.all()
    serializer_class = WorkservisSerializer

class WorkservisCRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workservis.objects.all()
    serializer_class = WorkservisSerializer
class WorkservisAPIView(APIView):
    def get(self, request):
        lst = Workservis.objects.all()
        return Response({'list services' : WorkservisSerializer(lst, many = True).data})

    def post(self,request):
        serializer = WorkservisSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # servis_new = Workservis.objects.create(
        #     title = request.data['title'],
        #     description = request.data['description'],
        #     price = request.data['price'],
        #     cat_id = request.data['cat_id']

        #)
        return Response({'servis_new' : serializer.data})

    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({"Error" : "Method PUT is not allowed"})

        try:
            instance = Workservis.objects.get(pk = pk)
        except:
            return Response({"Error": "Object does not exist"})

        serializer = WorkservisSerializer(data = request.data,instance= instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'servis_update': serializer.data})

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({"Error" : "Method DELETE is not allowed"})
        try:
            instance = Workservis.objects.get(pk=pk)
        except:
            return Response({"Error": "Object does not exist"})

        instance = Workservis.objects.get(pk = pk)
        instance.delete()
        return Response({'servis_delete': 'delete_servis ' + instance.title })