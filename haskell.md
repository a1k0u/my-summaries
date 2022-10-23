# 2. Типы и классы типов.

В Haskell есть механизм вывода типов, поэтому не нужно его указывать,
так как язык самостоятельно выведет его.

```haskell
ghci> :t True
True :: Bool
```

Символ `::` означает: "имеет тип".

```haskell
ghci> :t "Hello, my friend!"
"Hello, my friend!" :: [Char]

ghci> :t (True, 1, "a")
(True, 1, "a") :: (Bool, Int, Char)
```

У функций тоже есть типы, хорошим тоном является указывать их явно.

```haskell
foo :: [Char] -> [Char]
foo st = [c | c <- st, c `elem` ['A' .. 'Z']]
```

**Встроенные типы в языке Haskell:**

- **Int** - в зависимости от разрядности системы принимает значения от
-2^n до 2^n - 1, где n - разрядность.
- **Integer** -  а-ля не имеет ограничений, то есть очень большой.
> Int работает более эффективно в сравнении с Integer.
- **Float** - число с плавающей точкой одинарной точности.
- **Double** - двойная точность. Для предоставления чисел используется
вдвое больше битов.
- **Bool**, **Char** (`литералы в одинарных кавычках`), **()**
(`кортеж`): теоретически количество типов кортежей бесконечно.

> **a** - типовая переменная, то есть **_a_** может быть любым типом.
```haskell
ghci> :t head
head :: [a] -> [a] 
```
> Подобные элементы в других языках называют "дженериками", но только в
> Haskell - это мощный инструмент, так как позволяет нам легко писать
> самые общие функции.

```haskell
ghci> :t fst
fst :: (a, b) -> a
```

**Класс типов** - интерфейс, определяющий некоторое поведение.
Такие операторы, как (==), являются функциями.
```haskell
ghci> :t (==)
(==) :: (Eq a) => a -> a -> Bool
```

> Всё, что находится перед символом **=>**, называется _ограничителем
класса_. Тип этих двух значений должен быть экземпляром класса _Eq_.

**Класс типа Eq** - предоставляет интерфейс для сравнения двух значений
на равенство.

> Класс типов в Haskell /= классы в ООП ЯП.

- `Ord -> Ordering = EQ | GT | LT.`
- `Show -> show` _(вывод)_
- `Read -> read` _(интерпретатор GHCi вычисляет, определяя тип)_
```haskell
ghci> read "8" + 3
11
ghci> read "(3, 'a')" :: (Int, Char)
(3, 'a')
ghci> [read "True", False]
[True, False]
```
**Аннотация типа** - явный способ указать, какого типа должно быть выражение.

- **Enum** - экземпляры этого типа можно пронумеровать.
```haskell
ghci> [3 .. 5]
[3, 4, 5]
```

- **Bounded** - экземпляры класса имеют верхнюю и нижнюю границу.
```haskell
ghci> minBound :: Int
-2147483648
```

- **Num** - класс типов для чисел. `(Double, Int, ...)`
```haskell
ghci> :t (*)
(*) :: (Num a) => a -> a -> a
```

- **Floating** - числа с плавающей точкой.

- **Integral** - целые числа.
```haskell
ghci> fromIntegral (length [1, 2]) + 3.2
5.2
ghci> :t fromIntegral
fromIntegral :: (Num b, Integral a) => a -> b
ghci> :t length
length :: [a] -> Int
```

# 7. Создание новых типов и классов типов.

Один из способов создать свой собственный тип - `data`.

```haskell
ghci> data Bool = False | True
ghci> data Shape = Circle Float Float Float | Rec Float Float Float Float
```

Когда мы записываем конструктор значения типа, опционально можем
добавить типы после имени; эти типы определяют, какие значения
будет содержать тип с данным конструктором.

```haskell
ghci> :t Circle
Circle :: Float -> Float -> Float -> Shape
```

```haskell
ghci> area :: Shape -> Float
ghci> area (Circle _ _ r) = pi * r ^ 2
ghci> area $ Circle 3 4 10
314.15927
```

Чтобы определить для нашего типа `Shape` экземпляр класса `Show`, 
модифицируем его следующим образом.
```haskell
data Shape = Circle Float Float Float deriving (Show)        
```

```haskell
ghci> Circle 10 20 30
Cirlce 10.0 20.0 30.0
```

**Конструкторы значений** - это функция.

```haskell
data Point = Point Float Float deriving (Show)
data Shape = Circle Point Float | Rectangle ... deriving (Show)
```

Подвигаем наши фигуры:
```haskell
nudge :: Shape -> Float -> Float -> Shape
nudge (Circle (Point x y) r) a b = Circle (Point (x + a) (y + b)) r
```

Создадим тип, отображающий информацию о человеке.

```haskell
data Person = Person String String Int Float String String deriving (Show)
```

```haskell
ghci> let guy = Person "Фредди" "Крюгер" 43 184.2 "526–2928" "Эскимо" ghci> guy
Person "Фредди" "Крюгер" 43 184.2 "526–2928" "Эскимо"
```

Но есть синтаксис для более читаемой формы, он же генерирует
функции для извлечения полей. 

```haskell
data Person = Person { firstName :: String 
                     , lastName :: String
                     , age :: Int
                     , height :: Float
                     , phoneNumber :: String
                     , flavor :: String } deriving (Show)
```

```haskell
ghci> :t flavor
flavor :: Person –> String
ghci> :t firstName
firstName :: Person –> String
```

