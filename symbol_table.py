class SymTable:
    def fetch(self, var_name):
        # returns address, type (int, double, string, ...)
        pass

    def get_label(self, command):
        # command \in {"while", "if", "for", ...}
        # returns labels like "WHILE00", ...
        pass
