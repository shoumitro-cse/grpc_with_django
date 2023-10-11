import grpc
import customer_pb2
import customer_pb2_grpc


def run_client():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a gRPC stub for the CustomerService
        stub = customer_pb2_grpc.CustomerServiceStub(channel)

        # Create a new customer
        create_request = customer_pb2.CreateCustomerRequest(
            name="John Doe",
            phone="123-456-7890",
            address="123 Main St",
            email="johndoe@example.com"
        )
        created_customer = stub.CreateCustomer(create_request)
        print("Created Customer:")
        print(created_customer)

        # Get a customer by ID
        get_request = customer_pb2.GetCustomerRequest(customer_id=created_customer.customer_id)
        retrieved_customer = stub.GetCustomer(get_request)
        print("\nRetrieved Customer:")
        print(retrieved_customer)

        # Update a customer
        update_request = customer_pb2.UpdateCustomerRequest(
            customer_id=created_customer.customer_id,
            name="Updated Name",
            phone="987-654-3210",
            address="456 Updated St",
            email="updated@example.com"
        )
        updated_customer = stub.UpdateCustomer(update_request)
        print("\nUpdated Customer:")
        print(updated_customer)

        # # Delete a customer
        # delete_request = customer_pb2.DeleteCustomerRequest(customer_id=created_customer.customer_id)
        # stub.DeleteCustomer(delete_request)
        # print("\nDeleted Customer")


if __name__ == '__main__':
    run_client()

