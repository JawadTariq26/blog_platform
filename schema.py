from pydantic import BaseModel

class BlogContent(BaseModel):
    title : str
    subtitle : str
    body : str
