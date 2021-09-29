# autorec
AutoRecommender System Solution for Xebia Xethon Hackathon. A microservice API for aggregating user interactions, automatically trains the best recommender model for it and deploys the recommender model for real time inference.


## Tech Stack 

* Python 3.7+
* Scikit-learn
* Streamlit
* FastAPI - Web API Server
* Docker - Containerization Deployment
* SQLAlchemy - SQL ORM Wrapper
* SQLite3 - Standalone Database

## Modeling

In general, most recommendation models can be divided into two categories:

* Content based model,
* Collaborative filtering model.

The content-based model recommends based on similarity of the items and/or users using their description/metadata/profile. On the other hand, collaborative filtering model (discussion is limited to matrix factorisation approach in this notebook) computes the latent factors of the users and items. It works based on the assumption that if a group of people expressed similar opinions on an item, these peole would tend to have similar opinions on other items. For further background and detailed explanation between these two approaches, the reader can refer to machine learning literatures.

### LightFM

It is a hybrid content-collaborative model which represents users and items as linear combinations of their content features’ latent factors. The model learns embeddings or latent representations of the users and items in such a way that it encodes user preferences over items. These representations produce scores for every item for a given user; items scored highly are more likely to be interesting to the user.

The user and item embeddings are estimated for every feature, and these features are then added together to be the final representations for users and items.

For example, for user i, the model retrieves the i-th row of the feature matrix to find the features with non-zero weights. The embeddings for these features will then be added together to become the user representation e.g. if user 10 has weight 1 in the 5th column of the user feature matrix, and weight 3 in the 20th column, the user 10’s representation is the sum of embedding for the 5th and the 20th features multiplying their corresponding weights. The representation for each items is computed in the same approach.

## Design

![API Design]("./designapi-design.png")