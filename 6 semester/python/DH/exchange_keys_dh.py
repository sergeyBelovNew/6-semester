class ExchangeKeysDH:
    def __init__(self, public_key, private_params):
        self.alise_galua_field_result = public_key[0] ** private_params[0] % public_key[1]
        self.bob_galua_field_result = public_key[0] ** private_params[1] % public_key[1]
        self.alise_private_key = self.bob_galua_field_result ** private_params[0] % public_key[1]
        self.bob_private_key = self.alise_galua_field_result ** private_params[1] % public_key[1]

    def get_alise_galua_field_result(self):
        return self.alise_galua_field_result

    def get_bob_galua_field_result(self):
        return self.bob_galua_field_result

    def get_alise_private_key(self):
        return self.alise_private_key

    def get_bob_private_key(self):
        return self.alise_private_key
