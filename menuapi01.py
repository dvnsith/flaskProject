#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)

menu = [{
        "appetizers": [
            {
                "name": "Pork Gyoza",
                "price": 10,
            },
            {
                "name": "Edamame",
                "price": 4,
            },
            {
                "name": "Chicken Karaage",
                "price": 8,
            },
            {
                "name": "Takoyaki",
                "price": 7,
            }
        ],
        "main": [
            {
                "name": "Tonkotsu Ramen",
                "price": 15,
            },
            {
                "name": "Miso Ramen",
                "price": 15,
            },
            {
                "name": "Chashu Bowl",
                "price": 6,
            },
            {
                "name": "Karaage Bowl",
                "price": 6,
            }
        ],
        "drinks": [
            {
                "name": "Green Tea",
                "price": 2,
            },
            {
                "name": "Sapporo",
                "price": 5,
            }
        ]
        }]


@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(menu)


if __name__ == "__main__":
    app.run(port=3000)
