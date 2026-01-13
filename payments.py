from fastapi import APIRouter
router=APIRouter(prefix='/payments')

@router.post('/pay')
def pay(p:dict):
    return {'status':'success','data':p}
