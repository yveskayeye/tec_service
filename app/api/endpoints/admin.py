from fastapi import APIRouter


router = APIRouter()

router.post('/admin')
def login():
    return 'login'