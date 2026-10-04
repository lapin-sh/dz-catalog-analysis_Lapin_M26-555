"""Домашнее задание №1. Аналитика каталога стримингового сервиса."""

import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021,
     "genres": {"sci-fi", "drama"}, "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019,
     "genres": {"comedy", "drama"}, "rating": 7.1, "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016,
     "genres": {"thriller", "drama"}, "rating": 6.4, "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023,
     "genres": {"sci-fi", "action"}, "rating": 5.9, "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014,
     "genres": {"comedy"}, "rating": 7.8, "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020,
     "genres": {"thriller", "mystery"}, "rating": 8.9, "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022,
     "genres": {"drama"}, "rating": 4.8, "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024,
     "genres": {"sci-fi", "drama"}, "rating": 9.2, "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011,
     "genres": {"comedy"}, "rating": 6.0, "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018,
     "genres": {"action", "thriller"}, "rating": 7.3, "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]


# Этап 1. Разминка: переменные, числа, math

def average_rating(catalog):
    """Возвращает средний рейтинг по каталогу (округление до одного знака)."""
    total = 0
    for movie in catalog:
        total += movie["rating"]
    return round(total / len(catalog), 1)


def catalog_age_stats(catalog, current_year=2026):
    """Возвращает кортеж: возраст самого старого, нового и средний (лет)."""
    ages = []
    for movie in catalog:
        ages.append(current_year - movie["year"])
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


# Этап 2. Условия и match

def rating_tier(rating):
    """Возвращает категорию фильма по его оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating < 5:
        return "слабо"
    else:
        return "хорошо" if rating >= 7 else "средне"


def decade_label(year):
    """Возвращает метку десятилетия через оператор match."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы

def print_non_comedy_titles(catalog):
    """Печатает названия фильмов, которые не относятся к жанру comedy."""
    for movie in catalog:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(catalog):
    """Ищет первый фильм с рейтингом выше 9.0 через while + break."""
    result = None
    i = 0
    while i < len(catalog):
        if catalog[i]["rating"] > 9.0:
            result = catalog[i]["title"]
            break
        i += 1
    else:
        print("Шедевров не найдено")
    return result


def count_long_movies(catalog, threshold=120):
    count = 0
    for movie in catalog:
        if movie["duration_min"] > threshold:
            count += 1
    return count