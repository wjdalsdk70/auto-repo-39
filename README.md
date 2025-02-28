# 게시판 CRUD API
🎉 간단한 게시판 CRUD API를 FastAPI와 SQLite를 사용하여 구현했습니다.  쉽고 빠르게 게시글을 관리할 수 있습니다!

## 폴더 구조
```
board_app/
├── main.py
├── requirements.txt
├── routers/
│   └── board.py
└── models.py
```

## 파일 별 설명
- main.py : FastAPI 애플리케이션을 실행하는 메인 파일입니다.
- requirements.txt : 프로젝트에 필요한 패키지 목록을 정의하는 파일입니다.
- routers/board.py : 게시판 관련 API 라우터를 정의하는 파일입니다.
- models.py : 게시판 데이터 모델을 정의하는 파일입니다.


## 배포 작업 순서 설명
1. `pip install -r requirements.txt` 명령어를 사용하여 필요한 패키지를 설치합니다.
2. `python main.py` 명령어를 사용하여 FastAPI 애플리케이션을 실행합니다.
3. API 문서(http://127.0.0.1:8000/docs)를 통해 API를 테스트하고 사용할 수 있습니다.