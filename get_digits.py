def get_digits(number: int | float) -> list[int]:
    return [int(i) for i in list(str(number).replace('.', ''))]

print(get_digits(13.909934))