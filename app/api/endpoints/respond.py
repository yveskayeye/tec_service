from fastapi import APIRouter


router = APIRouter()

router.post('/respond')
def login():
    return 'login'