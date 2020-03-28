from rest_framework_json_api import serializers

from .models import ChatMessage


# here can refactor to pass the needed fields as a parameter
# and default to _all_ if parameter is not passed
# not relevant for the task
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
