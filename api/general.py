import fastapi

from models.pydantic.sample_data import InputData, OutputData, ModelName

router = fastapi.APIRouter()

@router.get('/', include_in_schema=False)
async def index():
    return {'hello': 'world'}


@router.get('/status')
async def status():
    return {'status': 'ok'}


@router.get('/item/{item_id}')
async def get_item(item_id: int):
    
    # print(type(item_id))
    
    d = {1: 'one', 2: 'two'}
    return {'item_id': d.get(item_id)}


@router.get('/calculator')
async def calc(a: int, b: int):
    return {'result': a+b}


@router.get('/selection/{model}')
async def calc(model: ModelName):
    return {'model_name': model}


@router.post('/check_class', response_model=OutputData)
async def check_class(data: InputData = fastapi.Depends()):
    
    # return {'InputData': data}

    output = OutputData(my_value=data.my_string)

    return output