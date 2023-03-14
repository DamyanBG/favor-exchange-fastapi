import databases
import sqlalchemy
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST_URL')}:5432/favorexchange"
TEST_DATABASE_URL = "postgresql://postgres:3dprint@localhost:5433/Test_favor_exchange"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Add this function to create a new instance of the database for testing
async def get_test_database():
    return await databases.Database(TEST_DATABASE_URL).connect()
