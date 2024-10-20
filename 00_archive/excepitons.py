try:
    print("try: пробуем сделать что-нибудь")
    dct = {}
    val = dct["key"]
except KeyError as exception:
    print(f"except: try выкинул ошибку {exception}")
else:
    print("else: try не выкинул ошибку")
finally:
    print("finally: выполняем всегда")
