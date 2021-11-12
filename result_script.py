import json
import csv
from csv import reader
from csv import DictReader


def open_file_json(filepath):
    with open(filepath) as global_file:
        users = json.load(global_file)
    return users


def open_file_csv():
    with open("../otusHomeWork/books-133064-871075.csv", newline='') as global_file:
        books = reader(global_file)
        books_list = books
    return books_list


def result_file(users):
    users = [
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        } for user in users]
    return users


def write_result_json(final_json):
    with open("../otusHomeWork/result.json", "w") as global_file:
        json.dump(final_json, global_file,  indent=4)


if __name__ == '__main__':
    users_list = open_file_json('users-39204-8e2f95.json')
    result_write = result_file(users_list)
    write_result_json(result_write)


