# How to Process a Refund

## Problem

A customer requests a refund for a completed payment.

## Solution

Hyperswitch supports full and partial refunds:

### Full Refund

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/refunds" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "payment_id": "pay_abc123xyz"
      }'
    ```

### Partial Refund

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/refunds" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "payment_id": "pay_abc123xyz",
        "amount": 3000,
        "reason": "requested_by_customer"
      }'
    ```

## Refund Reasons

| Reason | Description |
|--------|-------------|
| `duplicate` | Double charge |
| `fraudulent` | Suspected fraud |
| `requested_by_customer` | Customer requested |

## Response

```json
{
  "refund_id": "ref_xyz789",
  "payment_id": "pay_abc123xyz",
  "amount": 6540,
  "currency": "USD",
  "status": "succeeded"
}
```

## Check Refund Status

=== "cURL"

    ```bash
    curl -X GET "https://sandbox.hyperswitch.io/refunds/ref_xyz789" \
      -H "api-key: sk_snd_your_api_key"
    ```

## List Refunds

=== "cURL"

    ```bash
    curl -X GET "https://sandbox.hyperswitch.io/refunds/list?payment_id=pay_abc123xyz" \
      -H "api-key: sk_snd_your_api_key"
    ```

## Refund Rules

- **Timing** - Refunds within 180 days of payment
- **Partial** - Up to original payment amount
- **Currency** - Same as original payment
- **Fees** - Processing fees may be refunded

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/refunds&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Related

- [API Reference: Refunds](../api-reference/refunds/index)
- [Tutorial: Process Refunds](../tutorials/process-refunds)