import pickle
from fastapi import APIRouter, Depends
import pandas as pd
from sqlmodel import Session
from backend.app.db.db import get_session
from backend.app.model import Orders

r = router = APIRouter()


@r.post("/add_data")
async def add_data(order: Orders, session: Session = Depends(get_session)):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order

@r.get("/recommender/{choice}/{id}")
async def get_recommendation(choice: str, id: str):
    df = pd.read_csv("../../dataset/clean-retail.csv")
    if choice == "product":
        with open("../../models/product_based_rec.pickle", "rb") as f:
            product_similarity = pickle.load(f)
        top_10_similar_products = list(product_similarity.loc[id].sort_values(ascending=False).iloc[:10].index)
        return df.loc[ 
            df['StockCode'].isin(top_10_similar_products),
            ['StockCode', 'Description']
        ].drop_duplicates().set_index('StockCode').loc[top_10_similar_products].to_json()
    
    if choice == "user":
        with open("../../models/user_based_rec.pickle", "rb") as f:
            user_similarity = pickle.load(f)
        with open("../../models/user_product_matrix.pickle", "rb") as f:
            customer_item_matrix = pickle.load(f)
        user_similarity.loc[float(id)].sort_values(ascending=False).head(10)
        user_similarity.loc[12350.0].sort_values(ascending=False)
        products_bought_by_A = customer_item_matrix.loc[12350.0][customer_item_matrix.loc[12350.0]>0]
        nearest_user = user_similarity.loc[12350.0].sort_values(ascending=False).index[1]
        products_bought_by_B = customer_item_matrix.loc[nearest_user][customer_item_matrix.loc[nearest_user]>0]
        products_to_recommend_to_B = set(products_bought_by_A.index) - set(products_bought_by_B.index)
        return df.loc[
            df['StockCode'
            ].isin(
                products_to_recommend_to_B),['StockCode', 'Description']].drop_duplicates().set_index('StockCode'
                ).to_json()
        

