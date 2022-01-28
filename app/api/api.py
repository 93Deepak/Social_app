from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from .serializers import *

__all__ = ['RegisterUser', 'UserView', 'StatusView']

class RegisterUser(CreateAPIView):
    queryset           = User.objects.all()
    serializer         = RegisterSerializer
    permission_classes = [AllowAny]


class UserView(APIView):
    permission_classes     = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    
    def get(self, request):
        obj        = User.objects.get(id=request.user.id)
        follow     = User.objects.exclude(id__in=[request.user.id]+[i.id for i in obj.following.all()])
        unfollow   = User.objects.filter(id__in=[i.id for i in obj.following.all()])
        not_follow = UserSerializer(follow, many=True)
        following  = UserSerializer(unfollow, many=True)
        
        return Response({'following':following.data, 'Not Following':not_follow.data}, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        if request.data.get('action').lower() == 'follow':
            if request.data.get('id') is not None:
                obj = User.objects.get(id=request.user.id)
                try:
                    followed_user = User.objects.get(id=request.data['id'])
                except:
                    return Response({'Not Found':f"User with id {request.data['id']} Not Found"},
                                    status=status.HTTP_404_NOT_FOUND)
                
                obj.following.add(followed_user)
                followed_user.followed_by.add(obj)
                obj.save()
                followed_user.save()
                
                return Response({'OK': f"You are now Following {followed_user.username}"}, status=status.HTTP_200_OK)
            
            return Response({'Error':'Please Enter User id to follow user'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        elif request.data.get('action').lower() == 'unfollow':
            if request.data.get('id') is not None:
                obj = User.objects.get(id=request.user.id)
                try:
                    followed_user = User.objects.get(id=request.data['id'])
                except:
                    return Response({'Not Found':f"User with id {request.data['id']} Not Found"},
                                    status=status.HTTP_404_NOT_FOUND)
                
                obj.following.remove(followed_user)
                followed_user.followed_by.remove(obj)
                obj.save()
                followed_user.save()
                
                return Response({'OK': f"You Have Un-Followed {followed_user.username}"}, status=status.HTTP_202_ACCEPTED)
            
            return Response({'Error':'Please Enter User id to follow user'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'Error':'Please Specify an action Keyword, follow or unfollow'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
    
class StatusView(APIView):
    permission_classes     = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    
    def get(self, request):
        obj        = User.objects.get(id=request.user.id)
        status     = Status.objects.filter(created_by__in=[request.user.id]+[i.id for i in obj.following.all()])
        serializer = StatusGETSerializer(status, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        data = request.data
        data._mutable = True
        data['created_by'] = request.user.id
        serializer = StatusPOSTSerializer(data=data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        