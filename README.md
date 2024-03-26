# RouteRover

RouteRover is a route mapping application designed to provide clients with comprehensive information about features along their routes. It empowers users to create summaries of their routes and facilitates the exchange of route-related data, including real-time traffic updates, with the server and other clients.

---

## Generating Python Code for gRPC Services

To generate Python code from Protocol Buffer (.proto) files, specifically for gRPC (Google Remote Procedure Call) services, you can use the following commands:

```bash
pip install grpcio-tools
```

You can use the `-I` parameter along with the `grpc_tools.protoc` command to specify a custom package name for the generated files

```bash
python -m grpc_tools.protoc -I<path/to/your/proto/dir> --python_out=. --grpc_python_out=. <path/to/your/proto/file>
```

