import fastapi
from models.pydantic.predict_iris import OutputIris, InputIris
from utils.data import load_model
import numpy as np

router = fastapi.APIRouter()

@router.post('/predict_iris_species', response_model=OutputIris)
async def predict_species(data: InputIris=fastapi.Depends()):
    
    model = load_model()

    arr = np.array([x for x in data.dict().values()])

    prediction = model.predict([arr])[0]
    
    output = OutputIris(species=prediction)

    return output