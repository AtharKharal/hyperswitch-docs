# How to Accept a Payment

## Problem

You need to accept your first payments using the Hyperswitch API.

## Solution

Follow these steps to accept card payments:

### Step 1: Create a Payment Intent

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
        "payment_method": {
          "card": {
            "card_number": "4242424242424242",
            "exp_month": "12",
            "exp_year": "2027",
            "cvc": "123"
          }
        },
        "confirm": true
      }'
    ```

### Step 2: Handle the Response

```json
{
  "payment_id": "pay_abc123",
  "status": "succeeded",
  "amount": 6540,
  "currency": "USD"
}
```

### Step 3: Confirm Card Payments on Frontend

For security, confirm card payments on your frontend:

```javascript
const stripe = Stripe('pk_your_key');

const {error, paymentIntent} = await stripe.confirmCardPayment(
  clientSecret,
  {
    payment_method: {
      card: cardElement,
      billing_details: {name: 'John Doe'}
    }
  }
);
```

## Common Statuses

| Status | Description | Next Action |
|--------|-------------|-------------|
| `succeeded` | Payment complete | Show success |
| `requires_payment_method` | Card declined | Request new card |
| `requires_verification` | 3DS needed | Redirect to verification |
| `requires_capture` | Pre-authorized | Capture later |
| `processing` | Processing | Wait for webhook |
| `failed` | Failed | Show error |

## Partial Payments

For split payments:

```json
{
  "amount": 10000,
  "currency": "USD",
  "automatic_payment_method": {
    "enabled": true,
    "multiple_enabled": true
  }
}
```

## Recurring Payments

Set up for future charges:

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/payments" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "amount": 2999,
        "currency": "USD",
        "customer_id": "cus_existing",
        "setup_future_usage": "off_session"
      }'
    ```

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Related

- [API Reference: Payments](../api-reference/payments/index)
- [Tutorial: Quick Start](../tutorials/quickstart)