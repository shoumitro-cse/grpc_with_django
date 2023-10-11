import greet_pb2  # Import the generated Python protobuf module

# Create an instance of the protobuf message
hello_request = greet_pb2.HelloRequest()

# Parse the binary string into the message
binary_string = b'\n\x0bgreet.proto\x12\x05greet".\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t"E\n\x0cDelayedReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12$\n\x07request\x18\x02 \x03(\x0b2\x13.greet.HelloRequest2\xff\x01\n\x07Greeter\x122\n\x08SayHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply\x12;\n\x0fParrotSaysHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply0\x01\x12C\n\x15ChattyClientSaysHello\x12\x13.greet.HelloRequest\x1a\x13.greet.DelayedReply(\x01\x12>\n\x10InteractingHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply(\x010\x01b\x06proto3'
hello_request.ParseFromString(binary_string)

# Access the fields in the message
print("Name:", hello_request.name)
print("Greeting:", hello_request.greeting)
