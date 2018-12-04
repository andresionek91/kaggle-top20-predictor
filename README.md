# Kaggle Top20 Predictor

This code was developed to be implemented at AWS Lambda. It executes the prediction step of a model developed from [Kaggle's second annual Machine Learning and Data Science Survey](https://www.kaggle.com/kaggle/kaggle-survey-2018).

To deploy this model we had basically two options:
1. Export the model as as serialized object, load into AWS lambda and start making predictions.
2. [Parametrize](https://en.wikipedia.org/wiki/Parametrization) the model and load all coeficients and intercept manually to Lambda.

I choose the second option because I want the model to be transparen to anyone. It should be clear what the coefficients are and how the score is calculated. A serialized model wouldn't let us see that in detail.

[All material regarding the model's development is available here.](https://www.kaggle.com/andresionek/what-makes-a-kaggler-valuable)

## Implementing the parametrized model as a AWS Lambda Function.
To get this model into production, we are creating a Lambda function that receives the input json through an API Gateway Integration, calculates the score and then returns it to the API. You can access the API by doing a simple POST with the input json at the body.

Instructions on how to deploy a model to AWS lambda were found on this [Towards Data Science post, by Ben Weber](https://towardsdatascience.com/data-science-for-startups-model-services-2facf2dde81d).

### Implementation Example
```
import requests

input_json = {
    "Q1": "q1_other",
    "Q2": "q2_25_29",
    "Q3": "q3_united_",
    "Q4": "q4_other",
    "Q6": "q6_data_sc",
    "Q7": "q7_other2",
    "Q8": "q8_2_3",
    "Q10": "q10_we_rec",
    "q11_analyz": "on",
    "q11_run_a_": "on",
    "q11_build_": "on",
    "q15_amazon": "on",
    "other": "on",
    "q16_python": "on",
    "q16_sql": "on",
    "Q23": "q23_25_to_",
    "q31_catego": "on",
    "q31_geospa": "on",
    "q31_numeri": "on",
    "q31_tabula": "on",
    "q31_text_d": "on",
    "q31_time_s": "on",
    "q42_revenu": "on"
}

header = {'Content-Type': 'application/x-www-form-urlencoded'}
url = 'https://tk9k0fkvyj.execute-api.us-east-2.amazonaws.com/default/top20-predictor'

requests.post(url, params=input_json, headers=header).json()
```
