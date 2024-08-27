import grpc
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../api')))

from api.greeting import helloworld_pb2
from api.greeting import helloworld_pb2_grpc

def run():
    # Establish a connection to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a client stub (this is the client)
        stub = helloworld_pb2_grpc.ExampleServiceStub(channel)

        # Create a request message
        request = helloworld_pb2.HelloRequest(name='World')

        # Make the call to the server using the client stub
        response = stub.SayHello(request)

    # Print the response message from the server
    print(f"Greeting: {response.message}")

if __name__ == '__main__':
    run()