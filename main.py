from fastapi import FastAPI
from bike import Bike

app = FastAPI()
Bike_list = [
    {
        "id": 1,
        "brand": "Honda",
        "Engine_capacity": "120cc",
        "price": "12000"
    },
    {
        "id": 2,
        "brand": "Hero",
        "Engine_capacity": "150cc",
        "price": "10000"
    }
]


@app.get("/")
def Bike_shop():
    print(f"inside Bike_shop")
    return {"message": "Welcome to the Bike Shop"}


@app.post("/new-Bike")
def add_new_Bike(Bike: Bike):
    Bike_list.append(Bike.dict())
    return Bike_list


@app.get("/Bikes")
def get_all_Bikes():
    return Bike_list


@app.delete("/Bikes/{id}")
def remove_bikes_by_id(id: int):
    print(f"remove_desktop_by_id|id{id}")
    return Bike_list

# if __name__ == '__main__':
#    print(f"startup |")
