from pydantic import BaseModel, validator
from re import sub


class Customer(BaseModel):
    name: str
    cpf: str
    phone: str

    @validator("name")
    def normalizar_nome(cls, v: str):
        nomes = v.split(' ')
        nome_final=[]
        for nome in nomes:
            nome_final.append(nome.capitalize())
        return ' '.join(nome_final)

    @validator("cpf")
    def n_cpf(cls, v):
        v = sub('[^0-9]', '', v)
        return v

    @validator("phone")
    def n_cpf(cls, v):
        v = sub('[^0-9]', '', v)
        return v

