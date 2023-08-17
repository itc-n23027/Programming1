name_age = {"tantaka": 35, "satou": 25, "suzuki": 27}


def dict_info(dict_tdl, key):
    try:
        return dict_tdl[key]
    except:
        return "key is not found"


print(dict_info(name_age, "satou"))
print(dict_info(name_age, "yamada"))
