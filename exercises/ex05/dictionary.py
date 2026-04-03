"""Dictionary practice."""

__author__ = "730705811"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Flip key and value."""
    new_dictionary: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        if value in new_dictionary:
            raise KeyError("Can't have duplicate keys!")
        new_dictionary[value] = key
    return new_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """Return name of most popular color."""
    color_count: dict[str, int] = {}
    for key in dictionary:
        value = dictionary[key]
        if dictionary[key] in color_count:
            color_count[value] += 1
        else:
            color_count[value] = 1
    popular_color: str = ""
    max_count: int = 0
    for key in color_count:
        if color_count[key] > max_count:
            max_count = color_count[key]
            popular_color = key
    return popular_color


def count(value_list: list[str]) -> dict[str, int]:
    """Number of times smt appears in dictionary."""
    new: dict[str, int] = {}
    for value in value_list:
        if value in new:
            new[value] += 1
        else:
            new[value] = 1
    return new


def alphabetizer(random: list[str]) -> dict[str, list[str]]:
    """Put together words that start with same alphabet."""
    alphabetized: dict[str, list[str]] = {}
    for value in random:
        first_letter: str = value[0].lower()
        if value.isalpha():
            if first_letter in alphabetized:
                alphabetized[first_letter].append(value)
            else:
                alphabetized[first_letter] = [value]
    return alphabetized


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Update attendance."""
    if day in attendance_log:
        attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
