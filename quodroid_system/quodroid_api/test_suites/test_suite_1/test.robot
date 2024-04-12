
*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***

Open google.com
   Open Browser  browser=chrome
   Go To  url=https://google.com

Open yahoo.com
   Open Browser  browser=edge
   Go To  url=https://yahoo.com