class Bob:

    def __init__(self, public_key, degree_for_dh):
        self.primitive_root = public_key[0]
        self.mod = public_key[1]
        self.degree_for_dh = degree_for_dh

    def get_mod(self):
        return self.mod

    def get_primitive_root(self):
        return self.primitive_root

    def get_degree_for_dh(self):
        return self.degree_for_dh

    def set_mod(self, mod):
        self.mod = mod

    def set_primitive_root(self, primitive_root):
        self.primitive_root = primitive_root

    def set_degree_for_dh(self, degree):
        self.degree_for_dh = degree
