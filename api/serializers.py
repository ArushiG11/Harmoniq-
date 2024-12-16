# In Django, a serializer is a component provided by the Django REST framework (DRF) that is used to convert complex data types, such as Django models, into native Python data types (like dictionaries), which can then be easily converted to JSON or other content types. It also handles the reverse process: validating and converting incoming JSON (or other formats) into Python objects that can be used in your application.

# Key Functions of a Serializer:
# Serialization: Converts Python objects (like Django model instances) into JSON or other formats for APIs.
# Deserialization: Converts JSON (or other formats) from API requests into Python objects, validating the data in the process.
# Validation: Ensures that incoming data adheres to specified rules before saving it to the database.
# Types of Serializers:
# Standard Serializer: A basic serializer for manually defining fields and validation.
# ModelSerializer: A shortcut serializer that automatically generates fields based on a Django model.


from rest_framework import serializers
from .models import Room # model we want to serialize

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields = ('id', 'code' ,'host' ,'guests_can_pause' ,'votes_to_skip', 'created_at')   # id is to set a Primary key that identify the model 