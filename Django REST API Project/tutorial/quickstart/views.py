from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from django.contrib.auth.models import User, Group
from quickstart.models import userdata
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, UserdataSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from django.contrib.auth.decorators import login_required
# from quickstart.models import mongouserdata

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# @api_view(['GET','POST'])
# def user(self,request):
#     import pdb;pdb.set_trace()
#     if request.method == 'POST':
#     	serializer_class = UserdataSerializer
#     	serializer = self.serializer_class(data=request.data)
#     	if serializer.is_valid():
#     		serializer.save()
#     	else:
#     		return Response('Ok!')
#         # data = request.data
#         # if data != "":
#         #     uname = data.get('username')
#         #     return Response(uname)

#     if request.method == 'GET':
#         return Response('get method')  

class UserdataViewSet(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
    	import pdb;pdb.set_trace()
    	if request.method == 'POST':
    		serializer = self.serializer_class(data=request.data)
    		if serializer.is_valid():
    			serializer.save()
    			return Response(request.data,status=status.HTTP_200_OK)


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserListViewSet(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		queryset = User.objects.all()
		for user in queryset:
			serializer = UserSerializer(user)
			return Response(serializer.data, status=HTTP_200_OK)


class TestView(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		data = {'user':'test user'}
		return Response(data, status=HTTP_200_OK)