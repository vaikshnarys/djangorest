import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Workservis

# class WorkservisModel:
#     def __init__(self,title,description):
#         self.title = title
#         self.description = description

class WorkservisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workservis
        fields = "__all__"
        #fields = ['kind','title','description','price','create_at','update_at','is_published','cat']

# class WorkservisSerializer(serializers.Serializer):
#
#     kind = serializers.CharField(max_length=10,default='DRAFT')
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     create_at = serializers.DateTimeField(read_only=True)
#     update_at = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Workservis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.update_at = validated_data.get('update_at', instance.update_at)
        instance.cat_id = validated_data.get('cat_id', instance.cat)
        instance.save()
        return instance

# def encode():
#     model = WorkservisModel('Washing machine', 'Content : Karcher')
#     model_sr =WorkservisSerializer(model)
#     print(model_sr.data, type(model_sr), sep = "\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Washing machine","description":"Content : Karcher"}')
#     data = JSONParser().parse(stream)
#     serializer = (WorkservisSerializer(data = data))
#     serializer.is_valid()
#     print(serializer.validate_data)

