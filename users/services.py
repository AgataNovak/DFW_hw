import stripe

stripe.api_key = 'sk_test_51QdvsGFalMPBmV7YvqxMbF4IPt7yEMx6VId7IYu0JI7UtzrM0ukUDpMz8C152CcGdt4djJefdC1NWxBuGvri5RMC007O0yfIop'


def create_stripe_product(product):

    stripe.Product.create(
        name=product
    )


def create_stripe_price(amount):

    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Payment"}
    )
    return price


def create_stripe_session(price):

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/education/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')

