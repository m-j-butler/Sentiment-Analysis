"""
Sentiment Analysis Package
==========================

This package provides tools for analyzing the sentiment of text using 
external IBM Watson AI sentiment analysis service.

Modules
-------
- sentiment_analysis: Contains the `sentiment_analyzer` function for performing sentiment analysis.

Example Usage
-------------
Here's an example of how to use this package:

    from sentiment_analysis import sentiment_analyzer

    # Example function usage
    result = sentiment_analyzer("I love programming!")
    print(result)  # Output: {'label': 'positive', 'score': 0.95}
"""

from . import sentiment_analysis