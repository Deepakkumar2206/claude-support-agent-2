import json

from mock_data import CUSTOMERS, ORDERS


def get_customer(query: str) -> str:
    query = query.strip().lower()

    for customer in CUSTOMERS.values():

        if (
            query == customer["customer_id"].lower()
            or query == customer["email"].lower()
            or query == customer["name"].lower()
        ):
            return json.dumps(customer)

    return json.dumps(
        {
            "error": {
                "type": "validation",
                "retryable": False,
                "message": (
                    "Customer not found. Verify customer ID, "
                    "email address or full name."
                ),
            }
        }
    )


def lookup_order(order_id: str) -> str:
    order_id = order_id.strip().upper()

    if order_id in ORDERS:
        return json.dumps(ORDERS[order_id])

    return json.dumps(
        {
            "error": {
                "type": "validation",
                "retryable": False,
                "message": (
                    "Order not found. Verify the order ID "
                    "and try again."
                ),
            }
        }
    )


def run_tool(tool_name: str, tool_input: dict) -> str:

    if tool_name == "get_customer":
        return get_customer(tool_input["query"])

    if tool_name == "lookup_order":
        return lookup_order(tool_input["order_id"])

    return json.dumps(
        {
            "error": {
                "type": "system",
                "retryable": False,
                "message": f"Unknown tool: {tool_name}",
            }
        }
    )