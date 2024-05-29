from src.app import create_app
import importlib.metadata
# import werkzeug
from flask import Flask


def test_home_page():
    app = create_app()
    client = app.test_client()
    user_agent = f"werkzeug/{importlib.metadata.version('werkzeug')}"
    with client as c:
        response = c.get('/', headers={"User-Agent": user_agent})
        assert response.status_code == 200
        assert 'Conversor Monetário' in response.data.decode('utf')


def test_conversion_usd_to_brl():
    app = create_app()
    client = app.test_client()
    response = client.get('/convert?from=USD&to=BRL&amount=1')
    data = response.get_json()
    assert 'converted_amount' in data
    assert isinstance(data['converted_amount'], float)


def test_conversion_invalid_currency():
    app = create_app()
    client = app.test_client()
    response = client.get('/convert?from=XXX&to=BRL&amount=1')
    data = response.get_json()
    assert 'error' in data
