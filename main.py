from fastapi import FastAPI
from pydantic import BaseModel
# 데이터 유효성 검사와 설정 관리에 사용되는 라이브러리(모델링이 쉽고 강력함)
from starlette.middleware.base import BaseHTTPMiddleware

# 요청과 응답사이에 특정 작업 수행
# 미들웨어는 모든 요청에 대해 실행되며, 요청을 처리하기 전에 응답을 반환하기 전에 특정 작업을 수행할 수 있음
# 예를 들어 로깅, 인증, cors처리, 압축등...
import logging # 로깅 처리용

app = FastAPI(  # App 시그니처 환경설정 담당
    
    title = "MBC AI Study",                 # 앱 제목
    description = "MBC AI Study",           # 앱 설명
    version = "0.0.1",                      # 앱 버전
    docs_url = None,
    redoc_url = None,
    
    
    
)

class LoggingMiddleware(BaseHTTPMiddleware):
    logging.basicConfig(level=logging.INFO)
    async def dispatch(self, request, call_next):
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")
        return response
app.add_middleware(LoggingMiddleware)

class Item(BaseModel): # item 객체 생성(basemodel :  객체연결 ->  상속)
    name: str               # 상품명
    description: str = None # 상품설명
    price: float            # 가격
    tax: float =None        # 세금


@app.post("/items/") # post  메서드 요청(create)
async def create_item(item: Item):
    # baseModel은 데이터 모델링을 쉽게 도와주고 유효성검사도 수행
    # 잘못된 데이터가 들어오면 422 오류코드 반환
    return item


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # http://localhost:8001/item/1 -> get요청시
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q" : q}
    # item_id : 상품의 번호 -> 결로 매개 변수
    # q : 쿼리 매개변수 (기본값 None)

# postman은 프론트가 없는 백엔드 테스트용 프로그램
# 서버 실행은 uvicorn main:app --reload --port 8001
#           파이썬 백엔드 가동 서버           포트번호는 8001