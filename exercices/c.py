class Chien:

    def __init__(self):
        self.pattes = ["avant_gauche", "avant_droit", "arriere_gauche", "arriere_droit"]

    def bark(self):
        print(f"bark! i'm {self.nom}")

    def __repr__(self):
        return f"Chien nom:{self.nom}"

    def __eq__(self, rhs):
        return self.nom == rhs.nom

    def __len__(self):
        return len(self.pattes)

    def __getitem__(self, index):
        return self.pattes[index]

    def __enter__(self):
        return Chien()

    def __exit__(self, exception_type, exception_val, exception_tb):
        print("on sort")

print("avant")
with Chien() as c:
    print("pendant")