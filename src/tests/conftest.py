
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:
    pass


import pytest
from server import create_flask_app

@pytest.fixture
def client():
    app = create_flask_app({"TESTING": True})

    with app.test_client() as client:
        yield client