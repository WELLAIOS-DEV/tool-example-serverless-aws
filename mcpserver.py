from typing import Any, Dict
from lambda_mcp.lambda_mcp import LambdaMCPServer

# Create an instance of the LambdaMCP server.
# This server will host our tools and handle requests from the WELLAIOS engine.
mcp_server = LambdaMCPServer(name="wellaios-demo", version="1.0.0")


@mcp_server.tool()
def get_my_id(lambda_event: Dict[str, Any]) -> str:
    """
    Retrieves the ID of the current user.

    This tool requires no parameters.

    Returns:
        The ID of the current user as a string.
    """
    # Extract headers from the Lambda event. Default to an empty dictionary if not present.
    headers = lambda_event.get("headers", {})
    # Attempt to retrieve the user ID from the 'X-User-ID' header.
    user_id = headers.get("X-User-ID")
    if user_id is None:
        # If 'X-User-ID' is missing, it means the request is likely not from a
        # multi-user WELLAIOS context. We default to "single_user" to maintain
        # compatibility with traditional MCP or simple testing scenarios.
        user_id = "single_user"
    return user_id


def lambda_handler(event: Dict[str, Any], context: Any):
    """
    The main AWS Lambda handler function.
    """
    return mcp_server.handle_request(event, context)
