# Quick Start Tutorial

## Prerequisites

!!! warning "API Key Security"
    Never expose your secret API keys in client-side code. Always keep them on your server.

Before you begin, ensure you have:
- A Hyperswitch account at [app.hyperswitch.io](https://app.hyperswitch.io)
- Your API keys (available in the dashboard under Developers → API Keys)
- A payment processor account (Stripe, PayPal, Adyen, etc.)

## Step 1: Create a Payment

The first step is to create a payment intent. This is the core operation in Hyperswitch.

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/payments" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "amount": 6540,
        "currency": "USD",
        "customer": {
          "email": "customer@example.com",
          "name": "John Doe"
        },
        "return_url": "https://your-site.com/payment-complete"
      }'
    ```

=== "Python"

    ```python
    import requests
    
    url = "https://sandbox.hyperswitch.io/payments"
    headers = {
        "Content-Type": "application/json",
        "api-key": "sk_snd_your_api_key"
    }
    payload = {
        "amount": 6540,
        "currency": "USD",
        "customer": {
            "email": "customer@example.com",
            "name": "John Doe"
        },
        "return_url": "https://your-site.com/payment-complete"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const axios = require('axios');
    
    const url = 'https://sandbox.hyperswitch.io/payments';
    const options = {
      method: 'POST',
      url: url,
      headers: {
        'Content-Type': 'application/json',
        'api-key': 'sk_snd_your_api_key'
      },
      data: {
        amount: 6540,
        currency: 'USD',
        customer: {
          email: 'customer@example.com',
          name: 'John Doe'
        },
        return_url: 'https://your-site.com/payment-complete'
      }
    };
    
    axios.request(options)
      .then(res => console.log(res.data))
      .catch(err => console.error(err));
    ```

## Step 2: Handle the Response

The API returns a `client_secret` which you use to complete the payment on the client side:

```json
{
  "payment_id": "pay_abc123xyz",
  "client_secret": "pi_abc123_secret_xyz789",
  "status": "requires_payment_method",
  "amount": 6540,
  "currency": "USD"
}
```

## Step 3: Complete with Payment Element

On your frontend, use the client-side SDK to collect card details:

```javascript
const stripe = Stripe('pk_your_publishable_key');

await stripe.confirmPayment({
  elements,
  client_secret: response.client_secret,
  confirm_return_url: 'https://your-site.com/payment-complete'
});
```

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Next Steps

- [Connectors](connectors) - Set up payment processors (recommended next)
- [Customers](customers) - Create and manage customer profiles
- [Process Refunds](process-refunds) - Learn how to refund payments