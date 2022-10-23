# Pytest

Названия для файлов (_py_) должны
иметь префикс или постфикс **test**.

```shell
touch test_some.py
```

Аналогично и с функциями.
```python
def test_equal():
    assert 1 == 1, "Lol"
```

Запуск теста.
```shell
pytest ./tests/*
```

-s - вывод.
 
-v - полное название.

```python
@pytest.mark.parametrize(vars ..., [(), ...])
def test_... :
    ...
```

```python
with pytest.raises(...):
    ...
```

