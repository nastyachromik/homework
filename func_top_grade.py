def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:

    top_gr = max(grades['grades'])
    return {'name': grades['name'], 'top_grade': top_gr}

info = {'name': 'Timur', 'grades': [30, 57, 99]}
print(top_grade(info))