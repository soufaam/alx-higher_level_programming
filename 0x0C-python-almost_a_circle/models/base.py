#!/usr/bin/python3

"""this the model base containing the class Base"""
import json


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
