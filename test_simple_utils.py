"""Tests for simple_utils.py"""

import pytest

from simple_utils import celsius_to_fahrenheit, count_words, reverse_string


class TestReverseString:
    """Unit tests for the reverse_string function."""

    def test_basic_string(self):
        """Test that a basic string is correctly reversed."""
        assert reverse_string("hello") == "olleh"

    def test_empty_string(self):
        """Test that an empty string returns an empty string."""
        assert reverse_string("") == ""

    def test_single_character(self):
        """Test that a single character string returns the same character."""
        assert reverse_string("a") == "a"

    def test_palindrome(self):
        """Test that a palindrome string returns itself when reversed."""
        assert reverse_string("racecar") == "racecar"

    def test_string_with_spaces(self):
        """Test that a string containing spaces is correctly reversed."""
        assert reverse_string("hello world") == "dlrow olleh"

    def test_string_with_numbers(self):
        """Test that a string containing numbers is correctly reversed."""
        assert reverse_string("abc123") == "321cba"

    def test_special_characters(self):
        """Test that a string of special characters is correctly reversed."""
        assert reverse_string("!@#$") == "$#@!"

    def test_unicode_characters(self):
        """Test that a string with unicode characters is correctly reversed."""
        assert reverse_string("café") == "éfac"

    def test_whitespace_only(self):
        """Test that a whitespace-only string is correctly reversed."""
        assert reverse_string("   ") == "   "

    def test_mixed_case(self):
        """Test that a mixed-case string is reversed while preserving case."""
        assert reverse_string("Hello") == "olleH"

    def test_returns_string_type(self):
        """Test that reverse_string returns a value of type str."""
        result = reverse_string("test")
        assert isinstance(result, str)


class TestCountWords:
    """Unit tests for the count_words function."""

    def test_basic_sentence(self):
        """Test that a basic two-word sentence returns a word count of 2."""
        assert count_words("hello world") == 2

    def test_empty_string(self):
        """Test that an empty string returns a word count of 0."""
        assert count_words("") == 0

    def test_single_word(self):
        """Test that a single word returns a word count of 1."""
        assert count_words("hello") == 1

    def test_multiple_words(self):
        """Test that a sentence with multiple words returns the correct count."""
        assert count_words("the quick brown fox") == 4

    def test_multiple_spaces_between_words(self):
        """Test that multiple spaces between words are treated as a single delimiter."""
        # str.split() with no argument splits on any whitespace and ignores extras
        assert count_words("hello   world") == 2

    def test_leading_spaces(self):
        """Test that leading spaces do not affect the word count."""
        assert count_words("  hello world") == 2

    def test_trailing_spaces(self):
        """Test that trailing spaces do not affect the word count."""
        assert count_words("hello world  ") == 2

    def test_leading_and_trailing_spaces(self):
        """Test that both leading and trailing spaces do not affect the word count."""
        assert count_words("  hello world  ") == 2

    def test_tabs_as_whitespace(self):
        """Test that tab characters are treated as word delimiters."""
        assert count_words("hello\tworld") == 2

    def test_newlines_as_whitespace(self):
        """Test that newline characters are treated as word delimiters."""
        assert count_words("hello\nworld") == 2

    def test_whitespace_only(self):
        """Test that a whitespace-only string returns a word count of 0."""
        assert count_words("   ") == 0

    def test_single_character_words(self):
        """Test that single-character tokens separated by spaces are counted correctly."""
        assert count_words("a b c") == 3

    def test_returns_int_type(self):
        """Test that count_words returns a value of type int."""
        result = count_words("hello world")
        assert isinstance(result, int)


class TestCelsiusToFahrenheit:
    """Unit tests for the celsius_to_fahrenheit function."""

    def test_freezing_point(self):
        """Test that 0°C (water freezing point) converts to 32.0°F."""
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        """Test that 100°C (water boiling point) converts to 212.0°F."""
        assert celsius_to_fahrenheit(100) == 212.0

    def test_crossover_point(self):
        """Test that -40°C converts to -40.0°F, the crossover point of both scales."""
        # -40 is the point where Celsius and Fahrenheit are equal
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_body_temperature(self):
        """Test that 37°C (normal human body temperature) converts to approximately 98.6°F."""
        assert celsius_to_fahrenheit(37) == pytest.approx(98.6, rel=1e-3)

    def test_negative_temperature(self):
        """Test that a negative Celsius value converts correctly to Fahrenheit."""
        assert celsius_to_fahrenheit(-10) == 14.0

    def test_float_input(self):
        """Test that a float input of 0.0°C converts to 32.0°F."""
        assert celsius_to_fahrenheit(0.0) == 32.0

    def test_float_celsius(self):
        """Test that a fractional Celsius value converts correctly to Fahrenheit."""
        assert celsius_to_fahrenheit(20.5) == pytest.approx(68.9, rel=1e-4)

    def test_large_value(self):
        """Test that a large Celsius value converts correctly to Fahrenheit."""
        assert celsius_to_fahrenheit(1000) == 1832.0

    def test_room_temperature(self):
        """Test that 20°C (typical room temperature) converts to 68.0°F."""
        assert celsius_to_fahrenheit(20) == 68.0

    def test_returns_float_type(self):
        """Test that celsius_to_fahrenheit returns a value of type float."""
        result = celsius_to_fahrenheit(0)
        assert isinstance(result, float)

    def test_formula_correctness(self):
        """Test that the conversion follows the formula F = (C * 9/5) + 32."""
        # Verify the formula: F = (C * 9/5) + 32 for a known value
        celsius = 25
        expected = (25 * 9 / 5) + 32  # 77.0

