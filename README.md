# WELLAIOS Tool Server Demo (Serverless - AWS Lambda)

This repository presents a serverless demonstration for developing tools compatible with the WELLAIOS engine. It showcases how to build and seamlessly integrate custom functionalities, enabling AI agents within the WELLAIOS ecosystem to leverage these tools in a **multi-user** environment.

## Features

- **Multi-User Support**

  Designed to handle simultaneous requests from multiple distinct users, facilitating personalized interactions with your tools.

- **MCP Compatibility**

  Fully compatible with the Model Context Protocol (MCP), ensuring seamless integration and communication with MCP-enabled platforms.

- **WELLAIOS Engine Integration**

  Enables sophisticated AI agent use cases by providing custom tools that the WELLAIOS engine can discover and utilize.

## Getting Started

This demo utilizes a minimal serverless architecture, primarily hosted on **AWS API Gateway** with an **AWS Lambda** function serving as the backend.

To deploy this tool server on AWS Lambda, follow the general deployment documentation provided by AWS for Lambda functions: [AWS Lambda Deployment Steps](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-lambda.html).

Here's a summarized guide to deploy the tool server:

1.  **Create a New AWS Lambda function**

    - In the AWS Management Console, create a new Lambda function.
    - Choose Python as the runtime.

2.  **Upload the Sample Codes**

    Upload the project files to your Lambda function.
    Ensure the directory structure is maintained as follows:

    ```
    mcpserver.py
    lambda_mcp/
    ├── lambda_mcp.py
    ├── session.py
    └── types.py
    ```

    **Important**:
    Verify that the Lambda function's Runtime settings (under the "Configuration" tab) are correctly set.
    The handler should point to `mcpserver.lambda_handler`.

3.  **Create an API Gateway Trigger**

    Configure an **API Gateway** as a trigger for your Lambda function.
    This will expose your Lambda function via an HTTP endpoint.

4.  Test your Tool Server

    You can test your running tool server

    - **MCP Inspector**:
      For basic testing and inspecting the tool's functionality, you can use the [MCP inspector](https://github.com/modelcontextprotocol/inspector).

      **Note**: The MCP Inspector currently does not support multi-user scenarios. Therefore, you won't be able to test the multi-user specific features using this tool alone.

    - **WELLAIOS Engine**:
      The best way to thoroughly test the multi-user capabilities and the full integration is by connecting your tool server to the WELLAIOS engine itself.
      Refer to the WELLAIOS documentation for instructions on how to connect external tool servers.

## Guide to connect to MCP Inspector

### Transport Type

Select `Streamble HTTP`

### URL

Enter the full URL of your deployed tool server.
This will be the URL provided by your AWS API Gateway.
It typically follows this format:

`https://[AWS ID].execute-api.[server location].amazonaws.com/[stage]/[Lambda function name]`

## Notes on Production Readiness

This demo implementation is intended **for testing and demonstration purposes only**.
It lacks critical security measures and robust session management required for production environments.

In a practical production setup:

1. **API Security**: Access to the Lambda function (via API Gateway) **must be protected**. Implement authentication using **Bearer Tokens** (e.g., via AWS Lambda authorizers) to ensure MCP compatibility.

2. **User Authorization**: For comprehensive multi-user support within WELLAIOS, a proper **user authorization system** should be implemented.

## Acknowledgement

This demo server implementation is based on and significantly inspired by the excellent work from the [Lambda MCP Server](https://github.com/mikegc-aws/Lambda-MCP-Server) repository.
