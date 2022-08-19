from metadata import get_metadata


def test_get_metadata():
    header = ['property0', 'property1', 'property2', 'metric0', 'metric0']
    metrics, properties = get_metadata(header)
    assert metrics == ['metric0', 'metric0']
    assert properties == ['property0', 'property1', 'property2']
