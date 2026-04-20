# Connectors

## Prerequisites

- [Quick Start](quickstart) - Complete the quick start to understand basic payment flows

## Overview

Hyperswitch integrates with 50+ payment processors (connectors). This tutorial covers managing connectors programmatically.

## Supported Connectors

| Region | Connectors |
|--------|------------|
| Global | Stripe, PayPal, Adyen, Braintree |
| US | Stripe, PayPal, Square, Authorize.net |
| Europe | Stripe, PayPal, Adyen, Mollie |
| Asia | Stripe, PayPal, RazorPay, Paytm |

## Add a Connector

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/connectors" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "connector_type": "stripe",
        "connector_account_id": "acct_your_stripe_id",
        "api_key": "sk_live_your_stripe_key",
        "api_secret": "sk_live_your_stripe_secret",
        "meta": {
          "merchant_id": "your_merchant_id"
        }
      }'
    ```

## Response

```json
{
  "connector_id": "conn_stripe_abc",
  "connector_type": "stripe",
  "status": "active",
  "merchant_id": "your_merchant_id",
  "created_at": "2026-04-19T12:00:00Z"
}
```

## Retrieve Connector

=== "cURL"

    ```bash
    curl -X GET "https://sandbox.hyperswitch.io/connectors/conn_stripe_abc" \
      -H "api-key: sk_snd_your_api_key"
    ```

## Update Connector

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/connectors/conn_stripe_abc" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "api_key": "sk_live_new_key"
      }'
    ```

## Test Mode

Use sandbox credentials for testing:

```json
{
  "connector_type": "stripe",
  "api_key": "sk_test_your_key",
  "api_secret": "sk_test_your_secret"
}
```

## Playground

Test connector operations in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground).

## Best Practices

1. **Use test keys in sandbox** - Never use production keys
2. **Store credentials securely** - Use secrets management
3. **Enable logging** - For debugging issues
4. **Monitor performance** - Track success rates

## Next Steps

- [Customers](customers) - Create customer profiles to track payments
- [Smart Routing](routing) - Configure intelligent payment routing

## Related

- [API Reference: Merchant Connector Account](../api-reference/merchant-connector-account/index)
- [Explanation: Architecture](../explanation/architecture)