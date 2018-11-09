#!/usr/bin/env bash


if ! [ -n `which java` ];
then
    echo -e "\nInstalling Java!\n"
    apt-get update && apt-get install oracle-java8-set-default
else
    echo -e "\nCompiling java gateway...\n"
    javac  -cp py4j0.10.8.1.jar:. javaGatewayServer.java
    echo -e "Done compiling java gateway!\n"
fi