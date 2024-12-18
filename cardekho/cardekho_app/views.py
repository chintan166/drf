from django.shortcuts import render
from .models import Carlist,Showroomlist
from django.http import JsonResponse
from .api_file.serializers import CarSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class Showroom_View(APIView):
    
    def get(self,request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer= ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#def car_list_view(request):
 #   cars = Carlist.objects.all()
  #  data = {
   #     'cars':list(cars.values()),
   # }
   # return JsonResponse(data)

#def car_detail_view(request,pk):
 #   car = Carlist.objects.get(pk=pk)
  #  data = {
   #     'name':car.name,
    #    'description':car.description,
     #   'active':car.active,
    #}
    #return JsonResponse(data)
    
@api_view(['GET','POST'])
def car_list_view(request):
    if request.method == 'GET':    
        car = Carlist.objects.all()
        serializer = CarSerializer(car,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method == 'GET':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)