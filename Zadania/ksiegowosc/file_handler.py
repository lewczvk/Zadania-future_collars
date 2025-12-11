import json

class FileHandler:
    def __init__(self, filepath):
        self.file = filepath
        self.krotka = self.load_data_from_file()
        self.saldo_firmy = self.krotka[0]
        self.historia = self.krotka[1]
        self.system_ksiegowy = self.krotka[2]
        self.saldo_firmy, self.historia, self.system_ksiegowy = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file, encoding="utf-8") as file:
            data = json.load(file)
            return data.get("saldo_firmy"), data.get("historia"), data.get("system_ksiegowy")

    def save_data_to_file(self, new_saldo_firmy, new_historia, new_system_ksiegowy):
        with open(self.file, mode="w", encoding="utf-8") as file:
            temporary_data = {
                "saldo_firmy": new_saldo_firmy,
                "historia": new_historia,
                "system_ksiegowy": new_system_ksiegowy
            }
            file.write(json.dumps(temporary_data, indent=4, ensure_ascii=False))


file_handler = FileHandler("ksiegowosc.json")
print(file_handler.saldo_firmy)
print(file_handler.historia)
print(file_handler.system_ksiegowy)