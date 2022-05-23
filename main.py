import fastapi
import uvicorn
import os
from pathlib import Path

from api import general, prediction


api = fastapi.FastAPI()


api.include_router(general.router)
api.include_router(prediction.router)


if __name__ == '__main__':

    # abs_path = os.getcwd()

    # PATH = '/'.join(str(Path(__file__).absolute()).split('/')[:-1])
    # os.chdir(PATH)

    uvicorn.run(api, host='0.0.0.0', port=80)