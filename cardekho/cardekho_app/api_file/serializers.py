from rest_framework import serializers
from ..models import Carlist,Showroomlist

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroomlist
        fields = "__all__"
    

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carlist
        fields = "__all__"
    
    
    def validate_price(self,value):
        if value <= 2000.00:
            raise serializers.ValidationError("price must be greater than 2000")
        return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description must be diffrent")
        if data['name'] == data['chassisnumber']:
            raise serializers.ValidationError("name and chassisnumber must be diffrent")
        if data['price'] == data['chassisnumber']:
            raise serializers.ValidationError("price and chassisnumber must be diffrent")
        return data