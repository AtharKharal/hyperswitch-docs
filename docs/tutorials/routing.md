# Smart Routing

## Prerequisites

- [Quick Start](quickstart) - Complete the quick start to understand basic payment flows
- [Connectors](connectors) - Set up payment processors before configuring routing

## Overview

Hyperswitch's smart routing intelligently routes payments across multiple processors to optimize:
- Success rates
- Authorization rates
- Processing fees
- Customer experience

## Create a Routing Profile

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/routing" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "name": "Optimized Routing",
        "rules": [
          {
            "name": "Visa Priority",
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
            "name": " Mastercard Savings",
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
            "condition": {
              "field": "amount",
              "gte": 0
            },
            "action": {
              "type": "route_to", 
              "connector": "stripe"
            },
            "priority": 99
          }
        ]
      }'
    ```

## Routing Conditions

| Field | Operators | Example |
|-------|-----------|---------|
| `card.brand` | equals | `visa`, `mastercard`, `amex` |
| `card.bin` | starts_with | `4` (Visa) |
| `amount` | gte, lte, eq | `10000` |
| `currency` | equals | `USD`, `EUR` |
| `customer.country` | equals | `US`, `IN` |

## Routing Actions

### Route to Specific Connector

```json
{
  "action": {
    "type": "route_to",
    "connector": "stripe"
  }
}
```

### Split Routing

```json
{
  "action": {
    "type": "split",
    "split_ratio": [70, 30],
    "connectors": ["stripe", "adyen"]
  }
}
```

## Use Routing in Payments

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/payments" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "amount": 6540,
        "currency": "USD",
        "routing_profile": "rout_abc123",
        "customer": {
          "email": "customer@example.com"
        }
      }'
    ```

## Analytics

View routing performance in the dashboard:
- Success rate per connector
- Average authorization time
- Cost savings

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Best Practices

1. **Start simple** - Begin with fallback routing
2. **A/B test** - Compare success rates
3. **Monitor costs** - Track processor fees
4. **Keep backups** - Always have a fallback

## Next Steps

- [Webhooks](webhooks) - Set up real-time notifications for payment events

## Related

- [API Reference: Routing](../api-reference/routing/index)
- [How-To: Set Up Routing](../howto/setup-routing)