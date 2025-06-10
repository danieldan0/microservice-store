from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def get_products():
    return [
        {"id": 1, "name": "Product 1", "price": 10.0},
        {"id": 2, "name": "Product 2", "price": 20.0},
        {"id": 3, "name": "Product 3", "price": 30.0}
    ]

@app.get("/{product_id}")
def get_product(product_id: int):
    products = {
        1: {"id": 1, "name": "Product 1", "price": 10.0},
        2: {"id": 2, "name": "Product 2", "price": 20.0},
        3: {"id": 3, "name": "Product 3", "price": 30.0}
    }
    return products.get(product_id, {"error": "Product not found"})

@app.post("/")
def create_product(product: dict):
    # Placeholder
    return {"message": "Product created", "product": product}

@app.put("/{product_id}")
def update_product(product_id: int, product: dict):
    # Placeholder
    return {"message": "Product updated", "product_id": product_id, "product": product}

@app.delete("/{product_id}")
def delete_product(product_id: int):
    # Placeholder
    return {"message": "Product deleted", "product_id": product_id}