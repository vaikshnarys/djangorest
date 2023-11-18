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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:

        model = Workservis
        fields = "__all__"

        #fields = ['kind','title','description','price','create_at','update_at','is_published','cat']

class CreateWorkservisSerializerOleg(serializers.Serializer):

    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.FloatField()

    def create(self, validated_data):
        return Workservis(**validated_data)

class UserSerializerOleg(serializers.Serializer):
    username = serializers.CharField()
    is_staff = serializers.BooleanField()

class CommentsSerializerOleg(serializers.Serializer):
    working_servis_id = serializers.IntegerField()
    text = serializers.CharField()
class WorkservisSerializerOleg(serializers.Serializer):

    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.FloatField()
    kind = serializers.CharField()
    user = UserSerializerOleg(many = False)
    comments = CommentsSerializerOleg(many=True)
    def create(self, validated_data):
        return super().create(**validated_data)
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance

class RetrieveWorkservisSerializerOleg(serializers.Serializer):
    kind = serializers.CharField(max_length=10, default='DRAFT')
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.FloatField()



    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.update_at = validated_data.get('update_at', instance.update_at)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat)
    #     instance.save()
    #     return instance

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

