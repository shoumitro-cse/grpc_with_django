### Tutorial
 - https://grpc.io/docs/languages/python/basics/
 - https://grpc.io/docs/what-is-grpc/introduction/
 - https://protobuf.dev/overview/
 - https://protobuf.dev/getting-started/pythontutorial/
 - https://protobuf.dev/reference/python/python-generated/
 - https://grpc.io/docs/protoc-installation/


### Proto Buffering
```angular2html

# install grpc
pip install grpcio grpcio-tools

cd django_grpc
python3 -m grpc_tools.protoc -I customer_protoc --python_out=. --grpc_python_out=. customer_protoc/customer.proto


# using ubuntu system protoc
sudo pip install grpclib protobuf-4.24.4
sudo apt install -y protobuf-compiler
protoc -I=customer_protoc --plugin=grpc_python_plugin --python_out=. --grpclib_python_out=. customer_protoc/customer.proto

```

