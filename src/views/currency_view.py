from flask import request, jsonify
from ..models.currency_model import get_conversion_rate


def convert_currency():
    from_currency = request.args.get('from', '').lower()
    to_currency = request.args.get('to', '').lower()
    amount = float(request.args.get('amount', 1))

    try:
        converted_amount = get_conversion_rate(
            from_currency, to_currency, amount
            )
        return jsonify({'converted_amount': converted_amount})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


# def convert_currency():
#     from_currency = request.args.get('from')
#     to_currency = request.args.get('to')
#     amount = request.args.get('amount')

#     if not from_currency or not to_currency or not amount:
#         return jsonify({'error': 'Missing required parameters'}), 400

#     try:
#         amount = float(amount)
#     except ValueError:
#         return jsonify({'error': 'Invalid amount'}), 400

#     try:
#         converted_amount = get_conversion_rate(
# from_currency, to_currency, amount
# )
#         return jsonify({
#             'from': from_currency,
#             'to': to_currency,
#             'amount': amount,
#             'converted_amount': converted_amount,
#         })
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 400
