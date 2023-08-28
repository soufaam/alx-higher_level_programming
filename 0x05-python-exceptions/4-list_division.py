#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for idx in range(list_length):
        try:
            lst.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            lst.append(0)
            print("{}".format("division by 0"))
        except IndexError:
            lst.append(0)
            print("{}".format("out of range"))
        except TypeError:
            lst.append(0)
            print("{}".format("wrong type"))
        finally:
            pass
    return lst
