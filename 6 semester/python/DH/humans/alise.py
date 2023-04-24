class Alise:
    def __init__(self, primitive_root, mod, degree_for_dh):
        self.primitive_root = primitive_root
        self.mod = mod
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
