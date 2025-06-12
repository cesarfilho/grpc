import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('server:50051') as channel:
        stub = helloworld_pb2_grpc.HelloServiceStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='LinkedIn'))
    print("Resposta do servidor:", response.message)

if __name__ == '__main__':
    run()