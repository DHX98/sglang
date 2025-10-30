"""Launch the inference server."""

import asyncio
import os
import sys

from sglang.Mylogger import MyLogger
from sglang.srt.server_args import prepare_server_args
from sglang.srt.utils import kill_process_tree

# Step7: python -m sglang.launch_server ...。它会解析参数，然后直接起上面的 HTTP / gRPC server
if __name__ == "__main__":
    server_args = prepare_server_args(sys.argv[1:])

    try:
        if server_args.grpc_mode:
            MyLogger.banner("Step7: launch_server Grpc")
            # Handle gRPC server
            from sglang.srt.entrypoints.grpc_server import serve_grpc

            asyncio.run(serve_grpc(server_args))
        else:
            MyLogger.banner("Step7: launch_server Http")
            # Handle HTTP server
            from sglang.srt.entrypoints.http_server import launch_server

            launch_server(server_args)
    finally:
        kill_process_tree(os.getpid(), include_parent=False)
