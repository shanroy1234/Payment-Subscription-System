from fastapi import APIRouter
router=APIRouter(prefix='/subscriptions')

@router.post('/create')
def sub(s:dict):
    return {'subscription':s}
