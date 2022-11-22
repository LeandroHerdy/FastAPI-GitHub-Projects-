from pydantic import BaseModel


class StandardInput(BaseModel):
    name: str
    


class StandardOutput(BaseModel):
    name: str
    