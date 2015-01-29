#!/bin/sh

java -jar selenium-server-standalone-2.44.0.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -Dwebdriver.chrome.driver="chromedriver.exe" \
    -browser browserName=chrome,maxInstances=1 \
    -browser browserName=firefox,maxInstances=1