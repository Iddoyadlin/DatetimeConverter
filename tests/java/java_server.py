import subprocess
import os

from py4j.java_gateway import JavaGateway


class JavaServer:
    RUN_JAVA_SERVER_CMD = "-cp py4j0.10.8.1.jar:. java_gateway_server"

    def __init__(self):
        self.gateway_pid = None
        self.gateway = None

    def run_server(self):
        path = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        self.process = subprocess.Popen(['java', '-cp', 'py4j0.10.8.1.jar:.', 'java_gateway_server'])
        os.chdir(path)
        self.gateway_pid = self.process.pid
        self.gateway = JavaGateway()
        return self.gateway


    def shutdown_server(self):
        self.gateway.shutdown()
        os.kill(self.gateway_pid, 9)
        self.gateway = None