from concurrent import futures
import grpc
import greeting_pb2
import greeting_pb2_grpc


class Greeter(greeting_pb2_grpc.GreeterServicer):
    def greet(self, request, context):
        print("Got request " + str(request))
        return greeting_pb2.ServerOutput(message='{} {}!'.format(request.greeting, request.name))


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    greeting_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:5001')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
