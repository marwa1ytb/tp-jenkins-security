from app import add

def test_add():
    assert add(2, 3) == 5
```

---

**Fichier 3 — `requirements.txt`**
```
pytest
flask==2.0.1
requests==2.18.0
