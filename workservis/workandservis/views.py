from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

from .filters import WorkservisCustomFilter
from .models import Workservis, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WorkservisSerializer,WorkservisSerializerOleg,CreateWorkservisSerializerOleg



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
    permission_classes = ( IsAuthenticatedOrReadOnly,)

class WorkservisUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Workservis.objects.all()
    serializer_class = WorkservisSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

class WorkservisCRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workservis.objects.all()
    serializer_class = WorkservisSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class WorkservisAPIView(APIView):
#     def get(self, request):
#         lst = Workservis.objects.all()
#         return Response({'list services' : WorkservisSerializer(lst, many = True).data})
#
#     def post(self,request):
#         serializer = WorkservisSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # servis_new = Workservis.objects.create(
#         #     title = request.data['title'],
#         #     description = request.data['description'],
#         #     price = request.data['price'],
#         #     cat_id = request.data['cat_id']
#
#         #)
#         return Response({'servis_new' : serializer.data})
#
#     def put(self,request,*args,**kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({"Error" : "Method PUT is not allowed"})
#
#         try:
#             instance = Workservis.objects.get(pk = pk)
#         except:
#             return Response({"Error": "Object does not exist"})
#
#         serializer = WorkservisSerializer(data = request.data,instance= instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'servis_update': serializer.data})
#
#     def delete(self,request,*args,**kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({"Error" : "Method DELETE is not allowed"})
#         try:
#             instance = Workservis.objects.get(pk=pk)
#         except:
#             return Response({"Error": "Object does not exist"})
#
#         instance = Workservis.objects.get(pk = pk)
#         instance.delete()
#         return Response({'servis_delete': 'delete_servis ' + instance.title })

class WorkservisSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 4

class DetailedWorkservisView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Workservis.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'working_service_id'

    def get_serializer_class(self):
        if self.request.method in ["GET","PATCH"]:
            return WorkservisSerializerOleg
        return CreateWorkservisSerializerOleg
class WorkservisViewSet(generics.ListCreateAPIView):
    queryset = Workservis.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, WorkservisCustomFilter]
    search_fields = ['^title', '^description']
    ordering_filters = ['title', 'description']
    ordering = ['title']
    pagination_class = WorkservisSetPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return WorkservisSerializerOleg
        return CreateWorkservisSerializerOleg


