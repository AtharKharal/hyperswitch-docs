# Payment Methods

Reference documentation for payment methods API endpoints.

## Endpoints

### [POST /payment_methods](post--payment_methods)

PaymentMethods - Create

### [GET /account/payment_methods](get--account-payment_methods)

List payment methods for a Merchant

### [GET /customers/{customer_id}/payment_methods](get--customers-customer_id-payment_methods)

List payment methods for a Customer

### [GET /customers/payment_methods](get--customers-payment_methods)

List customer saved payment methods for a Payment

### [POST /{customer_id}/payment_methods/{payment_method_id}/default](post--customer_id-payment_methods-payment_method_id-default)

Payment Method - Set Default Payment Method for Customer

### [GET /payment_methods/{method_id}](get--payment_methods-method_id)

Payment Method - Retrieve

### [DELETE /payment_methods/{method_id}](delete--payment_methods-method_id)

Payment Method - Delete

### [POST /payment_methods/{method_id}/update](post--payment_methods-method_id-update)

Payment Method - Update


## Playground

Test these endpoints in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground?category=payment-methods).
