from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TestsSerializer

import os

@api_view(['POST'])
def run_robot_test(request):
    serializer = TestsSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():

        print(serializer.data)

        suites_count = len(os.listdir(os.getcwd() + "\\quodroid_api\\test_suites"))

        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
