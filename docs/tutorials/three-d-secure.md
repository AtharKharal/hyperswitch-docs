# 3D Secure

## Prerequisites

- [Quick Start](quickstart) - Complete the quick start to understand basic payment flows

## Overview

3D Secure is an authentication protocol that adds an extra layer of verification for card payments, reducing fraud and liability for merchants. Hyperswitch handles 3DS seamlessly.

## How 3DS Works

1. Customer initiates payment
2. Hyperswitch detects 3DS requirement
3. Customer redirected to issuer
4. Authentication completes
5. Payment processes

## Enable 3DS for Payment

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/payments" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "amount": 6540,
        "currency": "USD",
        "customer": {
          "email": "customer@example.com"
        },
        "payment_method": {
          "card": {
            "card_number": "4242424242424242",
            "exp_month": "12",
            "exp_year": "2027",
            "cvc": "123"
          }
        },
        "authentication": {
          "type": "3ds",
          "3ds": {
            "device_channel": "browser"
          }
        }
      }'
    ```

## 3DS Response

```json
{
  "payment_id": "pay_abc123",
  "status": "requires_verification",
  "client_secret": "pi_abc_secret_xyz",
  "requires_verification": ["3ds"],
  "verification_url": "https://sandbox.hyperswitch.io/3ds/verify"
}
```

## Handle 3DS Verification

On your frontend after receiving `requires_verification`:

```javascript
const result = await stripe.confirmPayment({
  elements,
  client_secret: response.client_secret,
  confirm_return_url: 'https://your-site.com/payment-complete',
  payment_method: {
    card: elements.getElement(CardElement)
  }
});
```

## 3DS Types

| Type | Description | Liability |
|------|-------------|-----------|
| `3ds` | Classic 3DS 1.0 | Shifted to issuer |
| `3ds2` | 3DS 2.0 (frictionless) | Shifted to issuer |
| `decoupled` | No redirect needed | Case by case |

## Exemptions

Some transactions can skip 3DS:

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/payments" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "amount": 2000,
        "currency": "USD",
        "customer": {
          "email": "customer@example.com",
          "user_agent": "Mozilla/5.0"
        },
        "payment_method": {
          "card": {
            "card_number": "4242424242424242"
          }
        },
        "authentication": {
          "type": "3ds",
          "3ds": {
            "exemption": "low_value"
          }
        }
      }'
    ```

## Playground

Test 3DS in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground).

## Best Practices

1. **Use 3DS2** - Better success rates
2. **Handle exemptions** - Low value, recurring
3. **Show indicators** - Let users know 3DS happening
4. **Test thoroughly** - Different cards, issuers

## Related

- [API Reference: Authentication](../api-reference/authentication/index)
- [Explanation: Payment Flows](../explanation/payment-flows)