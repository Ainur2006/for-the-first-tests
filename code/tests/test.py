from src.capitalize import capitalize

if capitalize('text') != 'Text':
    print("Ошибка!")


if capitalize('') != '':
    print('Error')

print('Все тесты прошли!')           