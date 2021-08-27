# Demo FastAPI

1. Run simple App with /docs
2. Simple functions (status)
3. Get Paramters (types to pass to the function)
4. ENUM Parameters
5. Pydantic Class
    - create
    - import
    - get vs. post error
    - errors
    - validator
    - "= fastapi.Depends()"
    - ", response_model="
6. Predict Species



### Deploy to Azure Container Instance
1. Build local Image of your app: docker build -t imagename --no-cache .
2. Create ACR resource (youracrname.azurecr.io)
3. az login --tenant xyz-abc (When confusion with logins run: az account clear)
4. docker login youracrname.azurecr.io (make sure to turn on Admin User Mode to get User and Password)
5. docker tag imagename youracrname.azurecr.io/imagename:tag
6. docker push youracrname.azurecr.io/imagename:tag
7. Create ACI resource (from the image you pushed to ACR before)
8. az container show --resource-group RG --name SERVICE --query ipAddress.ip