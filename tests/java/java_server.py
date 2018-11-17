import subprocess
import os
import time

from py4j.java_gateway import JavaGateway


class JavaServer:
    def __init__(self):
        self.gateway_pid = None
        self.gateway = None

    def run_server(self):
        process = self.__run_in_java_dir()
        self.__check_server_is_alive()
        self.gateway_pid = process.pid
        self.gateway = JavaGateway()
        return self.gateway

    def __run_in_java_dir(self):
        path = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        process = subprocess.Popen(['java', '-cp', 'py4j0.10.8.1.jar:.', 'javaGatewayServer'])
        os.chdir(path)
        return process

    def __check_server_is_alive(self):
        time.sleep(0.5)
        try:
            JavaGateway(eager_load=True)
        except Exception as e:
            raise Exception("Failed to load java server for tests...") from e

    def shutdown_server(self):
        self.gateway.shutdown()
        os.kill(self.gateway_pid, 9)
        self.gateway = None