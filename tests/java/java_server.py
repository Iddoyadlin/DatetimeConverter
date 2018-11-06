import subprocess
import os

from py4j.java_gateway import JavaGateway


class JavaServer:
    RUN_JAVA_SERVER_CMD = "java -cp py4j0.10.8.1.jar:. java_gateway_server"

    def __init__(self):
        self.gateway_pid = None
        self.gateway = None

    def run_server(self):
        process = subprocess.check_output(self.RUN_JAVA_SERVER_CMD)
        self.gateway_pid = process.pid
        self.gateway = JavaGateway()
        return self.gateway


    def shutdown_server(self):
        self.gateway.stop()
        os.kill(self.gateway_pid)