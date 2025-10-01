def test_imports():
    import src  # noqa: F401
    from app import ui_streamlit  # noqa: F401

    assert True
