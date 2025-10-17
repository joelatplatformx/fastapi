import os
import stripe

stripe.api_key = os.getenv("STRIPQE_SECRET")

products = stripe.Product.list(limit=10)

for product in products.data:
    print(product)
