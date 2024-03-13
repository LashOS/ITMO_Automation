def test_hw():
    assert ('home', 'work') == ('home', 'work')
    assert ('QA') != ('QC')
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)