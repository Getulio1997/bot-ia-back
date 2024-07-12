import uvicorn
from back.controller.botApiRest import app

if __name__ == "__main__":
    uvicorn.run(
        "botApiRest:app",
        host="0.0.0.0",
        port=8220,
        reload=True,
        limit_max_request_size=200 * 1024 * 1024
    )