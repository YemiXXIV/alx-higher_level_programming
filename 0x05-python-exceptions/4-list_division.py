#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        result = 0

        try:
            x = my_list_1[i] if i < len(my_list_1) else 0
            y = my_list_2[i] if i < len(my_list_2) else 0

            result = x / y

        except (TypeError, ZeroDivisionError) as e:
            if isinstance(e, TypeError):
                print("wrong type")
            else:
                print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)

    return result_list
