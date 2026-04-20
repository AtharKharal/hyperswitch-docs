# How to Handle Webhooks

## Problem

You need to receive and process real-time payment event notifications from Hyperswitch.

## Solution

### Step 1: Register a Webhook

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/webhooks" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "url": "https://your-server.com/webhooks",
        "events": [
          "payment.success",
          "payment.failed",
          "refund.created",
          "dispute.created"
        ],
        "active": true
      }'
    ```

## Webhook Events

| Event | Description |
|-------|-------------|
| `payment.success` | Payment completed |
| `payment.failed` | Payment declined |
| `payment.processing` | Payment being processed |
| `refund.created` | Refund initiated |
| `refund.succeeded` | Refund completed |
| `dispute.created` | New dispute |
| `dispute.resolved` | Dispute resolved |

## Step 2: Verify Webhook Signature

=== "Python"

    ```python
    import hmac
    import hashlib
    
    def verify_webhook_signature(payload, signature, secret):
        expected = hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).digest()
        
        return hmac.compare_digest(
            signature.encode(),
            expected
        )
    
    signature = request.headers.get('x-hyperswitch-signature')
    is_valid = verify_webhook_signature(request.body, signature, 'whsec_your_secret')
    ```

## Step 3: Process the Event

```python
@app.route('/webhooks', methods=['POST'])
def handle_webhook():
    event = request.json
    
    if event['event_type'] == 'payment.success':
        order_id = event['data']['metadata']['order_id']
        mark_order_complete(order_id)
    
    return 'OK', 200
```

## Webhook Payload

```json
{
  "event_id": "evt_abc123",
  "event_type": "payment.success",
  "data": {
    "payment_id": "pay_xyz789",
    "amount": 6540,
    "currency": "USD",
    "status": "succeeded"
  },
  "created_at": "2026-04-19T12:00:00Z"
}
```

## Retry Schedule

If your server returns non-200:
- Retry 1: 1 minute
- Retry 2: 5 minutes
- Retry 3: 30 minutes
- Retry 4: 2 hours
- Retry 5: 24 hours

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/webhooks&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Related

- [API Reference: Events](../api-reference/event/index)
- [Tutorial: Webhooks](../tutorials/webhooks)