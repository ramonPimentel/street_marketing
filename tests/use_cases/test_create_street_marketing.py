from app.use_cases.create_street_marketing import CreateStreetMarketing

class TestCreateStreetMarketing:
  def test_fail():
    result = CreateStreetMarketing({}).execute()
    assert result is None