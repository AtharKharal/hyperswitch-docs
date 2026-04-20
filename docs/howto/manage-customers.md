# How to Manage Customers

## Problem

You need to create and manage customer profiles to enable:
- Saved payment methods
- Customer dashboard
- Subscription management

## Solution

### Create Customer

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/customers" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "email": "customer@example.com",
        "name": "John Doe",
        "phone": "+1234567890",
        "metadata": {
          "tier": "premium"
        }
      }'
    ```

## Attach Payment Method

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/payment_methods" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "customer_id": "cus_abc123",
        "payment_method": {
          "card": {
            "card_number": "4242424242424242",
            "exp_month": "12",
            "exp_year": "2027",
            "cvc": "123"
          }
        }
      }'
    ```

## List Customer Payment Methods

=== "cURL"

    ```bash
    curl -X GET "https://sandbox.hyperswitch.io/customers/cus_abc123/payment_methods" \
      -H "api-key: sk_snd_your_api_key"
    ```

## Update Customer

=== "cURL"

    ```bash
    curl -X POST "https://sandbox.hyperswitch.io/customers/cus_abc123" \
      -H "Content-Type: application/json" \
      -H "api-key: sk_snd_your_api_key" \
      -d '{
        "email": "new.email@example.com",
        "metadata": {
          "tier": "vip",
          "since": "2024"
        }
      }'
    ```

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/customers&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Related

- [API Reference: Customers](../api-reference/customers/index)
- [Tutorial: Customer Management](../tutorials/customers)