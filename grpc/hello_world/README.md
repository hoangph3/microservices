# gRPC - Hello World

## .proto file
```proto
syntax = "proto3";

service Greeter {
   rpc greet (ClientInput) returns (ServerOutput) {}
}
message ClientInput {
   string greeting = 1;
   string name = 2;
}
message ServerOutput {
   string message = 1;
}
```

The `syntax` in the first block represents the version of Protobuf we are using (proto3).

In the second block, the name of the service `Greeter` and the function name `greet` which can be called. The `greet` function takes in the input of type `ClientInput` and returns the output of type `ServerOutput`.

In the third block, we have defined the `ClientInput` which contains two attributes, `greeting` and the `name` both of them being strings. The client is supposed to send the object of type of `ClientInput` to the server.

Finally, we have also defined that, given a `ClientInput`, the server would return the `ServerOutput` with a single attribute `message`. The server is supposed to send the object of type `ServerOutput` to the client.

## Protobuf classes and gRPC classes

Install package dependencies:

```sh
pip3 install -r requirements.txt
```

Generate the underlying code for the Protobuf classes and the gRPC classes by execute the following command:

```sh
python3 -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. greeting.proto
```

This should auto-generate the source code required for us to use gRPC.
- Protobuf class code: `greeting_pb2.py`
- Protobuf gRPC code: `greeting_pb2_grpc.py`

## Setting up gRPC server

```sh
python3 test_server.py
```

## Setting up gRPC client

```sh
python3 test_client.py
```
