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
