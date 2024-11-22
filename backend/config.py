import pytest
from dotenv import load_dotenv
import os


load_dotenv()


@pytest.fixture
def base_url():
    base_url = os.getenv("BASE_URL")
    return base_url
