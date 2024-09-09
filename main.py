from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def populate_db():
    """populating db"""
    db = client.test
    db.cats.insert_many(
        [
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
            {
                "name": "Boris",
                "age": 12,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Murzik",
                "age": 1,
                "features": ["ходить в лоток", "дає себе гладити", "чорний"],
            },
            {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"],
            },
        ]
    )


def read_all():
    """returning all db records"""
    db = client.test
    result = db.cats.find({})
    for el in result:
        print(el)


def find_by_name(name):
    """returning records by name input"""
    db = client.test
    result = db.cats.find({"name": name})
    for el in result:
        print(el)


def update_age_by_name(name, age):
    """updating age by name input"""
    db = client.test
    db.cats.update_one({"name": name}, {"$set": {"age": age}})
    result = db.cats.find_one({"name": name})
    print(result)


def add_feature_by_name(name, feature):
    """adding feature by name input"""
    db = client.test
    db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
    result = db.cats.find_one({"name": name})
    print(result)


def delete_by_name(name):
    """deleting record by name input"""
    db = client.test
    db.cats.delete_one({"name": name})
    result = db.cats.find_one({"name": name})
    print(result)


def delete_all_records():
    """deleting record by name input"""
    db = client.test
    db.cats.delete_many({})


uri = "mongodb+srv://<connection:string>/test?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(
    uri, server_api=ServerApi("1"), tls=True, tlsAllowInvalidCertificates=True
)

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


if __name__ == "__main__":

    populate_db()
    read_all()
    print("----------------------------------------")
    find_by_name("barsik")
    print("----------------------------------------")
    update_age_by_name("barsik", 5)
    print("----------------------------------------")
    add_feature_by_name("barsik", "sleeps")
    print("----------------------------------------")
    delete_by_name("Boris")
    print("----------------------------------------")
    delete_all_records()
    print("----------------------------------------")
    read_all()
