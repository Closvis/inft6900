from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WalkingCountSurvey, BicycleCountSurvey, CarShareUsage


# API for walking count surveys
@api_view(['GET'])
def get_walking_data(request):
    data = WalkingCountSurvey.objects.all().values()
    return Response(data)


# API for bicycle count surveys
@api_view(['GET'])
def get_bicycle_data(request):
    data = BicycleCountSurvey.objects.all().values()
    return Response(data)


# API for car share usage
@api_view(['GET'])
def get_carshare_data(request):
    data = CarShareUsage.objects.all().values()
    return Response(data)
