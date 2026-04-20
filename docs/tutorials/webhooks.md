# Webhooks

## Prerequisites

- [Quick Start](quickstart) - Complete the quick start to understand basic payment flows
- [Customers](customers) - Understand customer-related events

## Overview

Hyperswitch sends real-time webhook notifications for payment events. Webhooks enable:
- Server-side payment confirmation
- Automated refunds on failure
- Customer notifications
- Analytics updates

## Supported Events

| Event | Description |
|-------|-------------|
| `payment.success` | Payment completed successfully |
| `payment.failed` | Payment failed |
| `refund.created` | Refund initiated |
| `refund.processed` | Refund completed |
| `dispute.created` | New dispute opened |
| `customer.created` | Customer profile created |

## Verify Webhook Signatures

Always verify the webhook signature to ensure authenticity:

=== "Python"

    ```python
    import hmac
    import hashlib
    
    def verify_webhook(payload, signature, secret):
        expected = hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(signature, expected)
    
    payload = request.body
    signature = request.headers['x-hyperswitch-signature']
    secret = "whsec_your_webhook_secret"
    
    if not verify_webhook(payload, signature, secret):
        return 401, "Invalid signature"
    ```

=== "JavaScript"

    ```javascript
    const crypto = require('crypto');
    
    function verifyWebhook(payload, signature, secret) {
      const expected = crypto
        .createHmac('sha256', secret)
        .update(payload)
        .digest('hex');
      return crypto.timingSafeEqual(
        Buffer.from(signature),
        Buffer.from(expected)
      );
    }
    ```

## Webhook Payload Structure

```json
{
  "event_id": "evt_abc123",
  "event_type": "payment.success",
  "data": {
    "payment_id": "pay_xyz789",
    "amount": 6540,
    "currency": "USD",
    "status": "succeeded",
    "customer_id": "cus_abc123"
  },
  "created_at": "2026-04-19T12:00:00Z"
}
```

## Endpoint Configuration

Configure webhooks in the [Hyperswitch Dashboard](https://app.hyperswitch.io) under Developers → Webhooks.

### Create Webhook

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/webhooks" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "url": "https://your-server.com/webhook",
        "events": ["payment.success", "payment.failed"],
        "active": true
      }'
    ```

## Retry Failed Webhooks

Hyperswitch automatically retries failed webhooks with exponential backoff:

1. First retry: 1 minute
2. Second retry: 5 minutes  
3. Third retry: 30 minutes
4. Fourth retry: 2 hours
5. Final retry: 24 hours

## Playground

Configure and test webhooks in the [Hyperswitch Dashboard](https://app.hyperswitch.io).

## Best Practices

1. **Always verify signatures** - Prevent fake webhook attacks
2. **Respond within 30 seconds** - Return 200 OK quickly
3. **Process asynchronously** - Queue events for later processing
4. **Handle duplicates** - Webhooks may be sent multiple times

## Related

- [API Reference: Events](../api-reference/event/index)
- [How-To: Handle Webhooks](../howto/handle-webhooks)