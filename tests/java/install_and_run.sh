#!/usr/bin/env bash


if ! [ -n `which java` ];
then
    echo -e "\n Installing Java! \n"
    apt-get update && apt-get install oracle-java8-set-default
else
    echo -e "\n Compiling java gateway... \n"
    javac  -cp py4j0.10.8.1.jar:. java_gateway_server.java
    echo -e "\n Running the gateway :) \n"
    java -cp py4j0.10.8.1.jar:. java_gateway_server
fi