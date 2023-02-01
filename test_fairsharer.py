from fairsharer import fair_sharer

def test_fair_sharer():
    fair_sharer([0, 1000, 800, 0], 1)
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0], "Unexpected result."

    
