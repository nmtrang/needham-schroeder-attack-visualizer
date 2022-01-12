# Planned and coded by Trang Nguyen <pneppy@gmail.com>
# coding=utf-8
import rsa
from random import randint

"""
    Communicators in the system can be able to encrypt
    and see/decrypt messages.
    --- Attributes and methods ---
    - Each communicator can choose their nonce.
    - A communicator decrypts sender's message with their public key.
    - A communicator can check if he/she can decrypt the message.
"""


class Communicator():

    def __init__(self, name):

        self.name = name
        self.public_key, self.private_key = rsa.newkeys(512)
        self.nonce = str(randint(1, 100))

    # Alice or Bob can only send to Malice
    def send_message(self, message, other_communicator):
        self.message = message
        self.information_sent = {
            'nonce': rsa.encrypt(self.nonce.encode(), other_communicator.public_key),
            'receiver_public_key': other_communicator.public_key,
            'encrypted-message': rsa.encrypt(self.message.encode(), other_communicator.public_key)
        }

    # Alice can receive message from Malice and so does Bob
    def receive_message(self, other_communicator):
        if other_communicator.information_sent['receiver_public_key'] == self.public_key:
            message = rsa.decrypt(
                other_communicator.information_sent['encrypted-message'], self.private_key)
            return message
        else:
            # return f'Sorry! {other_communicator.name} didnt send any message to you or you dont have the proper private key to decrypt the message.'
            return other_communicator.information_sent['encrypted-message']


alice = Communicator("Alice")
bob = Communicator("Bob")
malice = Communicator("Malice")
