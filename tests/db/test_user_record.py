# Sample DB validation test
from utils.db_utils import query_db

def test_user_record():
    result = query_db("SELECT * FROM users WHERE username = 'user'")
    assert result
