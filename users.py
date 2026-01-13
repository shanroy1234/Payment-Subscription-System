from fastapi import APIRouter
router=APIRouter(prefix='/users')

@router.post('/create')
def create(u:dict):
    return u
