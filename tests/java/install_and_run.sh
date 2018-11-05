#!/usr/bin/env bash

apt-get update && apt-get install oracle-java8-set-default
echo -e "\n done installing... Gateway is up! \n"
java -cp py4j0.10.8.1.jar:. java_gateway_server