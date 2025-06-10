from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.api_route("/api/products", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_products_root(request: Request):
    method = request.method
    url = f"http://product-service/"
    headers = dict(request.headers)
    data = await request.body()
    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method,
            url,
            headers=headers,
            content=data
        )
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers=resp.headers
        )

@app.api_route("/api/products/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_products(request: Request, path: str):
    method = request.method
    url = f"http://product-service/{path}"
    headers = dict(request.headers)
    data = await request.body()
    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method,
            url,
            headers=headers,
            content=data
        )
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers=resp.headers
        )