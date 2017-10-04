from rest_framework import serializers
from basicapp.models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length = 50)
    # mymessage = serializers.CharField(max_length = 500)

    # def create(self,validated_data):
    #     return Messages.objects.create(**validated_data)


    # def update(self,instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.mymessage = validated_data.get('mymessage',instance.mymessage)
    #     instance.save()
    #     return instance
    class Meta:
        model = Messages
        fields =('id','name','mymessage')