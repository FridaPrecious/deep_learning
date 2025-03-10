from pymongo import MongoClient

uri = "mongodb+srv://anyanguprecious:Pretty2003.@cluster0.iufpx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&readPreference=primary"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ Error:", e)
