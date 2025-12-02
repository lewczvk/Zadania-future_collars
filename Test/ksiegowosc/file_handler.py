import json


def load_data():
    with open("ksiegowosc_example.json") as file:
        text = file.read()
        list_text = text.split("}")
        print(list_text)
        text = json.load(file)
        print(text)

load_data()

class FileHandler:
    def __init__(self, filepath):
        self.file = filepath
        self.krotka = self.load_data_from_file()
        self.saldo = self.krotka[0]
        self.historia = self.krotka[1]
        self.system_ksiegowy = self.krotka[2]
        self.saldo, self.historia, self.system_ksiegowy = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file, encoding="utf-8") as file:
            data = json.load(file)
            return data.get("saldo"), data.get("historia"), data.get("system_ksiegowy")

    def save_data_to_file(self, new_saldo, new_historia, new_system_ksiegowy):
        with open(self.file, mode="w", encoding="utf-8") as file:
            temporary_data = {
                "saldo": new_saldo,
                "historia": new_historia,
                "system_ksiegowy": new_system_ksiegowy
            }
            file.write(json.dumps(temporary_data, indent=4, ensure_ascii=False))


file_handler = FileHandler("ksiegowosc.json")
print(file_handler.saldo)
print(file_handler.historia)
print(file_handler.ksiegowosc)