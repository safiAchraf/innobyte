from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from .models import user , room , tasks  , reservation
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group
import json


@api_view(('GET','POST'))
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        full_name = data["name"]
        email = data["email"]
        password = data["password"]
        number = data["number"]
        if password == "" or email == "" or full_name == "" or number == "" :
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data= {
                "message": "All fields are required."
            })
        
        try:
            newuser = user.objects.create_user(email , password, full_name = full_name, staff = False)
            newuser.save()
        except IntegrityError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                "message": "Email address already taken."
            })
       
        refresh = RefreshToken.for_user(newuser)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response(status=status.HTTP_201_CREATED, data= {
            "message": "User created successfully.",
            "access_token": access_token,
            "refresh_token": refresh_token
        })
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST , data= {
            "message": "POST request required."
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def getuser(request):
    if request.method == "GET":
        return Response(status=status.HTTP_200_OK, data= {
            "user": {
                "id": request.user.id,
                "full_name": request.user.full_name,
                "email": request.user.email,
                "phone_number": request.user.phone_number,
                
            }
        })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST , data= {
            "message": "GET request required."
        })
    

@api_view(('GET','POST'))
@permission_classes([IsAuthenticated])
@csrf_exempt
def reservation(request , room_id):
    if request.method == "POST":
        data = json.loads(request.body)
        start_date = data["start_date"]
        end_date = data["end_date"]
        
        if start_date == "" or end_date == "" :
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data= {
                "message": "All fields are required."
            })
        try:
            """check if there is available rooms with room_type in the given period
            if there is available rooms then reserve one of them
            else return error"""
            
            available_room = room.filter(room_number = room_id)
            if not available_room:
                return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                    "message": "No available rooms."
                })
            available_room[0].available = False
            newuser = user.objects.get(id = request.user.id)
            newuser.reservation_set.create(start_date = start_date , end_date = end_date , room_id = room_id)
            newuser.save()
            available_room[0].save()

        except IntegrityError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                "message": "Error in reservation."
            })
        
        
        return Response(status=status.HTTP_200_OK, data= {
            "message": "Room reserved successfully."
        })



@api_view(('GET','POST'))
@permission_classes([IsAuthenticated])
def tasks(request):
    if request.method == "POST" and request.user.is_superuser:
        data = json.loads(request.body)
        title = data["title"]
        description = data["description"]
        if title == "" or description == "":
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data= {
                "message": "All fields are required."
            })
        try:
            newtask = tasks.objects.create(title = title , description = description)
            newtask.save()
        except IntegrityError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                "message": "Error in creating task."
            })
        
        
        return Response(status=status.HTTP_200_OK, data= {
            "message": "Task created successfully."
        })
    elif request.method == "GET":
        if request.user.is_superuser and request.user.staff:
            tasks = tasks.objects.all()
            return Response(status=status.HTTP_200_OK, data= {
                "tasks": tasks
            })

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data= {
                "message": "Unauthorized."
            })
        
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST , data= {
            "message": "POST or GET request required."
        })

@api_view(('GET','POST'))
@permission_classes([IsAuthenticated])
def create_staff_user(request):
    if request.method == "POST" and request.user.is_superuser:
        data = json.loads(request.body)
        full_name = data["name"]
        email = data["email"]
        password = data["password"]
        number = data["number"]
        if password == "" or email == "" or full_name == "" or number == "" :
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data= {
                "message": "All fields are required."
            })
        
        try:
            newuser = user.objects.create_user(email , password, full_name = full_name, staff = True)
            newuser.save()
        except IntegrityError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                "message": "Email address already taken."
            })
       
        refresh = RefreshToken.for_user(newuser)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response(status=status.HTTP_201_CREATED, data= {
            "message": "User created successfully.",
            "access_token": access_token,
            "refresh_token": refresh_token
        })
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST , data= {
            "message": "POST request required."
        })
    
@api_view(('GET','POST'))
@permission_classes([IsAuthenticated])
def rooms(request):
    if request.user.is_superuser:
        if request.method == "POST":
            data = json.loads(request.body)
            capacity = data["capacity"]
            price = data["price"]
            summary = data["summary"]
            room_number = data["room_number"]
            sea_view = data["sea_view"]
            balcony = data["balcony"]
            available = data["available"]
            suite = data["suite"]
            
            if type == "" or capacity == "" or price == "" or summary == "" or room_number == "":
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data= {
                    "message": "All fields are required."
                })
            
            try:
                newroom = room.objects.create( capacity = capacity , price = price , summary = summary , room_number = room_number , sea_view = sea_view , balcony = balcony , available = available , suite = suite)
                newroom.save()
            except IntegrityError as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                    "message": "Error in creating room."
                })
            
            
            return Response(status=status.HTTP_200_OK, data= {
                "message": "Room created successfully."
            })
        elif request.method == "GET":
            rooms = room.objects.all()
            return Response(status=status.HTTP_200_OK, data= {
                "rooms": rooms
            })
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED , data= {
                "message": "Unauthorized."
            })

            


@api_view(('GET','POST'))
@permission_classes([IsAuthenticated])
def oneRoom(request , room_id):
    if request.user.is_superuser:
        if request.method == "DELETE":
            try:
                room.objects.get(id = room_id).delete()
            except IntegrityError as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                    "message": "Error in deleting room."
                })
            
            
            return Response(status=status.HTTP_200_OK, data= {
                "message": "Room deleted successfully."
            })
        elif request.method == "PUT":
            data = json.loads(request.body)
            type = data["type"]
            capacity = data["capacity"]
            price = data["price"]
            summary = data["summary"]
            room_number = data["room_number"]
            if type == "" or capacity == "" or price == "" or summary == "" or room_number == "":
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data= {
                    "message": "All fields are required."
                })
            
            try:
                room.objects.get(id = room_id).update(type = type , capacity = capacity , price = price , summary = summary , room_number = room_number)
            except IntegrityError as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data= {
                    "message": "Error in updating room."
                })
            
            
            return Response(status=status.HTTP_200_OK, data= {
                "message": "Room updated successfully."
            })
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST , data= {
                "message": "Bad request."
            })

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED , data= {
                "message": "Unauthorized."
            })
    
