import grpc
from concurrent import futures
import customer_pb2
import customer_pb2_grpc

import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_grpc.settings')
django.setup()

from django.shortcuts import get_object_or_404
from grpc_app.models import Customer


class CustomerService(customer_pb2_grpc.CustomerServiceServicer):

    def CreateCustomer(self, request, context):
        customer = Customer(
            name=request.name,
            phone=request.phone,
            address=request.address,
            email=request.email
        )
        customer.save()
        return customer_pb2.Customer(
            customer_id=str(customer.id),
            name=customer.name,
            phone=customer.phone,
            address=customer.address,
            email=customer.email
        )

    def GetCustomer(self, request, context):
        customer = get_object_or_404(Customer, id=request.customer_id)
        return customer_pb2.Customer(
            customer_id=str(customer.id),
            name=customer.name,
            phone=customer.phone,
            address=customer.address,
            email=customer.email
        )

    def UpdateCustomer(self, request, context):
        customer = get_object_or_404(Customer, id=request.customer_id)
        customer.name = request.name
        customer.phone = request.phone
        customer.address = request.address
        customer.email = request.email
        customer.save()
        return customer_pb2.Customer(
            customer_id=str(customer.id),
            name=customer.name,
            phone=customer.phone,
            address=customer.address,
            email=customer.email
        )

    def DeleteCustomer(self, request, context):
        customer = get_object_or_404(Customer, id=request.customer_id)
        customer.delete()
        return customer_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_pb2_grpc.add_CustomerServiceServicer_to_server(CustomerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
