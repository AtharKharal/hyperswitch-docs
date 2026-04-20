# Authentication

## Overview

Hyperswitch supports multiple authentication methods for payment verification.

## 3D Secure (3DS)

3DS adds an extra verification step:

### Request 3DS

```json
{
  "amount": 5000,
  "currency": "USD",
  "authentication": {
    "type": "3ds",
    "3ds": {
      "device_channel": "browser"
    }
  }
}
```

### Response with 3DS

```json
{
  "payment_id": "pay_abc123",
  "status": "requires_verification",
  "verification_url": "https://..."
}
```

## Authentication Response Codes

| Code | Description | Liability |
|------|------------|-----------|
| `Y` | Fully authenticated |Issuer |
| `A` | Attempts |Merchant |
| `N` | Not authenticated |Merchant |
| `U` | Unable to verify |Merchant |

## Exemptions

Some transactions can skip 3DS:
- Low value (< $100)
- Recurring (same merchant)
- Trusted merchants

## Tokenization

For card on file:

```json
{
  "customer_id": "cus_abc123",
  "setup_future_usage": "off_session"
}
```

## Related

- [Tutorial: 3D Secure](../tutorials/three-d-secure)
- [API Reference: Authentication](../api-reference/authentication/index)