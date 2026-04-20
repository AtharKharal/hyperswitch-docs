# How to Set Up Routing

## Problem

You need to configure intelligent payment routing to optimize success rates and reduce costs.

## Solution

### Create a Routing Profile

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/routing" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "name": "Production Routing",
        "rules": [
          {
            "name": "Visa - Primary",
            "condition": {
              "field": "card.brand",
              "equals": "visa"
            },
            "action": {
              "type": "route_to",
              "connector": "stripe"
            },
            "priority": 1
          },
          {
            "name": "Mastercard - Save",
            "condition": {
              "field": "card.brand",
              "equals": "mastercard"
            },
            "action": {
              "type": "route_to",
              "connector": "adyen"
            },
            "priority": 2
          },
          {
            "name": "Fallback",
            "action": {
              "type": "route_to",
              "connector": "stripe"
            },
            "priority": 99
          }
        ]
      }'
    ```

## Condition Operators

| Operator | Example |
|----------|---------|
| `equals` | `"equals": "visa"` |
| `starts_with` | `"starts_with": "4"` |
| `contains` | `"contains": "premium"` |
| `gte` | `"gte": 10000` |

## Action Types

### Route to Single Connector
```json
{
  "action": {
    "type": "route_to",
    "connector": "stripe"
  }
}
```

### Split Load
```json
{
  "action": {
    "type": "split",
    "split_ratio": [70, 30],
    "connectors": ["stripe", "adyen"]
  }
}
```

### Failover
```json
{
  "action": {
    "type": "failover",
    "connectors": ["stripe", "adyen"]
  }
}
```

## Use Routing in Payment

```json
{
  "amount": 5000,
  "currency": "USD",
  "routing_profile": "rout_abc123"
}
```

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Related

- [API Reference: Routing](../api-reference/routing/index)
- [Tutorial: Smart Routing](../tutorials/routing)