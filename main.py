from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["null"],
    allow_origin_regex=r"^http://(localhost|127\.0\.0\.1):[0-9]+$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    # =========================
    # Meat Shop 1
    # =========================
    {"id": 1, "product_key": "beef_sirloin", "name": "Beef Sirloin", "name_ko": "소고기 등심", "category": "meat", "category_ko": "정육", "price": 18500, "shop_id": 1},
    {"id": 2, "product_key": "pork_belly", "name": "Pork Belly", "name_ko": "삼겹살", "category": "meat", "category_ko": "정육", "price": 12500, "shop_id": 1},
    {"id": 3, "product_key": "chicken_breast", "name": "Chicken Breast", "name_ko": "닭가슴살", "category": "meat", "category_ko": "정육", "price": 8200, "shop_id": 1},
    {"id": 4, "product_key": "hanwoo_brisket", "name": "Hanwoo Brisket", "name_ko": "한우 차돌박이", "category": "meat", "category_ko": "정육", "price": 24000, "shop_id": 1},
    {"id": 5, "product_key": "marinated_pork_ribs", "name": "Marinated Pork Ribs", "name_ko": "양념 돼지갈비", "category": "meat", "category_ko": "정육", "price": 15000, "shop_id": 1},

    # Meat Shop 2
    {"id": 6, "product_key": "beef_sirloin", "name": "Beef Sirloin", "name_ko": "소고기 등심", "category": "meat", "category_ko": "정육", "price": 17800, "shop_id": 2},
    {"id": 7, "product_key": "pork_belly", "name": "Pork Belly", "name_ko": "삼겹살", "category": "meat", "category_ko": "정육", "price": 11900, "shop_id": 2},
    {"id": 8, "product_key": "chicken_breast", "name": "Chicken Breast", "name_ko": "닭가슴살", "category": "meat", "category_ko": "정육", "price": 8500, "shop_id": 2},
    {"id": 9, "product_key": "lamb_chops", "name": "Lamb Chops", "name_ko": "양갈비", "category": "meat", "category_ko": "정육", "price": 22000, "shop_id": 2},
    {"id": 10, "product_key": "smoked_sausage", "name": "Smoked Sausage", "name_ko": "훈제 소시지", "category": "meat", "category_ko": "정육", "price": 7600, "shop_id": 2},

    # Meat Shop 3
    {"id": 11, "product_key": "beef_sirloin", "name": "Beef Sirloin", "name_ko": "소고기 등심", "category": "meat", "category_ko": "정육", "price": 19200, "shop_id": 3},
    {"id": 12, "product_key": "pork_belly", "name": "Pork Belly", "name_ko": "삼겹살", "category": "meat", "category_ko": "정육", "price": 12800, "shop_id": 3},
    {"id": 13, "product_key": "chicken_breast", "name": "Chicken Breast", "name_ko": "닭가슴살", "category": "meat", "category_ko": "정육", "price": 7900, "shop_id": 3},
    {"id": 14, "product_key": "duck_breast", "name": "Duck Breast", "name_ko": "오리 가슴살", "category": "meat", "category_ko": "정육", "price": 13500, "shop_id": 3},
    {"id": 15, "product_key": "beef_bulgogi", "name": "Beef Bulgogi", "name_ko": "소불고기", "category": "meat", "category_ko": "정육", "price": 16500, "shop_id": 3},

    # =========================
    # Vegetable Shop 1
    # =========================
    {"id": 16, "product_key": "lettuce", "name": "Lettuce", "name_ko": "상추", "category": "vegetable", "category_ko": "채소", "price": 2600, "shop_id": 4},
    {"id": 17, "product_key": "onion", "name": "Onion", "name_ko": "양파", "category": "vegetable", "category_ko": "채소", "price": 1900, "shop_id": 4},
    {"id": 18, "product_key": "potato", "name": "Potato", "name_ko": "감자", "category": "vegetable", "category_ko": "채소", "price": 3100, "shop_id": 4},
    {"id": 19, "product_key": "perilla_leaves", "name": "Perilla Leaves", "name_ko": "깻잎", "category": "vegetable", "category_ko": "채소", "price": 2200, "shop_id": 4},
    {"id": 20, "product_key": "korean_chili", "name": "Korean Chili Pepper", "name_ko": "청양고추", "category": "vegetable", "category_ko": "채소", "price": 2500, "shop_id": 4},

    # Vegetable Shop 2
    {"id": 21, "product_key": "lettuce", "name": "Lettuce", "name_ko": "상추", "category": "vegetable", "category_ko": "채소", "price": 2400, "shop_id": 5},
    {"id": 22, "product_key": "onion", "name": "Onion", "name_ko": "양파", "category": "vegetable", "category_ko": "채소", "price": 2100, "shop_id": 5},
    {"id": 23, "product_key": "potato", "name": "Potato", "name_ko": "감자", "category": "vegetable", "category_ko": "채소", "price": 2900, "shop_id": 5},
    {"id": 24, "product_key": "zucchini", "name": "Zucchini", "name_ko": "애호박", "category": "vegetable", "category_ko": "채소", "price": 2300, "shop_id": 5},
    {"id": 25, "product_key": "spinach", "name": "Spinach", "name_ko": "시금치", "category": "vegetable", "category_ko": "채소", "price": 3200, "shop_id": 5},

    # Vegetable Shop 3
    {"id": 26, "product_key": "lettuce", "name": "Lettuce", "name_ko": "상추", "category": "vegetable", "category_ko": "채소", "price": 2800, "shop_id": 6},
    {"id": 27, "product_key": "onion", "name": "Onion", "name_ko": "양파", "category": "vegetable", "category_ko": "채소", "price": 1800, "shop_id": 6},
    {"id": 28, "product_key": "potato", "name": "Potato", "name_ko": "감자", "category": "vegetable", "category_ko": "채소", "price": 3300, "shop_id": 6},
    {"id": 29, "product_key": "broccoli", "name": "Broccoli", "name_ko": "브로콜리", "category": "vegetable", "category_ko": "채소", "price": 4500, "shop_id": 6},
    {"id": 30, "product_key": "paprika", "name": "Paprika", "name_ko": "파프리카", "category": "vegetable", "category_ko": "채소", "price": 3900, "shop_id": 6},

    # =========================
    # Fish Shop 1
    # =========================
    {"id": 31, "product_key": "salmon_fillet", "name": "Salmon Fillet", "name_ko": "연어 필렛", "category": "fish", "category_ko": "수산", "price": 16500, "shop_id": 7},
    {"id": 32, "product_key": "mackerel", "name": "Mackerel", "name_ko": "고등어", "category": "fish", "category_ko": "수산", "price": 7200, "shop_id": 7},
    {"id": 33, "product_key": "shrimp_pack", "name": "Shrimp Pack", "name_ko": "새우 팩", "category": "fish", "category_ko": "수산", "price": 13200, "shop_id": 7},
    {"id": 34, "product_key": "abalone", "name": "Abalone", "name_ko": "전복", "category": "fish", "category_ko": "수산", "price": 26000, "shop_id": 7},
    {"id": 35, "product_key": "sea_urchin", "name": "Sea Urchin", "name_ko": "성게", "category": "fish", "category_ko": "수산", "price": 30000, "shop_id": 7},

    # Fish Shop 2
    {"id": 36, "product_key": "salmon_fillet", "name": "Salmon Fillet", "name_ko": "연어 필렛", "category": "fish", "category_ko": "수산", "price": 15800, "shop_id": 8},
    {"id": 37, "product_key": "mackerel", "name": "Mackerel", "name_ko": "고등어", "category": "fish", "category_ko": "수산", "price": 6900, "shop_id": 8},
    {"id": 38, "product_key": "shrimp_pack", "name": "Shrimp Pack", "name_ko": "새우 팩", "category": "fish", "category_ko": "수산", "price": 14000, "shop_id": 8},
    {"id": 39, "product_key": "squid", "name": "Squid", "name_ko": "오징어", "category": "fish", "category_ko": "수산", "price": 9000, "shop_id": 8},
    {"id": 40, "product_key": "clams", "name": "Clams", "name_ko": "바지락", "category": "fish", "category_ko": "수산", "price": 6500, "shop_id": 8},

    # Fish Shop 3
    {"id": 41, "product_key": "salmon_fillet", "name": "Salmon Fillet", "name_ko": "연어 필렛", "category": "fish", "category_ko": "수산", "price": 17200, "shop_id": 9},
    {"id": 42, "product_key": "mackerel", "name": "Mackerel", "name_ko": "고등어", "category": "fish", "category_ko": "수산", "price": 7600, "shop_id": 9},
    {"id": 43, "product_key": "shrimp_pack", "name": "Shrimp Pack", "name_ko": "새우 팩", "category": "fish", "category_ko": "수산", "price": 12800, "shop_id": 9},
    {"id": 44, "product_key": "blue_crab", "name": "Blue Crab", "name_ko": "꽃게", "category": "fish", "category_ko": "수산", "price": 22000, "shop_id": 9},
    {"id": 45, "product_key": "flatfish", "name": "Flatfish", "name_ko": "광어", "category": "fish", "category_ko": "수산", "price": 25000, "shop_id": 9},

    # =========================
    # Fruit Shop 1
    # =========================
    {"id": 46, "product_key": "apple", "name": "Apple", "name_ko": "사과", "category": "fruit", "category_ko": "과일", "price": 3200, "shop_id": 10},
    {"id": 47, "product_key": "banana_bunch", "name": "Banana Bunch", "name_ko": "바나나 송이", "category": "fruit", "category_ko": "과일", "price": 4600, "shop_id": 10},
    {"id": 48, "product_key": "orange", "name": "Orange", "name_ko": "오렌지", "category": "fruit", "category_ko": "과일", "price": 3600, "shop_id": 10},
    {"id": 49, "product_key": "melon", "name": "Melon", "name_ko": "멜론", "category": "fruit", "category_ko": "과일", "price": 13000, "shop_id": 10},
    {"id": 50, "product_key": "kiwi_pack", "name": "Kiwi Pack", "name_ko": "키위 팩", "category": "fruit", "category_ko": "과일", "price": 7500, "shop_id": 10},

    # Fruit Shop 2
    {"id": 51, "product_key": "apple", "name": "Apple", "name_ko": "사과", "category": "fruit", "category_ko": "과일", "price": 3000, "shop_id": 11},
    {"id": 52, "product_key": "banana_bunch", "name": "Banana Bunch", "name_ko": "바나나 송이", "category": "fruit", "category_ko": "과일", "price": 4900, "shop_id": 11},
    {"id": 53, "product_key": "orange", "name": "Orange", "name_ko": "오렌지", "category": "fruit", "category_ko": "과일", "price": 3400, "shop_id": 11},
    {"id": 54, "product_key": "green_grapes", "name": "Green Grapes", "name_ko": "청포도", "category": "fruit", "category_ko": "과일", "price": 8500, "shop_id": 11},
    {"id": 55, "product_key": "pear", "name": "Pear", "name_ko": "배", "category": "fruit", "category_ko": "과일", "price": 4200, "shop_id": 11},

    # Fruit Shop 3
    {"id": 56, "product_key": "apple", "name": "Apple", "name_ko": "사과", "category": "fruit", "category_ko": "과일", "price": 3500, "shop_id": 12},
    {"id": 57, "product_key": "banana_bunch", "name": "Banana Bunch", "name_ko": "바나나 송이", "category": "fruit", "category_ko": "과일", "price": 4300, "shop_id": 12},
    {"id": 58, "product_key": "orange", "name": "Orange", "name_ko": "오렌지", "category": "fruit", "category_ko": "과일", "price": 3800, "shop_id": 12},
    {"id": 59, "product_key": "strawberry_pack", "name": "Strawberry Pack", "name_ko": "딸기 팩", "category": "fruit", "category_ko": "과일", "price": 9000, "shop_id": 12},
    {"id": 60, "product_key": "watermelon", "name": "Watermelon", "name_ko": "수박", "category": "fruit", "category_ko": "과일", "price": 14500, "shop_id": 12},
]


cart = []
orders = []
users = [
    {
        "user_id": 1,
        "username": "test",
        "password": "test1",
        "name": "테스트 고객",
        "created_at": "test account"
    }
]
next_user_id = 2
next_order_id = 1
HUB_LOCATION = {"name": "Logistics Hub", "x": 0, "y": 7}
rider_state = {
    "current_location": HUB_LOCATION.copy(),
    "last_location_update_at": None,
    "active_batch_order_ids": [],
    "active_batch_started_at": None
}

PRODUCT_RECOMMENDATION_RULES = {
    "meat": {
        "missing_category": "vegetable",
        "trigger_count": 3,
        "message_ko": "장바구니에 육류 상품이 많이 담겨 있어요. 함께 먹기 좋은 채소를 추천드려요.",
        "reason_ko": "고기와 함께 먹기 좋은 채소예요."
    }
}






class CartItem(BaseModel):
    product_id: int
    quantity: int


class CartReplaceItem(BaseModel):
    current_product_id: int
    recommended_product_id: int
    quantity: int | None = None


class CustomerSignup(BaseModel):
    username: str
    password: str
    name: str = "Customer"


class CustomerLogin(BaseModel):
    username: str
    password: str



class RiderLocationUpdate(BaseModel):
    name: str = "Manual Test Location"
    x: int
    y: int


class PaymentRequest(BaseModel):
    payment_method: str = "card"
    amount: int


class CheckoutRequest(BaseModel):
    payment_method: str = "card"


def get_cart_product_details():
    cart_details = []
    total_price = 0

    for item in cart:
        product = next((p for p in products if p["id"] == item["product_id"]), None)

        if product:
            subtotal = product["price"] * item["quantity"]
            total_price += subtotal

            cart_details.append({
                "product_id": product["id"],
                "product_key": product["product_key"],
                "name": product["name"],
                "name_ko": product["name_ko"],
                "category": product["category"],
                "category_ko": product["category_ko"],
                "price": product["price"],
                "quantity": item["quantity"],
                "subtotal": subtotal,
                "shop_id": product["shop_id"]
            })

    return {
        "items": cart_details,
        "total_price": total_price
    }


def get_ai_product_recommendations():
    cart_details = get_cart_product_details()["items"]

    if not cart_details:
        return {
            "show_popup": False,
            "message_ko": "",
            "recommendations": []
        }

    cart_categories = {}

    for item in cart_details:
        category = item["category"]
        cart_categories[category] = cart_categories.get(category, 0) + item["quantity"]

    recommended_product_ids = {item["product_id"] for item in cart_details}
    recommendations = []
    message_ko = ""

    for category, rule in PRODUCT_RECOMMENDATION_RULES.items():
        current_category_count = cart_categories.get(category, 0)
        missing_category = rule["missing_category"]
        missing_category_count = cart_categories.get(missing_category, 0)

        if current_category_count >= rule["trigger_count"] and missing_category_count == 0:
            message_ko = rule["message_ko"]

            candidate_products = [
                product for product in products
                if product["category"] == missing_category
                and product["id"] not in recommended_product_ids
            ]

            cheapest_products_by_key = {}

            for product in candidate_products:
                product_key = product["product_key"]

                if (
                    product_key not in cheapest_products_by_key
                    or product["price"] < cheapest_products_by_key[product_key]["price"]
                ):
                    cheapest_products_by_key[product_key] = product

            for product in list(cheapest_products_by_key.values())[:4]:
                shop = next((s for s in shops if s["id"] == product["shop_id"]), None)

                recommendations.append({
                    "product_id": product["id"],
                    "product_key": product["product_key"],
                    "name": product["name"],
                    "name_ko": product["name_ko"],
                    "category": product["category"],
                    "category_ko": product["category_ko"],
                    "price": product["price"],
                    "shop_id": product["shop_id"],
                    "shop_name": shop["name"] if shop else None,
                    "reason_ko": rule["reason_ko"]
                })

    return {
        "show_popup": len(recommendations) > 0,
        "message_ko": message_ko,
        "recommendations": recommendations
    }


@app.get("/")
def home():
    return {"message": "Market backend is running"}


@app.post("/auth/signup")
def signup_customer(signup_data: CustomerSignup):
    global next_user_id

    username = signup_data.username.strip()
    password = signup_data.password.strip()
    name = signup_data.name.strip()

    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password are required")

    existing_user = next(
        (user for user in users if user["username"] == username),
        None
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = {
        "user_id": next_user_id,
        "username": username,
        "password": password,
        "name": name,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users.append(new_user)
    next_user_id += 1

    return {
        "message": "Signup completed",
        "message_ko": "회원가입이 완료되었습니다.",
        "user": {
            "user_id": new_user["user_id"],
            "username": new_user["username"],
            "name": new_user["name"]
        }
    }


@app.post("/auth/login")
def login_customer(login_data: CustomerLogin):
    username = login_data.username.strip()
    password = login_data.password.strip()

    matched_user = next(
        (user for user in users if user["username"] == username and user["password"] == password),
        None
    )

    if matched_user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "message_ko": "로그인에 성공했습니다.",
        "is_logged_in": True,
        "user": {
            "user_id": matched_user["user_id"],
            "username": matched_user["username"],
            "name": matched_user["name"]
        }
    }


@app.get("/auth/users")
def get_users():
    return {
        "users": [
            {
                "user_id": user["user_id"],
                "username": user["username"],
                "name": user["name"],
                "created_at": user["created_at"]
            }
            for user in users
        ]
    }


@app.get("/products")
def get_products(category: str | None = None):
    if category:
        return [p for p in products if p["category"] == category]
    return products


@app.post("/cart/items")
def add_to_cart(item: CartItem):
    product = next((p for p in products if p["id"] == item.product_id), None)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_item = next(
        (cart_item for cart_item in cart if cart_item["product_id"] == item.product_id),
        None
    )

    if existing_item:
        existing_item["quantity"] += item.quantity
    else:
        cart.append({
            "product_id": item.product_id,
            "quantity": item.quantity
        })

    cart_result = get_cart_product_details()
    ai_product_recommendations = get_ai_product_recommendations()

    return {
        "message": "Product added to cart",
        "cart": cart_result,
        "ai_product_recommendations": ai_product_recommendations
    }


# ---- Cart item quantity and removal endpoints ----

@app.patch("/cart/items/{product_id}/increase")
def increase_cart_item(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_item = next(
        (cart_item for cart_item in cart if cart_item["product_id"] == product_id),
        None
    )

    if existing_item:
        existing_item["quantity"] += 1
    else:
        cart.append({
            "product_id": product_id,
            "quantity": 1
        })

    cart_result = get_cart_product_details()
    ai_product_recommendations = get_ai_product_recommendations()

    return {
        "message": "Cart item quantity increased",
        "message_ko": "장바구니 상품 수량이 증가했습니다.",
        "cart": cart_result,
        "ai_product_recommendations": ai_product_recommendations
    }


@app.patch("/cart/items/{product_id}/decrease")
def decrease_cart_item(product_id: int):
    existing_item = next(
        (cart_item for cart_item in cart if cart_item["product_id"] == product_id),
        None
    )

    if existing_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")

    existing_item["quantity"] -= 1

    if existing_item["quantity"] <= 0:
        cart.remove(existing_item)

    cart_result = get_cart_product_details()
    ai_product_recommendations = get_ai_product_recommendations()

    return {
        "message": "Cart item quantity decreased",
        "message_ko": "장바구니 상품 수량이 감소했습니다.",
        "cart": cart_result,
        "ai_product_recommendations": ai_product_recommendations
    }



@app.delete("/cart/items/{product_id}")
def remove_cart_item(product_id: int):
    existing_item = next(
        (cart_item for cart_item in cart if cart_item["product_id"] == product_id),
        None
    )

    if existing_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")

    cart.remove(existing_item)

    cart_result = get_cart_product_details()
    ai_product_recommendations = get_ai_product_recommendations()

    return {
        "message": "Cart item removed",
        "message_ko": "장바구니 상품이 삭제되었습니다.",
        "cart": cart_result,
        "ai_product_recommendations": ai_product_recommendations
    }


# --- Replace cart item with cheaper same product endpoint ---
@app.post("/cart/replace-item")
def replace_cart_item(replace_data: CartReplaceItem):
    current_item = next(
        (cart_item for cart_item in cart if cart_item["product_id"] == replace_data.current_product_id),
        None
    )

    if current_item is None:
        raise HTTPException(status_code=404, detail="Original cart item not found")

    current_product = next(
        (product for product in products if product["id"] == replace_data.current_product_id),
        None
    )

    recommended_product = next(
        (product for product in products if product["id"] == replace_data.recommended_product_id),
        None
    )

    if current_product is None or recommended_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if current_product["product_key"] != recommended_product["product_key"]:
        raise HTTPException(status_code=400, detail="Replacement product must be the same product type")

    if recommended_product["price"] >= current_product["price"]:
        raise HTTPException(status_code=400, detail="Recommended product is not cheaper than current product")

    replacement_quantity = replace_data.quantity or current_item["quantity"]

    cart.remove(current_item)

    existing_recommended_item = next(
        (cart_item for cart_item in cart if cart_item["product_id"] == replace_data.recommended_product_id),
        None
    )

    if existing_recommended_item:
        existing_recommended_item["quantity"] += replacement_quantity
    else:
        cart.append({
            "product_id": replace_data.recommended_product_id,
            "quantity": replacement_quantity
        })

    saving_per_item = current_product["price"] - recommended_product["price"]
    total_saving = saving_per_item * replacement_quantity

    cart_result = get_cart_product_details()
    ai_price_recommendations = get_ai_price_recommendations()
    ai_product_recommendations = get_ai_product_recommendations()

    return {
        "message": "Cart item replaced with cheaper same product",
        "message_ko": "더 저렴한 동일 상품으로 교체되었습니다.",
        "replaced_product": {
            "product_id": current_product["id"],
            "name": current_product["name"],
            "name_ko": current_product["name_ko"],
            "price": current_product["price"],
            "shop_id": current_product["shop_id"]
        },
        "new_product": {
            "product_id": recommended_product["id"],
            "name": recommended_product["name"],
            "name_ko": recommended_product["name_ko"],
            "price": recommended_product["price"],
            "shop_id": recommended_product["shop_id"]
        },
        "quantity": replacement_quantity,
        "saving_per_item": saving_per_item,
        "total_saving": total_saving,
        "cart": cart_result,
        "ai_price_recommendations": ai_price_recommendations,
        "ai_product_recommendations": ai_product_recommendations
    }


@app.delete("/cart")
def clear_cart():
    cart.clear()

    return {
        "message": "Cart cleared",
        "message_ko": "장바구니가 비워졌습니다.",
        "cart": {
            "items": [],
            "total_price": 0
        },
        "ai_product_recommendations": {
            "show_popup": False,
            "message_ko": "",
            "recommendations": []
        }
    }


@app.get("/cart")
def get_cart():
    cart_result = get_cart_product_details()
    ai_product_recommendations = get_ai_product_recommendations()

    return {
        "items": cart_result["items"],
        "total_price": cart_result["total_price"],
        "ai_product_recommendations": ai_product_recommendations
    }


# === AI Price Recommendations Endpoint ===
@app.get("/ai/price-recommendations")
def get_ai_price_recommendations():
    if not cart:
        return {
            "message": "Cart is empty",
            "ai_summary_ko": "AI가 분석할 장바구니 상품이 아직 없습니다. 상품을 먼저 담아주세요.",
            "ai_summary_en": "There are no cart items for AI to analyze yet. Please add products first.",
            "recommendations": []
        }

    recommendations = []

    for item in cart:
        current_product = next(
            (p for p in products if p["id"] == item["product_id"]),
            None
        )

        if current_product is None:
            continue

        same_products = [
            p for p in products
            if p["product_key"] == current_product["product_key"]
            and p["id"] != current_product["id"]
        ]

        cheaper_products = [
            p for p in same_products
            if p["price"] < current_product["price"]
        ]

        current_shop = next(
            (s for s in shops if s["id"] == current_product["shop_id"]),
            None
        )

        if cheaper_products:
            best_product = min(cheaper_products, key=lambda p: p["price"])
            recommended_shop = next(
                (s for s in shops if s["id"] == best_product["shop_id"]),
                None
            )

            saving_per_item = current_product["price"] - best_product["price"]
            total_saving = saving_per_item * item["quantity"]

            recommendations.append({
                "type": "cheaper_same_product_found",
                "current_product": {
                    "product_id": current_product["id"],
                    "product_key": current_product["product_key"],
                    "name": current_product["name"],
                    "name_ko": current_product["name_ko"],
                    "price": current_product["price"],
                    "shop_id": current_product["shop_id"],
                    "shop_name": current_shop["name"] if current_shop else None
                },
                "recommended_product": {
                    "product_id": best_product["id"],
                    "product_key": best_product["product_key"],
                    "name": best_product["name"],
                    "name_ko": best_product["name_ko"],
                    "price": best_product["price"],
                    "shop_id": best_product["shop_id"],
                    "shop_name": recommended_shop["name"] if recommended_shop else None
                },
                "quantity": item["quantity"],
                "saving_per_item": saving_per_item,
                "total_saving": total_saving,
                "confidence_score": 0.92,
                "ai_message_ko": (
                    f"장바구니를 스캔한 결과, 동일 상품이 "
                    f"{recommended_shop['name'] if recommended_shop else '다른 점포'}에서 더 낮은 가격으로 확인되었습니다. "
                    f"현재 선택가는 {current_product['price']}원이지만, 추천 가격은 {best_product['price']}원입니다. "
                    f"개당 {saving_per_item}원, 현재 수량 기준 총 {total_saving}원을 절약할 수 있어요."
                ),
                "ai_message_en": (
                    f"After scanning your cart, the same product was found at a lower price from "
                    f"{recommended_shop['name'] if recommended_shop else 'another shop'}. "
                    f"Your current price is {current_product['price']} KRW, while the recommended price is {best_product['price']} KRW. "
                    f"You can save {saving_per_item} KRW per item, for a total estimated saving of {total_saving} KRW."
                )
            })
        else:
            recommendations.append({
                "type": "no_cheaper_same_product_found",
                "current_product": {
                    "product_id": current_product["id"],
                    "product_key": current_product["product_key"],
                    "name": current_product["name"],
                    "name_ko": current_product["name_ko"],
                    "price": current_product["price"],
                    "shop_id": current_product["shop_id"],
                    "shop_name": current_shop["name"] if current_shop else None
                },
                "quantity": item["quantity"],
                "saving_per_item": 0,
                "total_saving": 0,
                "confidence_score": 0.88,
                "ai_message_ko": "",
                "ai_message_en": ""
            })

    total_possible_saving = sum(
        recommendation["total_saving"]
        for recommendation in recommendations
    )

    if total_possible_saving > 0:
        ai_summary_ko = f"AI가 장바구니 전체를 분석한 결과, 최대 {total_possible_saving}원을 절약할 수 있는 가격 개선 기회를 발견했습니다."
        ai_summary_en = f"AI analyzed the full cart and found price optimization opportunities worth up to {total_possible_saving} KRW."
    else:
        ai_summary_ko = ""
        ai_summary_en = ""

    return {
        "message": "AI price recommendation completed",
        "total_possible_saving": total_possible_saving,
        "ai_summary_ko": ai_summary_ko,
        "ai_summary_en": ai_summary_en,
        "recommendations": recommendations
    }

shops = [
    # 2 x 6 mixed layout: same-category shops are not placed next to each other
    {"id": 1, "name": "Meat Shop 1", "category": "meat", "x": 2, "y": 4},
    {"id": 4, "name": "Vegetable Shop 1", "category": "vegetable", "x": 5, "y": 4},
    {"id": 7, "name": "Fish Shop 1", "category": "fish", "x": 8, "y": 4},
    {"id": 10, "name": "Fruit Shop 1", "category": "fruit", "x": 11, "y": 4},
    {"id": 2, "name": "Meat Shop 2", "category": "meat", "x": 14, "y": 4},
    {"id": 5, "name": "Vegetable Shop 2", "category": "vegetable", "x": 17, "y": 4},

    {"id": 8, "name": "Fish Shop 2", "category": "fish", "x": 2, "y": 10},
    {"id": 11, "name": "Fruit Shop 2", "category": "fruit", "x": 5, "y": 10},
    {"id": 3, "name": "Meat Shop 3", "category": "meat", "x": 8, "y": 10},
    {"id": 6, "name": "Vegetable Shop 3", "category": "vegetable", "x": 11, "y": 10},
    {"id": 9, "name": "Fish Shop 3", "category": "fish", "x": 14, "y": 10},
    {"id": 12, "name": "Fruit Shop 3", "category": "fruit", "x": 17, "y": 10},
]
@app.get("/shops")
def get_shops():
    return shops

@app.get("/map", response_class=HTMLResponse)
def show_market_map():
    shop_cards = ""

    for shop in shops:
        left = shop["x"] * 45 + 90
        top = shop["y"] * 45 + 35

        shop_cards += f'''
        <div class="shop {shop["category"]}" style="left: {left}px; top: {top}px;">
            <strong>{shop["name"]}</strong><br>
            <span>{shop["category"]}</span><br>
            <small>({shop["x"]}, {shop["y"]})</small>
        </div>
        '''

    route_svg = ""
    route_info = ""
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Market Map</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                padding: 30px;
            }}

            .map {{
                position: relative;
                width: 960px;
                height: 720px;
                background-image:
                    linear-gradient(#ddd 1px, transparent 1px),
                    linear-gradient(90deg, #ddd 1px, transparent 1px);
                background-size: 45px 45px;
                background-color: white;
                border: 3px solid #333;
                border-radius: 10px;
            }}

            .shop {{
                position: absolute;
                width: 125px;
                height: 70px;
                border: 2px solid #333;
                border-radius: 8px;
                text-align: center;
                padding-top: 10px;
                box-sizing: border-box;
                font-size: 13px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
                transform: translate(-50%, -50%);
            }}

            .route-layer {{
                position: absolute;
                left: 0;
                top: 0;
                width: 960px;
                height: 720px;
                pointer-events: none;
                z-index: 1;
            }}

            .shop, .hub {{
                z-index: 2;
            }}

            .route-info {{
                margin-top: 20px;
                padding: 15px;
                background: white;
                border: 2px solid #333;
                border-radius: 8px;
                width: 860px;
            }}

            .meat {{ background: #ffd6d6; }}
            .vegetable {{ background: #d8ffd6; }}
            .fish {{ background: #d6ecff; }}
            .fruit {{ background: #fff0c2; }}

            .hub {{
                position: absolute;
                left: 90px;
                top: 350px;
                width: 120px;
                height: 70px;
                background: #eeeeee;
                border: 3px dashed #222;
                border-radius: 8px;
                text-align: center;
                padding-top: 12px;
                box-sizing: border-box;
                font-size: 13px;
                transform: translate(-50%, -50%);
            }}
        </style>
    </head>
    <body>
        <h1>Virtual Market Map</h1>
        <p>Each shop is placed using x, y coordinates from the backend.</p>

        <div class="map">
            <svg class="route-layer">
                {route_svg}
            </svg>
            <div class="hub">
                <strong>Logistics Hub</strong><br>
                (0, 7)
            </div>
            {shop_cards}
        </div>
        {route_info}
    </body>
    </html>
    '''


@app.get("/route-map", response_class=HTMLResponse)
def show_route_map():
    if not cart:
        return '''
        <h1>Cart is empty</h1>
        <p>Add products to cart first, then open <a href="/route-map">/route-map</a>.</p>
        <p>Go to <a href="/docs">/docs</a> to test POST /cart/items.</p>
        '''

    needed_shop_ids = set()

    for item in cart:
        product = next((p for p in products if p["id"] == item["product_id"]), None)
        if product:
            needed_shop_ids.add(product["shop_id"])

    target_shops = [
        shop for shop in shops
        if shop["id"] in needed_shop_ids
    ]

    start = HUB_LOCATION.copy()
    route_result = calculate_route(start, target_shops, return_to_hub=True)
    route = route_result["route"]

    points = [start] + route
    route_svg = ""

    for i in range(len(points) - 1):
        x1 = points[i]["x"] * 45 + 90
        y1 = points[i]["y"] * 45 + 35
        x2 = points[i + 1]["x"] * 45 + 90
        y2 = points[i + 1]["y"] * 45 + 35
        route_svg += f'''
        <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" stroke-width="5" stroke-dasharray="8,6" />
        <circle cx="{x2}" cy="{y2}" r="7" fill="black" />
        '''

    shop_cards = ""

    for shop in shops:
        left = shop["x"] * 45 + 90
        top = shop["y"] * 45 + 35
        shop_cards += f'''
        <div class="shop {shop["category"]}" style="left: {left}px; top: {top}px;">
            <strong>{shop["name"]}</strong><br>
            <span>{shop["category"]}</span><br>
            <small>({shop["x"]}, {shop["y"]})</small>
        </div>
        '''

    route_names = " → ".join(["Logistics Hub"] + [shop["name"] for shop in route])

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rider Route Map</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                padding: 30px;
            }}

            .map {{
                position: relative;
                width: 960px;
                height: 720px;
                background-image:
                    linear-gradient(#ddd 1px, transparent 1px),
                    linear-gradient(90deg, #ddd 1px, transparent 1px);
                background-size: 45px 45px;
                background-color: white;
                border: 3px solid #333;
                border-radius: 10px;
            }}

            .route-layer {{
                position: absolute;
                left: 0;
                top: 0;
                width: 960px;
                height: 720px;
                pointer-events: none;
                z-index: 1;
            }}

            .shop {{
                position: absolute;
                width: 125px;
                height: 70px;
                border: 2px solid #333;
                border-radius: 8px;
                text-align: center;
                padding-top: 10px;
                box-sizing: border-box;
                font-size: 13px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
                z-index: 2;
                transform: translate(-50%, -50%);
            }}

            .meat {{ background: #ffd6d6; }}
            .vegetable {{ background: #d8ffd6; }}
            .fish {{ background: #d6ecff; }}
            .fruit {{ background: #fff0c2; }}

            .hub {{
                position: absolute;
                left: 90px;
                top: 350px;
                width: 120px;
                height: 70px;
                background: #eeeeee;
                border: 3px dashed #222;
                border-radius: 8px;
                text-align: center;
                padding-top: 12px;
                box-sizing: border-box;
                font-size: 13px;
                z-index: 2;
                transform: translate(-50%, -50%);
            }}

            .route-info {{
                margin-top: 20px;
                padding: 15px;
                background: white;
                border: 2px solid #333;
                border-radius: 8px;
                width: 860px;
            }}
        </style>
    </head>
    <body>
        <h1>Rider Route Map</h1>
        <p>This route is calculated from the current cart.</p>

        <div class="map">
            <svg class="route-layer">
                {route_svg}
            </svg>
            <div class="hub">
                <strong>Logistics Hub</strong><br>
                (0, 7)
            </div>
            {shop_cards}
        </div>

        <div class="route-info">
            <h2>Route Result</h2>
            <p><strong>Route:</strong> {route_names}</p>
            <p><strong>Total grid distance:</strong> {route_result["total_grid_distance"]} squares</p>
            <p><strong>Total real distance:</strong> {route_result["total_distance_meters"]} meters</p>
            <p><strong>Estimated pickup time:</strong> {route_result["estimated_time_text"]}</p>
        </div>
    </body>
    </html>
    '''



def manhattan_distance(a, b):
    return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"])


# === Rider Route Grid Pathfinding Helpers ===
def find_grid_path_avoiding_shops(start, end, blocked_positions, max_x=19, max_y=14):
    start_pos = (start["x"], start["y"])
    end_pos = (end["x"], end["y"])

    queue = [(start_pos, [start_pos])]
    visited = {start_pos}

    while queue:
        current_pos, path = queue.pop(0)

        if current_pos == end_pos:
            return path

        x, y = current_pos
        next_positions = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for next_pos in next_positions:
            next_x, next_y = next_pos

            if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                continue

            if next_pos in visited:
                continue

            if next_pos in blocked_positions and next_pos != end_pos:
                continue

            visited.add(next_pos)
            queue.append((next_pos, path + [next_pos]))

    return [start_pos, end_pos]


def build_visual_route_path(route_points):
    """
    Builds a visual rider path using only predefined market aisle lines.

    Aisle structure:
    - Upper aisle: y = 6
    - Lower aisle: y = 8
    - Vertical connectors at each shop column
    - Hub connects to the aisle through x = 2

    The rider can enter a shop only from its nearest aisle point.
    """
    aisle_columns = [2, 5, 8, 11, 14, 17]
    upper_aisle_y = 6
    lower_aisle_y = 8
    hub_connector_x = 2
    hub_connector_y = HUB_LOCATION["y"]

    def add_point(path, x, y):
        if not path or path[-1] != (x, y):
            path.append((x, y))

    def get_shop_aisle_y(point):
        if point["y"] <= 7:
            return upper_aisle_y
        return lower_aisle_y

    def move_on_aisles(start_access, end_access):
        path = []
        start_x, start_y = start_access
        end_x, end_y = end_access

        add_point(path, start_x, start_y)

        if start_y != end_y:
            nearest_connector_x = min(
                aisle_columns,
                key=lambda column_x: abs(column_x - start_x) + abs(column_x - end_x)
            )

            add_point(path, nearest_connector_x, start_y)
            add_point(path, nearest_connector_x, end_y)

        add_point(path, end_x, end_y)
        return path

    def get_access_point(point):
        if point["name"] == HUB_LOCATION["name"]:
            return (hub_connector_x, hub_connector_y)

        shop_position = (point["x"], point["y"])
        is_shop = any((shop["x"], shop["y"]) == shop_position for shop in shops)

        if is_shop:
            return (point["x"], get_shop_aisle_y(point))

        return (point["x"], point["y"])

    visual_path = []

    for i in range(len(route_points) - 1):
        start = route_points[i]
        end = route_points[i + 1]
        segment_path = []

        start_access = get_access_point(start)
        end_access = get_access_point(end)

        add_point(segment_path, start["x"], start["y"])

        if (start["x"], start["y"]) != start_access:
            add_point(segment_path, start_access[0], start_access[1])

        aisle_path = move_on_aisles(start_access, end_access)
        for x, y in aisle_path[1:]:
            add_point(segment_path, x, y)

        if (end["x"], end["y"]) != end_access:
            add_point(segment_path, end["x"], end["y"])

        if i == 0:
            visual_path.extend(segment_path)
        else:
            visual_path.extend(segment_path[1:])

    return [
        {
            "name": "Route Point",
            "x": x,
            "y": y
        }
        for x, y in visual_path
    ]

def build_svg_path_d(points, grid_size=45, x_offset=90, y_offset=35, corner_radius=18):
    if not points:
        return ""

    screen_points = [
        {
            "x": point["x"] * grid_size + x_offset,
            "y": point["y"] * grid_size + y_offset
        }
        for point in points
    ]

    if len(screen_points) == 1:
        point = screen_points[0]
        return f'M {point["x"]} {point["y"]}'

    path_d = f'M {screen_points[0]["x"]} {screen_points[0]["y"]}'

    for i in range(1, len(screen_points) - 1):
        prev_point = screen_points[i - 1]
        current_point = screen_points[i]
        next_point = screen_points[i + 1]

        incoming_dx = current_point["x"] - prev_point["x"]
        incoming_dy = current_point["y"] - prev_point["y"]
        outgoing_dx = next_point["x"] - current_point["x"]
        outgoing_dy = next_point["y"] - current_point["y"]

        incoming_length = max(abs(incoming_dx), abs(incoming_dy))
        outgoing_length = max(abs(outgoing_dx), abs(outgoing_dy))

        radius = min(corner_radius, incoming_length / 2, outgoing_length / 2)

        before_corner_x = current_point["x"]
        before_corner_y = current_point["y"]
        after_corner_x = current_point["x"]
        after_corner_y = current_point["y"]

        if incoming_dx > 0:
            before_corner_x -= radius
        elif incoming_dx < 0:
            before_corner_x += radius

        if incoming_dy > 0:
            before_corner_y -= radius
        elif incoming_dy < 0:
            before_corner_y += radius

        if outgoing_dx > 0:
            after_corner_x += radius
        elif outgoing_dx < 0:
            after_corner_x -= radius

        if outgoing_dy > 0:
            after_corner_y += radius
        elif outgoing_dy < 0:
            after_corner_y -= radius

        path_d += f' L {before_corner_x} {before_corner_y}'
        path_d += f' Q {current_point["x"]} {current_point["y"]} {after_corner_x} {after_corner_y}'

    last_point = screen_points[-1]
    path_d += f' L {last_point["x"]} {last_point["y"]}'

    return path_d

def format_duration(seconds):
    seconds = int(round(seconds))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    if hours > 0:
        return f"{hours} hr {minutes} min {remaining_seconds} sec"

    if minutes > 0:
        return f"{minutes} min {remaining_seconds} sec"

    return f"{remaining_seconds} sec"

def calculate_route(start, target_shops, return_to_hub=False):
    current = start
    remaining = target_shops.copy()
    route = []
    total_distance = 0

    while remaining:
        nearest_shop = min(
            remaining,
            key=lambda shop: manhattan_distance(current, shop)
        )

        distance = manhattan_distance(current, nearest_shop)
        total_distance += distance

        route.append(nearest_shop)
        current = nearest_shop
        remaining.remove(nearest_shop)

    if return_to_hub:
        rider_is_at_hub = current["x"] == HUB_LOCATION["x"] and current["y"] == HUB_LOCATION["y"]

        if not rider_is_at_hub:
            total_distance += manhattan_distance(current, HUB_LOCATION)
            route.append(HUB_LOCATION.copy())

    meters_per_square = 10
    rider_speed_mps = 1.5
    pickup_time_per_shop = 30

    real_distance_meters = total_distance * meters_per_square
    walking_time = real_distance_meters / rider_speed_mps
    pickup_stop_count = len([
        point for point in route
        if point["name"] != HUB_LOCATION["name"]
    ])
    pickup_time = pickup_stop_count * pickup_time_per_shop
    estimated_time = walking_time + pickup_time

    estimated_time_seconds = round(estimated_time)

    return {
        "route": route,
        "total_grid_distance": total_distance,
        "meters_per_square": meters_per_square,
        "total_distance_meters": real_distance_meters,
        "rider_speed_mps": rider_speed_mps,
        "pickup_time_per_shop_seconds": pickup_time_per_shop,
        "estimated_time_seconds": estimated_time_seconds,
        "estimated_time_text": format_duration(estimated_time_seconds),
        "return_to_hub": return_to_hub
}

@app.get("/payment/summary")
def get_payment_summary():
    cart_result = get_cart_product_details()

    return {
        "message": "Payment summary created",
        "message_ko": "결제 요약이 생성되었습니다.",
        "items": cart_result["items"],
        "total_price": cart_result["total_price"],
        "available_payment_methods": ["card", "cash", "simple_pay"]
    }


@app.post("/checkout")
def checkout(request: CheckoutRequest):
    global next_order_id

    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    cart_result = get_cart_product_details()
    ai_price_result = get_ai_price_recommendations()
    ai_product_recommendations = get_ai_product_recommendations()

    order_items = [
        {
            "product_id": item["product_id"],
            "quantity": item["quantity"]
        }
        for item in cart
    ]

    payment = {
        "payment_id": f"PAY-{next_order_id}",
        "payment_method": request.payment_method,
        "payment_status": "paid",
        "paid_amount": cart_result["total_price"],
        "paid_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    order = {
        "order_id": next_order_id,
        "status": "pending",
        "pickup_status": "start",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": order_items,
        "total_price": cart_result["total_price"],
        "payment": payment
    }

    orders.append(order)
    next_order_id += 1

    needed_shop_ids = set()

    for item in order_items:
        product = next((p for p in products if p["id"] == item["product_id"]), None)
        if product:
            needed_shop_ids.add(product["shop_id"])

    target_shops = [
        shop for shop in shops
        if shop["id"] in needed_shop_ids
    ]

    start = HUB_LOCATION.copy()
    route_result = calculate_route(start, target_shops, return_to_hub=True)

    order_summary = {
        "order_id": order["order_id"],
        "status": order["status"],
        "created_at": order["created_at"],
        "items": cart_result["items"],
        "total_price": cart_result["total_price"],
        "total_item_count": sum(item["quantity"] for item in order_items),
        "shop_count": len(target_shops),
        "payment": payment
    }

    cart.clear()

    return {
        "message": "Checkout completed",
        "message_ko": "주문 및 결제가 완료되었습니다.",
        "order_summary": order_summary,
        "payment": payment,
        "route_result": route_result,
        "ai_price_recommendations": ai_price_result,
        "ai_product_recommendations": ai_product_recommendations
    }


@app.post("/payment/test")
def test_payment(payment_request: PaymentRequest):
    return {
        "message": "Payment approved",
        "message_ko": "결제가 승인되었습니다.",
        "payment": {
            "payment_id": f"TEST-PAY-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "payment_method": payment_request.payment_method,
            "payment_status": "paid",
            "paid_amount": payment_request.amount,
            "paid_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }


def get_pending_orders():
    return [order for order in orders if order["status"] == "pending"]


def get_active_batch_orders():
    pending_orders = get_pending_orders()

    if not pending_orders:
        rider_state["active_batch_order_ids"] = []
        rider_state["active_batch_started_at"] = None
        return []

    if not rider_state["active_batch_order_ids"]:
        rider_state["active_batch_order_ids"] = [
            order["order_id"]
            for order in pending_orders
        ]
        rider_state["active_batch_started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [
        order for order in pending_orders
        if order["order_id"] in rider_state["active_batch_order_ids"]
    ]


def complete_active_batch_if_rider_returned_to_hub():
    rider_location = rider_state["current_location"]
    rider_is_at_hub = rider_location["x"] == HUB_LOCATION["x"] and rider_location["y"] == HUB_LOCATION["y"]

    if not rider_is_at_hub or not rider_state["active_batch_order_ids"]:
        return

    completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for order in orders:
        if order["order_id"] in rider_state["active_batch_order_ids"] and order["status"] == "pending":
            order["status"] = "completed"
            order["completed_at"] = completed_at

    rider_state["active_batch_order_ids"] = []
    rider_state["active_batch_started_at"] = None


def get_shop_ids_from_orders(order_list):
    needed_shop_ids = set()

    for order in order_list:
        for item in order["items"]:
            product = next((p for p in products if p["id"] == item["product_id"]), None)
            if product:
                needed_shop_ids.add(product["shop_id"])

    return needed_shop_ids


def get_rider_route_result():
    complete_active_batch_if_rider_returned_to_hub()

    pending_orders = get_pending_orders()
    active_batch_orders = get_active_batch_orders()
    needed_shop_ids = get_shop_ids_from_orders(active_batch_orders)
    start = rider_state["current_location"]

    if active_batch_orders:
        target_shops = [
            shop for shop in shops
            if shop["id"] in needed_shop_ids
        ]
        route_mode = "active_batch_pickup_then_return_to_hub"
        message_ko = "현재 배치 주문의 상품을 모두 수령한 뒤 물류 허브로 복귀합니다. 이동 중 새 주문이 들어와도 현재 배치가 끝날 때까지 경로에 추가하지 않습니다."
    else:
        rider_is_at_hub = start["x"] == HUB_LOCATION["x"] and start["y"] == HUB_LOCATION["y"]
        target_shops = [] if rider_is_at_hub else [HUB_LOCATION.copy()]
        route_mode = "return_to_hub" if not rider_is_at_hub else "waiting_at_hub"
        message_ko = "대기 중인 주문이 없어 라이더가 물류 허브로 복귀합니다." if not rider_is_at_hub else "대기 중인 주문이 없어 라이더가 물류 허브에서 대기합니다."

    waiting_order_count = len([
        order for order in pending_orders
        if order["order_id"] not in rider_state["active_batch_order_ids"]
    ])

    route_result = calculate_route(start, target_shops, return_to_hub=True)

    return {
        "message": "Rider route updated",
        "message_ko": message_ko,
        "route_mode": route_mode,
        "return_to_hub_condition": "The rider must return to the Logistics Hub after picking up every item required for the active batch. New orders received during the run wait for the next batch.",
        "update_interval_minutes": 10,
        "last_updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rider_current_location": rider_state["current_location"],
        "rider_last_location_update_at": rider_state["last_location_update_at"],
        "active_batch_order_ids": rider_state["active_batch_order_ids"],
        "active_batch_started_at": rider_state["active_batch_started_at"],
        "waiting_order_count": waiting_order_count,
        "pending_order_count": len(pending_orders),
        "pending_orders": pending_orders,
        "active_batch_orders": active_batch_orders,
        "target_shop_count": len(target_shops),
        "target_shops": target_shops,
        "route_result": route_result
    }


@app.get("/orders")
def get_orders():
    total_sales = sum(
        order["total_price"]
        for order in orders
        if order.get("payment", {}).get("payment_status") == "paid"
    )

    return {
        "orders": orders,
        "pending_order_count": len(get_pending_orders()),
        "total_sales": total_sales
    }


# === Admin App API Endpoints ===
def get_admin_shop_name(shop_id):
    shop = next((s for s in shops if s["id"] == shop_id), None)

    if shop is None:
        return "상점명 없음"

    category_prefix = {
        "meat": "정육점",
        "vegetable": "채소가게",
        "fish": "수산가게",
        "fruit": "과일가게"
    }.get(shop["category"], shop["name"])

    same_category_shops = sorted(
        [s for s in shops if s["category"] == shop["category"]],
        key=lambda s: s["id"]
    )

    shop_number = next(
        (index + 1 for index, same_shop in enumerate(same_category_shops) if same_shop["id"] == shop_id),
        shop_id
    )

    return f"{category_prefix} {shop_number}"


def convert_order_to_admin_order(order):
    admin_products = []
    shop_ids = set()

    for item in order["items"]:
        product = next((p for p in products if p["id"] == item["product_id"]), None)

        if product is None:
            continue

        shop_ids.add(product["shop_id"])
        admin_products.append({
            "id": product["id"],
            "product_id": product["id"],
            "name": product["name_ko"],
            "name_ko": product["name_ko"],
            "price": product["price"],
            "quantity": item["quantity"],
            "shop_id": product["shop_id"],
            "shop_name": get_admin_shop_name(product["shop_id"])
        })

    first_shop_id = min(shop_ids) if shop_ids else None

    pickup_status = order.get("pickup_status", "start")

    if order["status"] == "completed":
        order_stage = "complete"
        pickup_status = "done"
    elif order["status"] in ["picking", "progress"]:
        order_stage = "progress"
    else:
        order_stage = "new"

    return {
        "id": order["order_id"],
        "order_id": order["order_id"],
        "customer": f"고객 {str(order['order_id']).zfill(3)}",
        "customer_name": f"고객 {str(order['order_id']).zfill(3)}",
        "shop": get_admin_shop_name(first_shop_id) if first_shop_id else "여러 상점",
        "shop_name": get_admin_shop_name(first_shop_id) if first_shop_id else "여러 상점",
        "orderStage": order_stage,
        "order_stage": order_stage,
        "order_status": order_stage,
        "pickupStatus": pickup_status,
        "pickup_status": pickup_status,
        "status": pickup_status,
        "products": admin_products,
        "items": admin_products,
        "total_price": order["total_price"],
        "payment_status": order.get("payment", {}).get("payment_status", "unknown"),
        "created_at": order["created_at"]
    }


@app.get("/api/admin/orders")
def get_admin_orders():
    admin_orders = [convert_order_to_admin_order(order) for order in orders]

    return {
        "orders": admin_orders,
        "new_count": len([order for order in admin_orders if order["orderStage"] == "new"]),
        "progress_count": len([order for order in admin_orders if order["orderStage"] == "progress"]),
        "complete_count": len([order for order in admin_orders if order["orderStage"] == "complete"])
    }


@app.get("/api/admin/sales-summary")
def get_admin_sales_summary():
    total_sales = sum(
        order["total_price"]
        for order in orders
        if order.get("payment", {}).get("payment_status") == "paid"
    )

    completed_sales = sum(
        order["total_price"]
        for order in orders
        if order["status"] == "completed" and order.get("payment", {}).get("payment_status") == "paid"
    )

    return {
        "today_sales": total_sales,
        "total_sales": total_sales,
        "completed_sales": completed_sales,
        "order_count": len(orders),
        "paid_order_count": len([
            order for order in orders
            if order.get("payment", {}).get("payment_status") == "paid"
        ])
    }


@app.post("/api/admin/orders/{order_id}/stage")
def update_admin_order_stage(order_id: int, payload: dict):
    order = next((order for order in orders if order["order_id"] == order_id), None)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    order_stage = payload.get("orderStage") or payload.get("order_stage")
    pickup_stage = payload.get("stage") or payload.get("pickupStatus") or payload.get("pickup_status")

    if pickup_stage in ["start", "moving", "done"]:
        order["pickup_status"] = pickup_stage

        if pickup_stage == "start" and order["status"] != "completed":
            order["status"] = "pending"
        elif pickup_stage in ["moving", "done"] and order["status"] != "completed":
            order["status"] = "progress"

    if order_stage in ["complete", "done"]:
        order["status"] = "completed"
        order["pickup_status"] = "done"
        order["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif order_stage == "progress":
        order["status"] = "progress"
        if order.get("pickup_status") == "start":
            order["pickup_status"] = "moving"
    elif order_stage == "new":
        order["status"] = "pending"
        order["pickup_status"] = "start"

    return {
        "message": "Admin order stage updated",
        "order": convert_order_to_admin_order(order)
    }


@app.get("/rider/route")
def get_rider_route():
    return get_rider_route_result()


@app.post("/rider/location")
def update_rider_location(location: RiderLocationUpdate):
    rider_state["current_location"] = {
        "name": location.name,
        "x": location.x,
        "y": location.y
    }
    rider_state["last_location_update_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    complete_active_batch_if_rider_returned_to_hub()

    return {
        "message": "Rider location updated",
        "message_ko": "라이더 현재 위치가 갱신되었습니다.",
        "rider_current_location": rider_state["current_location"],
        "updated_route": get_rider_route_result()
    }


@app.post("/rider/reset-location")
def reset_rider_location():
    rider_state["current_location"] = HUB_LOCATION.copy()
    rider_state["last_location_update_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rider_state["active_batch_order_ids"] = []
    rider_state["active_batch_started_at"] = None

    return {
        "message": "Rider location reset",
        "message_ko": "라이더 위치가 물류 허브로 초기화되었습니다.",
        "rider_current_location": rider_state["current_location"],
        "updated_route": get_rider_route_result()
    }


@app.post("/orders/{order_id}/complete")
def complete_order(order_id: int):
    order = next((order for order in orders if order["order_id"] == order_id), None)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    order["status"] = "completed"
    order["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    updated_route = get_rider_route_result()

    return {
        "message": "Order completed",
        "message_ko": "주문 처리가 완료되었습니다. 대기 주문이 없으면 라이더는 물류 허브로 복귀합니다.",
        "order": order,
        "updated_route": updated_route
    }


@app.get("/rider-monitor", response_class=HTMLResponse)
def show_rider_monitor():
    rider_result = get_rider_route_result()
    route = rider_result["route_result"]["route"]
    pending_orders = rider_result["pending_orders"]

    start_location = rider_result["rider_current_location"]
    route_names = " → ".join([start_location["name"]] + [shop["name"] for shop in route])

    route_points = [start_location] + route
    visual_route_points = build_visual_route_path(route_points)
    stop_positions = {
        (point["x"], point["y"]): point["name"]
        for point in route_points
    }

    route_point_data = []
    for point in visual_route_points:
        point_key = (point["x"], point["y"])
        route_point_data.append({
            "name": stop_positions.get(point_key, "Moving"),
            "x": point["x"],
            "y": point["y"]
        })

    shop_cards = ""
    for shop in shops:
        left = shop["x"] * 45 + 90
        top = shop["y"] * 45 + 35

        shop_cards += f'''
        <div class="shop {shop["category"]}" style="left: {left}px; top: {top}px;">
            <strong>{shop["name"]}</strong><br>
            <span>{shop["category"]}</span><br>
            <small>({shop["x"]}, {shop["y"]})</small>
        </div>
        '''

    route_path_d = build_svg_path_d(visual_route_points)
    route_svg = f'''
        <path id="rider-path" d="{route_path_d}" fill="none" stroke="black" stroke-width="5" stroke-dasharray="8,6" stroke-linecap="round" stroke-linejoin="round" />
    '''

    for point in route_points[1:]:
        cx = point["x"] * 45 + 90
        cy = point["y"] * 45 + 35
        route_svg += f'''
        <circle cx="{cx}" cy="{cy}" r="7" fill="black" />
        '''

    order_rows = ""
    for order in pending_orders:
        item_names = []

        for item in order["items"]:
            product = next((p for p in products if p["id"] == item["product_id"]), None)
            if product:
                shop = next((s for s in shops if s["id"] == product["shop_id"]), None)
                shop_name = shop["name"] if shop else "Unknown Shop"
                item_names.append(f'{product["name_ko"]} ({shop_name}) x {item["quantity"]}')

        payment_status = order.get("payment", {}).get("payment_status", "unknown")

        order_rows += f'''
        <tr>
            <td>{order["order_id"]}</td>
            <td>{order["created_at"]}</td>
            <td>{order["status"]}</td>
            <td>{payment_status}</td>
            <td>{", ".join(item_names)}</td>
            <td>{order["total_price"]}원</td>
        </tr>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rider Monitor</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                padding: 30px;
            }}

            .card {{
                background: white;
                border: 2px solid #333;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                width: 960px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                background: white;
            }}

            th, td {{
                border: 1px solid #999;
                padding: 10px;
                text-align: left;
            }}

            th {{
                background: #eee;
            }}

            .map {{
                position: relative;
                width: 960px;
                height: 720px;
                background-image:
                    linear-gradient(#ddd 1px, transparent 1px),
                    linear-gradient(90deg, #ddd 1px, transparent 1px);
                background-size: 45px 45px;
                background-color: white;
                border: 3px solid #333;
                border-radius: 10px;
                margin-bottom: 20px;
            }}

            .route-layer {{
                position: absolute;
                left: 0;
                top: 0;
                width: 960px;
                height: 720px;
                pointer-events: none;
                z-index: 1;
            }}

            .shop {{
                position: absolute;
                width: 125px;
                height: 70px;
                border: 2px solid #333;
                border-radius: 8px;
                text-align: center;
                padding-top: 10px;
                box-sizing: border-box;
                font-size: 13px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
                z-index: 2;
                transform: translate(-50%, -50%);
            }}

            .hub {{
                position: absolute;
                left: 90px;
                top: 350px;
                width: 120px;
                height: 70px;
                background: #eeeeee;
                border: 3px dashed #222;
                border-radius: 8px;
                text-align: center;
                padding-top: 12px;
                box-sizing: border-box;
                font-size: 13px;
                z-index: 2;
                transform: translate(-50%, -50%);
            }}

            .meat {{ background: #ffd6d6; }}
            .vegetable {{ background: #d8ffd6; }}
            .fish {{ background: #d6ecff; }}
            .fruit {{ background: #fff0c2; }}

            .rider-dot {{
                position: absolute;
                width: 22px;
                height: 22px;
                background: #1e88e5;
                border: 3px solid white;
                border-radius: 50%;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
                z-index: 5;
                transition: none;
                transform: translate(-50%, -50%);
            }}

            .location-label {{
                font-weight: bold;
                color: #1e88e5;
            }}
        </style>
    </head>
    <body>
        <h1>Rider Monitor</h1>
        <p>The rider follows the hidden aisle route, moves at half of the estimated real pickup time, and sends its simulated location back to the backend while moving. Refresh manually after adding new orders to recalculate the route from the rider's latest simulated location.</p>

        <div class="card">
            <h2>Route Update</h2>
            <p><strong>Last updated:</strong> {rider_result["last_updated_at"]}</p>
            <p><strong>Rider current location:</strong> {rider_result["rider_current_location"]["name"]} ({rider_result["rider_current_location"]["x"]}, {rider_result["rider_current_location"]["y"]})</p>
            <p><strong>Route mode:</strong> {rider_result["route_mode"]}</p>
            <p><strong>Pending orders:</strong> {rider_result["pending_order_count"]}</p>
            <p><strong>Active batch orders:</strong> {rider_result["active_batch_order_ids"]}</p>
            <p><strong>New orders waiting for next batch:</strong> {rider_result["waiting_order_count"]}</p>
            <p><strong>Target shops:</strong> {rider_result["target_shop_count"]}</p>
            <p><strong>Return-to-hub condition:</strong> {rider_result["return_to_hub_condition"]}</p>
            <p><strong>Route:</strong> {route_names}</p>
            <p><strong>Estimated pickup time:</strong> {rider_result["route_result"]["estimated_time_text"]}</p>
        </div>

        <div class="card">
            <h2>Live Rider Route Simulation</h2>
            <p><strong>Current simulated position:</strong> <span id="current-location" class="location-label">{start_location["name"]}</span></p>
            <div class="map">
                <svg class="route-layer">
                    {route_svg}
                </svg>
                <div class="hub">
                    <strong>Logistics Hub</strong><br>
                    (0, 7)
                </div>
                {shop_cards}
                <div id="rider-dot" class="rider-dot"></div>
            </div>
        </div>

        <div class="card">
            <h2>Pending Orders</h2>
            <table>
                <tr>
                    <th>Order ID</th>
                    <th>Created At</th>
                    <th>Status</th>
                    <th>Payment</th>
                    <th>Items</th>
                    <th>Total Price</th>
                </tr>
                {order_rows}
            </table>
        </div>
        <script>
            const routePoints = {route_point_data};
            const riderDot = document.getElementById("rider-dot");
            const currentLocationText = document.getElementById("current-location");
            const riderPath = document.getElementById("rider-path");

            let animationStart = null;
            const estimatedPickupSeconds = {rider_result["route_result"]["estimated_time_seconds"]};
            const animationDuration = Math.max(9000, estimatedPickupSeconds * 500);
            let lastSentRouteIndex = -1;

            function updateCurrentLocation(progress) {{
                if (routePoints.length === 0) {{
                    currentLocationText.textContent = "No pending route";
                    return;
                }}

                const index = Math.min(
                    routePoints.length - 1,
                    Math.floor(progress * routePoints.length)
                );

                const point = routePoints[index];
                currentLocationText.textContent = `${{point.name}} (${{point.x}}, ${{point.y}})`;
            }}

            function animateRider(timestamp) {{
                if (!riderPath || routePoints.length === 0) {{
                    riderDot.style.display = "none";
                    currentLocationText.textContent = "No pending route";
                    return;
                }}

                if (!animationStart) {{
                    animationStart = timestamp;
                }}

                const elapsed = timestamp - animationStart;
                const progress = Math.min(elapsed / animationDuration, 1);
                const pathLength = riderPath.getTotalLength();
                const currentPoint = riderPath.getPointAtLength(pathLength * progress);

                riderDot.style.display = "block";
                riderDot.style.left = currentPoint.x + "px";
                riderDot.style.top = currentPoint.y + "px";

                updateCurrentLocation(progress);

                const routeIndex = Math.min(
                    routePoints.length - 1,
                    Math.floor(progress * routePoints.length)
                );

                if (routeIndex !== lastSentRouteIndex) {{
                    lastSentRouteIndex = routeIndex;
                    const simulatedPoint = routePoints[routeIndex];

                    if (simulatedPoint) {{
                        fetch("/rider/location", {{
                            method: "POST",
                            headers: {{
                                "Content-Type": "application/json"
                            }},
                            body: JSON.stringify({{
                                name: simulatedPoint.name,
                                x: simulatedPoint.x,
                                y: simulatedPoint.y
                            }})
                        }}).catch(() => {{
                            console.log("Failed to update rider location");
                        }});
                    }}
                }}

                if (progress < 1) {{
                    requestAnimationFrame(animateRider);
                }} else {{
                    const lastPoint = routePoints[routePoints.length - 1];
                    currentLocationText.textContent = `${{lastPoint.name}} - route simulation completed`;
                }}
            }}

            requestAnimationFrame(animateRider);
        </script>
    </body>
    </html>
    '''
# === AI Product Recommendations Endpoint ===
@app.get("/ai/product-recommendations")
def get_ai_product_recommendations_endpoint():
    return get_ai_product_recommendations()