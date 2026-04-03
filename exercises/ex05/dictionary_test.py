"""Testing dictionary functions"""

__author__ = "730705811"

from exercises.ex05.dictionary import invert


def test_invert_multiple() -> None:
    """Use case: Inverting a dictionary with many values"""
    dictionary: dict[str, str] = {"a": "anna", "b": "bella", "c": "connor"}
    result = invert(dictionary)
    assert result == {"anna": "a", "bella": "b", "connor": "c"}


def test_invert_single() -> None:
    """Use case: Inverting a dictionary with one value"""
    dictionary: dict[str, str] = {"s": "shivani"}
    result = invert(dictionary)
    assert result == {"shivani": "s"}


import pytest


def test_invert_edge() -> None:
    """Edge case: Duplicate values so duplicate keys in new dictionary"""
    with pytest.raises(KeyError):
        dictionary: dict[str, str] = {"s": "shivani", "a": "shivani"}
        invert(dictionary)


from exercises.ex05.dictionary import favorite_color


def test_favorite_color_multiple() -> None:
    """Use case: Finding most popular color in dictionary with many values"""
    dictionary: dict[str, str] = {"anna": "pink", "bella": "blue", "connor": "blue"}
    result = favorite_color(dictionary)
    assert result == "blue"


def test_favorite_color_single() -> None:
    """Use case: Finding most popular color in dictionary with one value"""
    dictionary: dict[str, str] = {"anna": "pink"}
    result = favorite_color(dictionary)
    assert result == "pink"


def test_favorite_color_edge() -> None:
    """Edge case: Finding most popular color in empty dictionary"""
    dictionary: dict[str, str] = {}
    result = favorite_color(dictionary)
    assert result == ""


from exercises.ex05.dictionary import count


def test_count_multiple() -> None:
    """Use case: Finding number of times something appears in dictionary when the list has many values"""
    value_list: list[str] = ["red", "pink", "blue", "pink"]
    result = count(value_list)
    assert result == {"red": 1, "pink": 2, "blue": 1}


def test_count_single() -> None:
    """Use case: Finding number of times something appears in dictionary when the list only has one value"""
    value_list: list[str] = {"red"}
    result = count(value_list)
    assert result == {"red": 1}


def test_count_edge() -> None:
    """Edge case: Finding number of times something appears in dictionary when the list is empty"""
    value_list: list[str] = {}
    result = count(value_list)
    assert result == {}


from exercises.ex05.dictionary import alphabetizer


def test_alphabetizer_multiple() -> None:
    """Use case: Alphabetizing a list when the list has many values"""
    random: list[str] = {"red", "pink", "pine"}
    result = alphabetizer(random)
    assert result == {"r": ["red"], "p": ["pink", "pine"]}


def test_alphabetizer_single() -> None:
    """Use case: Alphabetizing a list when the list only has one value"""
    random: list[str] = {"red"}
    result = alphabetizer(random)
    assert result == {"r": ["red"]}


def test_alphabetizer_edge() -> None:
    """Edge case: Alphabetizing a list when the list is empty"""
    random: list[str] = {}
    result = alphabetizer(random)
    assert result == {}


from exercises.ex05.dictionary import update_attendance


def test_update_attendance_existing() -> None:
    """Use case: Updating attendance for a day in the attendance log"""
    attendance_log: dict[str, list[str]] = {
        "Monday": ["anna", "bella"],
        "Tuesday": ["anna", "bella"],
    }
    update_attendance(attendance_log, "Monday", "connor")
    assert attendance_log == {
        "Monday": ["anna", "bella", "connor"],
        "Tuesday": ["anna", "bella"],
    }


def test_update_attendance_new() -> None:
    """Use case: Updating attendance for a day not in the attendance log"""
    attendance_log: dict[str, list[str]] = {
        "Monday": ["anna", "bella"],
        "Tuesday": ["anna", "bella"],
    }

    update_attendance(attendance_log, "Wednesday", "connor")
    assert attendance_log == {
        "Monday": ["anna", "bella"],
        "Tuesday": ["anna", "bella"],
        "Wednesday": ["connor"],
    }


def test_update_attendance_edge() -> None:
    """Edge case: Updating attendance when the student's name isn't given"""
    attendance_log: dict[str, list[str]] = {
        "Monday": ["anna", "bella"],
        "Tuesday": ["anna", "bella"],
    }
    update_attendance(attendance_log, "Monday", "")
    assert attendance_log == {
        "Monday": ["anna", "bella", ""],
        "Tuesday": ["anna", "bella"],
    }
