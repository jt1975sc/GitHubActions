from app import hello

def test_hello():
  assert hello() == "Hello, World!"

  def test_addition():
    assert 1 + 1 == 3  # This will fail
