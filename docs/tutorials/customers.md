# Customers

## Prerequisites

- [Quick Start](quickstart) - Complete the quick start to understand basic payment flows

## Overview

Learn how to create, retrieve, update, and delete customer profiles in Hyperswitch. Customer profiles enable:
- Saved payment methods for returning customers
- Unified billing history
- Better fraud detection

## Create a Customer

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/customers" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "email": "john.doe@example.com",
        "name": "John Doe",
        "phone": "+1234567890",
        "metadata": {
          "loyalty_tier": "gold"
        }
      }'
    ```

=== "Python"

    ```python
    import requests
    
    url = "https://sandbox.hyperswitch.io/customers"
    payload = {
        "email": "john.doe@example.com",
        "name": "John Doe",
        "phone": "+1234567890",
        "metadata": {"loyalty_tier": "gold"}
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const axios = require('axios');
    
    const response = await axios.post('https://sandbox.hyperswitch.io/customers', {
      email: 'john.doe@example.com',
      name: 'John Doe',
      phone: '+1234567890',
      metadata: {loyalty_tier: 'gold'}
    }, {headers});
    ```

## Response

```json
{
  "customer_id": "cus_abc123xyz",
  "email": "john.doe@example.com",
  "name": "John Doe",
  "created_at": "2026-04-19T12:00:00Z"
}
```

## Retrieve a Customer

=== "cURL"

    ```bash
    curl -X GET "https://sandbox.hyperswitch.io/customers/cus_abc123xyz" \
      -H "api-key: sk_snd_your_api_key"
    ```

## Update a Customer

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/customers/cus_abc123xyz" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "email": "new.email@example.com",
        "metadata": {
          "loyalty_tier": "platinum",
          "account_age": "2_years"
        }
      }'
    ```

## List Customers

=== "cURL"

    ```bash
    curl -X GET "https://sandbox.hyperswitch.io/customers/list?limit=10&offset=0" \
      -H "api-key: sk_snd_your_api_key"
    ```

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/customers&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Best Practices

1. **Always create customers first** - Then associate payments to them
2. **Use metadata** - Store custom attributes for analytics
3. **Email uniqueness** - Hyperswitch allows duplicate emails across customers

## Next Steps

- [Process Refunds](process-refunds) - Learn to issue refunds for payments

## Related

- [API Reference: Customers](../api-reference/customers/index)
- [How-To: Accept Payment](../howto/accept-payment)