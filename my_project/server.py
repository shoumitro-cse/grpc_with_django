from concurrent import futures
import time
import grpc
import my_proj_pb2
import my_proj_pb2_grpc


"""
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business.settings')
django.setup()
"""


class MyServicer(my_proj_pb2_grpc.MyServiceDataServicer):
    
    def MyUnaryFun(self, request, context):
        print("MyUnaryFun Request Made:")
        print(request)
        hello_reply = my_proj_pb2.MyReply()
        hello_reply.message = f"{request.email} {request.name}"
        return hello_reply
    
    def MyServerStreamingFun(self, request, context):
        print("MyServerStreamingFun Request Made:")
        print(request)

        for i in range(30):
            hello_reply = my_proj_pb2.MyReply()
            hello_reply.message = f"{request.email} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)

    def MyClientStreamingFun(self, request_iterator, context):
        delayed_reply = my_proj_pb2.MyDelayedReply()
        for request in request_iterator:
            print("MyClientStreamingFun Request Made:")
            print(request)
            delayed_reply.request.append(request)
        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

    def MyBothStreamingFun(self, request_iterator, context):
        for request in request_iterator:
            print("MyBothStreamingFun Request Made:")
            print(request)
            hello_reply = my_proj_pb2.MyReply()
            hello_reply.message = f"{request.email} {request.name}"
            yield hello_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_proj_pb2_grpc.add_MyServiceDataServicer_to_server(MyServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

