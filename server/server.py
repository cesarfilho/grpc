from concurrent import futures
import grpc
import time
import helloworld_pb2
import helloworld_pb2_grpc

class HelloService(helloworld_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f"Olá, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()