from tinydb import TinyDB, Query

db = TinyDB("veri.json")
db.insert({
    "d": "a",
})