from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TestsSerializer

import os

# could be some cloud location
test_suites_location = os.getcwd() + "\\quodroid_api\\test_suites"

# POST method
@api_view(['POST'])
def run_robot_test(request):

    serializer = TestsSerializer(data=request.data)

    if serializer.is_valid():

        suites_count = len(os.listdir(test_suites_location))

        # instead of counting the files we can use a unique name for each suite file
        # counting since working locally for now
        new_suite_name = f'{test_suites_location}\\test_suite_{suites_count + 1}'
        os.mkdir(new_suite_name)
        new_testfile_name = f"{new_suite_name}\\test"

        suite_content = f"""
*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***"""
        tests = serializer.data.get("tests", [])

        for test in tests:
            test_case = f"""\n\n{test.get("title", "Test Case")}"""

            test_steps = test.get("steps", [])

            for test_step in test_steps:
                test_case += f"\n   {test_step}"

            suite_content += test_case
            
        with open(f"{new_testfile_name}.robot", 'w') as robot_suite:
            robot_suite.write(suite_content)
        
        print(test_suites_location)
        
        os.system(f'robot -d {new_suite_name} {new_testfile_name}.robot')

        return Response({'results': new_suite_name}, status=status.HTTP_200_OK)
    else:
        # steps are mandatory
        return Response("Incorrect data format", status=status.HTTP_400_BAD_REQUEST)
