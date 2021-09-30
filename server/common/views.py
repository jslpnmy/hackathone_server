from .models import User, Message, SignLogin
from .serializers import UserSerializer, MessageSerializer, SignupSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EachUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageSend(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@api_view(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            snippet = SignLogin.objects.get()
        except SignLogin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SignupSerializer(snippet)
        return Response(serializer.data)
