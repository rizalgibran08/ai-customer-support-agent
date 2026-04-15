import json
import random


def load_data():
    with open("data.json") as f:
        return json.load(f)


def cek_order(order_id):
    data = load_data()
    for order in data:
        if order["order_id"] == order_id:
            return order["status"]
    return "Order tidak ditemukan"


def create_ticket(issue):
    ticket_id = random.randint(1000, 9999)
    return f"Tiket berhasil dibuat dengan ID: {ticket_id} untuk masalah: {issue}"
