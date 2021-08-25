import fastapi
import uvicorn


from api import general

api = fastapi.FastAPI()

# what is an API? https://rapidapi.com/blog/api-vs-web-service/


api.include_router(general.router)


if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=80)