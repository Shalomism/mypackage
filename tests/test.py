from mypackage import myModule

def test_top_n():
    """
    Make sure top n works
    """

    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect'
    