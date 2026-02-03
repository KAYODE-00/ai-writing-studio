from fastapi import FastAPI

app =  FastAPI(
    title="AI writing studio",
    description="AI-powered content generation plartform",
    version="1.0.0"
)



app.data_middleware(
    CORSNiddleware.
    allow_origins=[
        "https://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/health")
def health_check():
    return{
        "status":"sucess",
        "message":"writing studio running"
    }