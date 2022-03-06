from fastapi import APIRouter


router = APIRouter()

router.post('/users')
def login():
    return 'login'