import uvicorn
from back.controller.botApiRest import app

if __name__ == "__main__":
    uvicorn.run(
        "back.controller.botApiRest:app",
        port=8000,
        reload=True
    )
