from fastapi import APIRouter, HTTPException, status
from .services import AssetService

from datetime import datetime, timezone


assets_list = APIRouter(prefix='/api/v1')
assets_filter = APIRouter(prefix='/api/v1')
assets_archived = APIRouter(prefix='/api/v1')


@assets_archived.get('/list_archived/{type}', description='Retorna todos os projetos arquivados.',
                                            summary='Retorna o nome de todos os projetos ou uma lista vazia.',                                            
                                            status_code=status.HTTP_201_CREATED)
async def list_name_archived(type: bool) -> str:
    try:
        data = await AssetService.github_archived()
        list = []
        print(type)
        for archived, filter_name in data:
            if archived == type:
                list.append(filter_name)
        return list
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Not found')


@assets_list.get('/list_order', description='Retorna todos os projetos ordenado.',
                            summary='Retorna o nome de todos os projetos em ordem alfabética e por data do último commit dos repositórios.',                            
                            status_code=status.HTTP_201_CREATED)
async def list_name_order():
    try:
        data = await AssetService.github_summary()
        list = []
        for date, field_name in data:  
            zone = datetime.fromisoformat(date[:-1]).astimezone(timezone.utc)
            date_time = zone.strftime('%Y/%m/%d %H:%M:%S')
            list += [(date_time, field_name)]

        sorted_list = sorted(list, key=lambda t: datetime.strptime(t[0],'%Y/%m/%d %H:%M:%S'))
        sorted_order = []
        for _, list_name in sorted_list:
            sorted_order.append(list_name)
        return sorted_order
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Not found')
    
        
@assets_filter.get('/filter/{name}', description='Retorna uma pesquisa.', 
                                    summary='Retorna uma lista dos projetos filtrados',                                     
                                    status_code=status.HTTP_201_CREATED)
async def filter_name(name: str) -> str:
    try:
        data = await AssetService.github_summary()        
        list = []
        for _, field_name in data:
            if name.casefold() in field_name.casefold():
                list.append(field_name)
        return list
        
    except KeyError:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Not found')   