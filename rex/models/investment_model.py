import datetime
from mongokit import Document
from rex import app, db
import validators

__author__ = 'taijoe'


class Investment(Document):
    __collection__ = 'investment'

    structure = {
        'uid' : unicode,
        'user_id': unicode,
        'username' : unicode,
        'amount_usd' : float,
        'package' : float,
        'package_string' : unicode,
        'status' : int,
        'date_added' : datetime.datetime,
        'amount_frofit' : float,
        'upgrade' : int,
        'coin_amount' : float,
        'date_upgrade' : datetime.datetime,
        'reinvest' : int,
        'total_income' : float,
        'status_income' : int,
        'date_income' : datetime.datetime,
        'date_profit' : datetime.datetime,
        'currency' : unicode
    }
    default_values = {
        'date_added': datetime.datetime.utcnow()
        }
    use_dot_notation = True

db.register([Investment])