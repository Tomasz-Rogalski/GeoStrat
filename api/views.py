from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TopicSerializer

from blogapp.models import Topic

def api(request):
  return render(request, 'api/api.html')

@api_view(['GET'])
def get_topics(request):
  topics = Topic.objects.filter(confirmed=True)
  serializer = TopicSerializer(topics, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_topic(request, topic_id):
  topic = Topic.objects.get(id= topic_id)
  serializer = TopicSerializer(topic, many=False)
  return Response(serializer.data)

# @api_view(['POST'])
# def add_topic(request):
#   serializer = TopicSerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#   return Response(serializer.data)
