from .models import Emp
from rest_framework import serializers,viewsets

class EmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields = '__all__'

class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer