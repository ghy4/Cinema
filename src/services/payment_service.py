from flask import jsonify
import stripe

stripe.api_key = 'your_stripe_secret_key'

def create_payment_intent(amount, currency='usd'):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )
        return jsonify({'client_secret': payment_intent['client_secret']})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def confirm_payment(payment_intent_id):
    try:
        payment_intent = stripe.PaymentIntent.confirm(payment_intent_id)
        return jsonify(payment_intent)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def retrieve_payment(payment_intent_id):
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return jsonify(payment_intent)
    except Exception as e:
        return jsonify({'error': str(e)}), 400