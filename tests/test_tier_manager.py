from src.tier_manager import TierManager

def test_put_and_get():
    tm = TierManager()
    tm.put("a", "alpha")
    assert tm.get("a") == "alpha"
