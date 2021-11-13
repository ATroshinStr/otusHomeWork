import json
import csv


def open_file_json(filepath):
    with open(filepath) as global_file:
        users = json.load(global_file)
    return users


def open_file_csv(filepath):
    book_fields = ('title', 'author', 'pages', 'genre')
    with open(filepath) as global_file:
        reader_csv = csv.DictReader(global_file)
        books = [{key.lower(): value for key, value in book.items()
                 if key.lower() in book_fields}
                 for book in reader_csv]
    return books


def result_users(users):
    users = [
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        } for user in users]
    return users


def result_file(users_list, books_list):
    users = result_users(users_list)
    books = books_list.copy()
    while books:
        for user in users:
            if not books:
                break
            user['books'].append(books.pop())
    return users


def write_result_json(final_json):
    with open("result.json", "w") as global_file:
        json.dump(final_json, global_file,  indent=4)


users_list_json = open_file_json('users-39204-8e2f95.json')
books_list_csv = open_file_csv('books-133064-871075.csv')
result_write = result_file(users_list_json, books_list_csv)
write_result_json(result_write)


