"""Tests for simple_utils.py"""

import pytest

from simple_utils import celsius_to_fahrenheit, count_words, reverse_string


class TestReverseString:
    def test_basic_string(self):
        assert reverse_string("hello") == "olleh"

    def test_empty_string(self):
        assert reverse_string("") == ""

    def test_single_character(self):
        assert reverse_string("a") == "a"

    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"

    def test_string_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_string_with_numbers(self):
        assert reverse_string("abc123") == "321cba"

    def test_special_characters(self):
        assert reverse_string("!@#$") == "$#@!"

    def test_unicode_characters(self):
        assert reverse_string("café") == "éfac"

    def test_whitespace_only(self):
        assert reverse_string("   ") == "   "

    def test_mixed_case(self):
        assert reverse_string("Hello") == "olleH"

    def test_returns_string_type(self):
        result = reverse_string("test")
        assert isinstance(result, str)


class TestCountWords:
    def test_basic_sentence(self):
        assert count_words("hello world") == 2

    def test_empty_string(self):
        assert count_words("") == 0

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_multiple_words(self):
        assert count_words("the quick brown fox") == 4

    def test_multiple_spaces_between_words(self):
        # str.split() with no argument splits on any whitespace and ignores extras
        assert count_words("hello   world") == 2

    def test_leading_spaces(self):
        assert count_words("  hello world") == 2

    def test_trailing_spaces(self):
        assert count_words("hello world  ") == 2

    def test_leading_and_trailing_spaces(self):
        assert count_words("  hello world  ") == 2

    def test_tabs_as_whitespace(self):
        assert count_words("hello\tworld") == 2

    def test_newlines_as_whitespace(self):
        assert count_words("hello\nworld") == 2

    def test_whitespace_only(self):
        assert count_words("   ") == 0

    def test_single_character_words(self):
        assert count_words("a b c") == 3

    def test_returns_int_type(self):
        result = count_words("hello world")
        assert isinstance(result, int)


class TestCelsiusToFahrenheit:
    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_crossover_point(self):
        # -40 is the point where Celsius and Fahrenheit are equal
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_body_temperature(self):
        assert celsius_to_fahrenheit(37) == pytest.approx(98.6, rel=1e-3)

    def test_negative_temperature(self):
        assert celsius_to_fahrenheit(-10) == 14.0

    def test_float_input(self):
        assert celsius_to_fahrenheit(0.0) == 32.0

    def test_float_celsius(self):
        assert celsius_to_fahrenheit(20.5) == pytest.approx(68.9, rel=1e-4)

    def test_large_value(self):
        assert celsius_to_fahrenheit(1000) == 1832.0

    def test_room_temperature(self):
        assert celsius_to_fahrenheit(20) == 68.0

    def test_returns_float_type(self):
        result = celsius_to_fahrenheit(0)
        assert isinstance(result, float)

    def test_formula_correctness(self):
        # Verify the formula: F = (C * 9/5) + 32 for a known value
        celsius = 25
        expected = (25 * 9 / 5) + 32  # 77.0
        assert celsius_to_fahrenheit(celsius) == expected
