tools = [
    {
        "name": "get_customer",
        "description": (
            "Look up customer information using customer ID, "
            "email address or full name. "
            "Returns account details and order IDs. "
            "Do not use for order details. "
            "Use lookup_order instead."
        ),

        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": (
                        "Customer ID, email or full name."
                    )
                }
            },

            "required": ["query"]
        }
    },

    {
        "name": "lookup_order",

        "description": (
            "Look up order information using an order ID. "
            "Returns shipping status, notes and order progress. "
            "If order ID is unknown, use get_customer first."
        ),

        "input_schema": {
            "type": "object",

            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Order ID like ORD-8821"
                }
            },

            "required": ["order_id"]
        }
    }
]