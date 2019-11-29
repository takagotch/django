from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('Hello, World!')

def board_topics(request, pk):
  board = Board.objects.get(pk=pk)
  return(request, 'topics.html', {'board': board})



