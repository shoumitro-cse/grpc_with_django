import my_proj_pb2_grpc
import my_proj_pb2
import time
import grpc

"""
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business.settings')
django.setup()
"""


def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = my_proj_pb2.MyRequest(
            email="shoumitro26@gmail.com",
            name=name,
            address="Mirpur3",
            image_url="dd",
            balance_amount="500", )
        yield hello_request

        time.sleep(1)


def run():
    # with grpc.insecure_channel('116.206.56.193:50051') as channel:
    with grpc.insecure_channel('0.0.0.0:50051') as channel:

        stub = my_proj_pb2_grpc.MyServiceDataStub(channel)

        print("1. MyUnaryFun - Unary")
        print("2. MyServerStreamingFun - Server Side Streaming")
        print("3. MyClientStreamingFun - Client Side Streaming")
        print("4. MyBothStreamingFun - Both Streaming")

        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            my_request = my_proj_pb2.MyRequest(
                name="Shoumitro2",
                email="shoumitro26@gmail.com",
                address="Mirpur",
                image_url="dd",
                balance_amount="500",
            )
            hello_reply = stub.MyUnaryFun(my_request)
            print("MyUnaryFun Response Received:")
            print(hello_reply)

        elif rpc_call == "2":
            hello_request = my_proj_pb2.MyRequest(
                email="shoumitro26@gmail.com",
                name="Shoumitro1",
                address="Mirpur",
                image_url="dd",
                balance_amount="500",
            )
            hello_replies = stub.MyServerStreamingFun(hello_request)

            for hello_reply in hello_replies:
                print("MyServerStreamingFun Response Received:")
                print(hello_reply)

        elif rpc_call == "3":
            delayed_reply = stub.MyClientStreamingFun(get_client_stream_requests())

            print("MyClientStreamingFun Response Received:")
            print(delayed_reply)

        elif rpc_call == "4":
            responses = stub.MyBothStreamingFun(get_client_stream_requests())

            for response in responses:
                print("MyBothStreamingFun Response Received: ")
                print(response)


if __name__ == "__main__":
    run()
