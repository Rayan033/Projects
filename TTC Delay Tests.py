"""CSC110 Fall 2024 Assignment 2, Part 3: Sentiment Analysis

Module Description
===============================
This module contains starter code for the tests for a few of the functions described in Part 3.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC110 Teaching Team
"""
from hypothesis import given
from hypothesis.strategies import lists, dictionaries, text, tuples, floats

import a2_part3


@given(word_list=lists(text()), sentiment_scores=dictionaries(text(), tuples(floats(), floats())))
def test_get_keywords_no_mut(word_list: list[str], sentiment_scores: dict[str, tuple[float, float]]) -> None:
    """Test that get_keywords does not mutate its arguments."""
    if word_list and not any(word in sentiment_scores for word in word_list):
        sentiment_scores[word_list[0]] = (0.80, 0.20)

    word_list_copy = word_list.copy()
    sentiment_scores_copy = sentiment_scores.copy()
    a2_part3.get_keywords(word_list, sentiment_scores)

    assert word_list == word_list_copy and sentiment_scores == sentiment_scores_copy


@given(word_list=lists(text(), min_size=1), sentiment_scores=dictionaries(text(), tuples(floats(), floats())))
def test_get_overall_score_no_mut(word_list: list[str], sentiment_scores: dict[str, tuple[float, float]]) -> None:
    """Test that get_overall_score does not mutate its arguments."""
    if not any(x == y for x in sentiment_scores for y in word_list):
        sentiment_scores[word_list[0]] = (0.80, 0.20)

    word_list_copy = word_list.copy()
    sentiment_scores_copy = sentiment_scores.copy()
    a2_part3.get_overall_score(word_list, sentiment_scores)

    assert word_list == word_list_copy and sentiment_scores == sentiment_scores_copy


if __name__ == '__main__':
    # DO NOT MODIFY ANY CODE BELOW (You can and should comment/uncomment them out for testing purposes though)
    import pytest

    #
    pytest.main(['test_a2_part3.py', '--disable-warnings'])
    #
    import python_ta

    #
    python_ta.check_all(config={
        'extra-imports': ['hypothesis', 'hypothesis.strategies', 'a2_part3'],
        'max-line-length': 120
    })
