from rest_framework import serializers
from blogapp.models import Topic

class TopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields = ['id', 'title', 'description', 'text', 'date_created', 'date_modified' ]

