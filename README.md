# QuoDroid System

## Problem Statement
The core objective of this challenge is to create a system that can accept a detailed API call,
execute the testing steps provided within as a Robot Framework test, and subsequently
return the test output. This entails developing an application using Python and Django that
exposes an API endpoint.

## Requirements
- python
- django
- django restframework
- robot framework
- selenium library

## Setup

Clone the repository

```
git clone https://github.com/abhimessi16/quodroid_system.git
```

Go to the directory
```
pip install -r requirements.txt

cd quodroid_system

python manage.py runserver
```

The server will start running at http://127.0.0.1:8000

## Solution

Expose an endpoint which will accept a POST method with body containing details about the tests to perform using the robot framework.

User makes the api call with valid data. The server will track the body recevied via the request and create a robot test suite dynamically and store it in the directory named 'test_suites'. Each api call will have a seperate folder to store the test execution results.

The server then runs the robot command with the created test suite. The outputs are stored in the directory created for the specific test suite.

The api call response contains the output files directory path.

## Example

Endpoint - /testai/tests/v1/execute

Method - POST

Payload format
```
{
    "tests":[
        {
            "title":"Open google.com",
            "steps":[
                "Open Browser browser=chrome",
                "Go To url=https://google.com"
            ]
        }
    ]
}
```

Result
```
{
    "results": "C:/test_suite_1"
}
```
