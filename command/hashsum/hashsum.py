import base64
import binascii
import hashlib
from command.model import CommandSet


class HashSum(CommandSet):
    _name = 'hashsum'

class Base64(CommandSet):
    _name = 'base64'

    def command(self, *args, **kwargs):
        input_file = args[0]
        if input_file:
            if "-d" in args:
                encoded_data = base64.b64decode(bytes(input_file, encoding='utf-8'))
                decoded_data = base64.b64decode(encoded_data + b"==").decode()
                print(decoded_data)
            else:
                encoded_data = base64.b64encode(bytes(input_file, encoding='utf-8'))
                print(encoded_data.decode())

class Base32(CommandSet):
    pass

class SHA1Sum(CommandSet):
    _name = 'sha1sum'

    def command(self, *args, **kwargs):
        input_file = args[0]
        if input_file:
            print(hashlib.sha1(bytes(input_file, encoding='utf-8')).hexdigest())

class SHA256Sum(CommandSet):
    _name = 'sha256sum'

    def command(self, *args, **kwargs):
        input_file = args[0]
        if input_file:
            print(hashlib.sha256(bytes(input_file, encoding='utf-8')).hexdigest())
