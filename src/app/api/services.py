from aiohttp import ClientSession


class AssetService:
    
    async def github_summary() -> str:
        async with ClientSession() as session:            
            url = f'https://api.github.com/users/LeandroHerdy/repos'
            response = await session.get(url)
            dataset = await response.json()
            name = [data['name'].replace("-", " ")  for data in dataset]
            date = [data['updated_at'] for data in dataset]
            dataset = zip(date, name)
            data = (list(dataset))
            return data 
        
    async def github_archived() -> str:
        async with ClientSession() as session:            
            url = f'https://api.github.com/users/LeandroHerdy/repos'
            response = await session.get(url)
            dataset = await response.json()
            name = [data['name'].replace("-", " ")  for data in dataset]
            archived = [data['archived'] for data in dataset]
            dataset = zip(archived, name)
            data = (list(dataset))
            return data   
                