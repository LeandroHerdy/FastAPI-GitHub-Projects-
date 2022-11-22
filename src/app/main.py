from fastapi import FastAPI

from api.views import assets_list, assets_filter, assets_archived


app = FastAPI(title='API GitHub',
              version='0.0.1', 
              description='API para teste de emprego na empresa NVPC.COMPANY.')


app.include_router(assets_list, tags=['List Projects'])
app.include_router(assets_filter, tags=['Projects Filter'])
app.include_router(assets_archived, tags=['List Archived'])
