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


# Этап 4. Строки

def normalize_title(title):
    """Приводит строку к Title Case без использования str.title()."""
    words = title.split(" ")
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:])
    return " ".join(new_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Собирает строку с описанием фильма для отчета."""
    genres = ", ".join(sorted(movie["genres"]))
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    return (f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
            f'{duration}, жанры: {genres}')


# Этап 5. Списки

def titles_sorted_by_rating(catalog):
    """Возвращает названия фильмов по убыванию рейтинга."""
    sorted_movies = sorted(catalog, key=lambda movie: movie["rating"], reverse=True)
    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles


def top_n_by_rating(catalog, n=3):
    sorted_movies = sorted(catalog, key=lambda movie: movie["rating"], reverse=True)
    top = []
    for movie in sorted_movies[:n]:
        top.append((movie["title"], movie["rating"]))
    return top


# Этап 6. Словари

def count_by_genre(catalog):
    """Возвращает словарь {жанр: количество фильмов} через dict.get()."""
    counts = {}
    for movie in catalog:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(catalog):
    """Возвращает словарь {актер: список фильмов с его участием}."""
    filmography = {}
    for movie in catalog:
        for actor in movie["actors"]:
            films = filmography.get(actor, [])
            films.append(movie["title"])
            filmography[actor] = films
    return filmography


def high_rated_titles(catalog):
    """Генератор словаря {название: рейтинг} для фильмов выше среднего."""
    average = average_rating(catalog)
    return {movie["title"]: movie["rating"] for movie in catalog
            if movie["rating"] > average}


# Этап 7. Множества

def all_genres(catalog):
    """Возвращает множество всех уникальных жанров каталога."""
    genres = set()
    for movie in catalog:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(catalog_a, catalog_b):
    """Возвращает жанры, которые есть в catalog_a, но нет в catalog_b."""
    return all_genres(catalog_a) - all_genres(catalog_b)


# Этап 8. Итераторы и генераторы

def iter_high_rated(catalog, min_rating=8.0):
    """Генератор: отдает фильмы с рейтингом не ниже min_rating."""
    for movie in catalog:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated(catalog):
    """Печатает строки отчета по фильмам с рейтингом не ниже 8.0."""
    for movie in iter_high_rated(catalog):
        print(format_report_line(movie))


def total_duration_high_rated(catalog):
    """Считает суммарную длительность фильмов с рейтингом выше 7."""
    return sum(movie["duration_min"] for movie in catalog if movie["rating"] > 7)


# Этап 9. Итоговый отчет

def build_report(catalog):
    """Собирает и печатает итоговый отчет по каталогу."""
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(catalog)}")
    oldest, newest, average_age = catalog_age_stats(catalog)
    print(f"Средний возраст фильмов: {average_age} лет")

    print("Топ-3 фильма:")
    for title, rating in top_n_by_rating(catalog, 3):
        for movie in catalog:
            if movie["title"] == title:
                print(f"  {format_report_line(movie)}")

    counts = count_by_genre(catalog)
    genre_names = sorted(counts)
    # сортировка стабильная: при равном количестве жанры остаются по алфавиту
    genre_names.sort(key=lambda genre: counts[genre], reverse=True)
    print("Фильмов по жанрам:")
    for genre in genre_names:
        print(f"  {genre} — {counts[genre]}")

    genres_line = ", ".join(sorted(all_genres(catalog)))
    print(f"Все жанры каталога: {genres_line}")


if __name__ == "__main__":
    build_report(movies)
