# DEX gRPC Python Client

This is a Python client for the DEX gRPC API. It is generated from the DEX gRPC API proto file.

## Installation

```bash
pip install dex-client
```

## Generate the client from the proto file


To download the proto file, run the following command:
```bash
curl -L https://raw.githubusercontent.com/dexidp/dex/refs/heads/master/api/v2/api.proto > api.proto
```

To generate the client, run the following command:

```bash
uv run -m grpc_tools.protoc -I ./ --python_betterproto_out=dex_client api.proto
```

## License

This project is licensed under the MIT License.
