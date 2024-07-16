from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Items, Score
from .serializer import ItemModelSerializer, ScoreSerializer

class ListSerializerView(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemModelSerializer(items, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = ItemModelSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        items = Items.objects.all()
        serializer = ItemModelSerializer(items, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScoreView(APIView):
    def get(self, request):
        score = Score.objects.all()
        serializer = ScoreSerializer(score, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ScoreSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
