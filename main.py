from fastapi import FastAPI
from app.routers import payments, subscriptions, users

app=FastAPI(title='Enterprise Payment & Subscription System')

app.include_router(users.router)
app.include_router(payments.router)
app.include_router(subscriptions.router)

@app.get('/')
def root():
    return {'message':'Payment System Running'}
