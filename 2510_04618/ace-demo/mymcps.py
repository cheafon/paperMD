import asyncio
import os

from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters

env = os.environ.copy()
node_bin = "/home/eason/.nvm/versions/node/v22.2.0/bin"
env["PATH"] = f"{node_bin}:{env.get('PATH', '')}"

semantic_mcp = McpToolset(
    connection_params=
    StdioConnectionParams(
        timeout=25,
        server_params=StdioServerParameters(
            command="/home/eason/.nvm/versions/node/v22.2.0/bin/npx",
            args=[
                "-y",
                "@smithery/cli@latest",
                "run",
                "@hamid-vakilzadeh/mcpsemanticscholar",
                "--key",
                "e2404846-5a81-4a02-91c3-a5504703a745",
                "--profile",
                "intellectual-toucan-DB0osA"
            ],
            env=env
        ))
)

file_mcp = McpToolset(
    connection_params=
    StdioConnectionParams(
        timeout=25,
        server_params=StdioServerParameters(
            command="/home/eason/.nvm/versions/node/v22.2.0/bin/npx",
            args=[
                "-y",
                "@smithery/cli@latest",
                "run",
                "@bhushangitfull/file-mcp-smith",
                "--key",
                "e2404846-5a81-4a02-91c3-a5504703a745"
            ],
            env=env
        ))
)
async def write_book(book_item:str)->str:
    """
    Using for saving the result of curator
    """
    with open('/home/eason/PycharmProjects/paperMD/2510_04618/ace-demo/playbook.txt', 'a') as f:
        f.write("=========================\n")
        f.write(book_item)