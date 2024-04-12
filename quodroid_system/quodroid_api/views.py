from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TestsSerializer
from .models import Tests

import os

test_suites_location = os.getcwd() + "\\quodroid_api\\test_suites"

@api_view(['POST'])
def run_robot_test(request):
    serializer = TestsSerializer(data=request.data)

    if serializer.is_valid():

        print(serializer.data)

        suites_count = len(os.listdir(test_suites_location))

        # instead of counting the files we can use a unique name for each suite file
        new_suite_name = f'{test_suites_location}\\test_suite_{suites_count + 1}'

        suite_content = f"""
*** Settings ***

Library SeleniumLibrary

*** Test Cases ***"""
        tests = serializer.data.get("tests", [])

        for test in tests:
            test_case = f"""\n\n{test.get("title", "Test Case")}"""

            test_steps = test.get("steps", [])

            for test_step in test_steps:
                test_case += f"\n   {test_step}"

            suite_content += test_case
            
        with open(f"{new_suite_name}.robot", 'w') as robot_suite:
            robot_suite.write(suite_content)
            pass

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # steps are mandatory
        return Response("Incorrect data format", status=status.HTTP_400_BAD_REQUEST)
