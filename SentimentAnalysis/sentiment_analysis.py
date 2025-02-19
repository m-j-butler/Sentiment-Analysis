'''
Analyzes the sentiment of the provided text using IBM Watson AI sentiment analysis
'''

import json
import requests

def sentiment_analyzer(text_to_analyse, timeout=10):
    '''
    Takes use inputted text and runs sentiment analysis using Watson AI.
    '''

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        # Sending a POST request to the sentiment analysis API with a timeout
        response = requests.post(url, json=myobj, headers=header, timeout=timeout)

        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # If the response status code is 200, extract the label and score from the response
        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']

        # If the response status code is 500, set label and score to None
        elif response.status_code == 500:
            label = None
            score = None

        # Handling other errors
        else:
            label = None
            score = None

    except requests.exceptions.Timeout:
        # Handle timeout exception
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}