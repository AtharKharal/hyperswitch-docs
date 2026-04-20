# Payment Flows

## Overview

Understanding how payments move through the Hyperswitch system.

## Payment Lifecycle

### 1. Initiate
```json
{
  "amount": 5000,
  "currency": "USD"
}
```

### 2. Process
The payment goes through:
- **Validation** - Check request
- **Authentication** - Verify 3DS if needed
- **Routing** - Choose connector(s)
- **Authorization** - Contact processor

### 3. Resolve
Final states:
- `succeeded` - Complete
- `failed` - Declined
- `pending` - Awaiting

## Card Payment Flow

```
┌──────────┐     ┌─────────────┐     ┌────────────┐     ┌────────────┐
│ Customer │────→│ Your App  │────→│Hyperswitch│────→│ Processor│
└──────────┘     └─────────────┘     └────────────┘     └────────────┘
                                              ↓
                                         ┌────────────┐
                                         │   VISA   │
                                         └────────────┘
```

## 3DS Flow

```
┌──────────┐     ┌─────────────┐     ┌────────────┐     ┌──────────┐
│ Customer │────→│ Hyperswitch │────→│   Bank   │────→│ 3DS UI   │
└──────────┘     │ (requires │     │  (auth)  │     └──────────┘
                 │  3DS)    │
                 └────────────┘
```

## Webhook Integration

```python
@app.route('/webhooks')
def handle_webhook():
    event = request.json
    
    if event['event_type'] == 'payment.success':
        fulfill_order(event['data']['payment_id'])
    
    return 'OK', 200
```

## Playground

Explore flows in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground).

## Related

- [API Reference: Payments](../api-reference/payments/index)
- [Tutorial: Quick Start](../tutorials/quickstart)