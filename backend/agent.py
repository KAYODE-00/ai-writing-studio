import json

from llm import llm_raw


# DEMO DATA — later replaced with a database
ORDERS = {
    "1005": {
        "status": "Shipped",
        "delivery": "Expected in 2 business days"
    },
    "1006": {
        "status": "Processing",
        "delivery": "Not yet dispatched"
    }
}


# 1. Actual Python tool function
def check_order_status(order_id):

    order = ORDERS.get(order_id)

    if not order:
        return {
            "error": "Order not found"
        }

    return order


# 2. Tool definition given to the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "check_order_status",
            "description": "Check a customer's order status",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The customer's order ID"
                    }
                },
                "required": ["order_id"]
            }
        }
    }
]


# 3. Tool registry
AVAILABLE_TOOLS = {
    "check_order_status": check_order_status
}


# 4. Agent execution loop
def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": (
                "You are a customer support agent. "
                "Use available tools to check order information. "
                "Never invent order statuses."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):

        response = llm_raw(
            messages,
            tools=TOOLS
        )

        assistant_message = response.choices[0].message

        messages.append(assistant_message)

        if not assistant_message.tool_calls:
            return assistant_message.content

        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            function = AVAILABLE_TOOLS.get(tool_name)

            if function is None:
                result = {"error": "Unknown tool"}
            else:
                result = function(**arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

    return "I couldn't complete that request. Please contact support."