#!/usr/bin/python3

"""this the model base containing the class Base"""
import json
import csv
import turtle


class Base:
    """the class base
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """init constructor
        args: id public instance attribute"""

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries"""

        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method def save_to_file(cls, list_objs):
        that writes the JSON string representation of
        list_objs to a file:"""

        json_obj = []
        with open(f"{cls.__name__}.json", "w") as json_file:
            if list_objs is None:
                json_file.write(cls.to_json_string(list_objs))
                return
            for item in list_objs:
                json_obj.append(item.to_dictionary())
            json_file.write(cls.to_json_string(json_obj))

    def from_json_string(json_string):
        """static method def from_json_string(json_string):
        that returns the list of the JSON
        string representation json_string:"""

        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method def create(cls, **dictionary):
        that returns an instance with all
        attributes already set:"""

        dummy = cls(24, 12)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method def load_from_file(cls):"""

        lista = []
        try:
            with open(f"{cls.__name__}.json", "r") as json_file:
                data = json_file.read()
                data_string = cls.from_json_string(data)
                for datem in data_string:
                    objec = cls.create(**datem)
                    lista.append(objec)
            return lista
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """class method def load_from_file(cls):"""

        lista = []
        dic = {}
        try:
            with open(f"{cls.__name__}.csv", "r") as csv_file:
                data = csv.reader(csv_file, delimiter=',')
                fieldname = next(data)
                for datem in data:
                    for i in range(len(datem)):
                        dic[fieldname[i]] = int(datem[i])
                    objec = cls.create(**dic)
                    lista.append(objec)
            return lista
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class methods def save_to_file_csv(cls, list_objs):
        and def load_from_file_csv(cls):
        that serializes and deserializes in CSV:"""

        csv_obj = []
        lt = []
        with open(f"{cls.__name__}.csv", "w") as csv_file:
            csvwrite = csv.writer(csv_file)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fields = ["id", "size", "x", "y"]
            csv_obj.append(fields)
            for item in list_objs:
                lt = []
                for key in fields:
                    lt.append(item.to_dictionary()[key])
                csv_obj.append(lt)
            if list_objs is None:
                csvwrite.writerow([])
                return
            csvwrite.writerows(csv_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method def draw(list_rectangles, list_squares): """

        pass

