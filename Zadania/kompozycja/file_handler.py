import csv
from abc import ABC, abstractmethod
import pickle

class FileHandler(ABC):
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.transformations = transformations
        self.data = None

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    def do_transformations(self):
        for transformation in self.transformations:
            # print(transformation)
            transformation_list = transformation.split(",")
            # print(transformation_list)
            y = transformation_list[0]
            x = transformation_list[1]
            value = transformation_list[2]
            self.data[int(y)][int(x)] = value
            print(self.data)




class CSVFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file, delimiter=',')
            temp_matrix_macierz = []
            for row in reader:
                print(row)
                temp_matrix_macierz.append(row)
                print(temp_matrix_macierz)
            return temp_matrix_macierz
    def save_data(self):
        with open(self.output_file, mode="w+") as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

class TxtFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file, delimiter=',')
            temp_matrix_macierz = []
            for row in reader:
                print(row)
                temp_matrix_macierz.append(row)
                print(temp_matrix_macierz)
            return temp_matrix_macierz

    def save_data(self):
        with open(self.output_file, mode="w+") as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

class PickleFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, "rb") as file:
            pass

    def save_data(self):
        with open(self.output_file, "wb+") as file:
            pass