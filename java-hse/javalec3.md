Не примитивные типы

String

В Java нет перегрузки операторов, но String в этом смысле "особый". Его нельзя сделать инструментами чистой джавы, это не тоже самые, что массив символов, нет нулевого байта. Все строковые литералы кешируются, можно создать не только через new, но и через массив литералов.

TODO: массив литералов
TODO: как устроены строки в Java (внутри)

Строки - не изменяемый объект, внутри у него лежит "массив символов". Как сделать substring? Очевидный способ взять кусок этого массива, скопировать его куда-то; сохранить ссылку на массив но ещё и offset от начала, это лучше по экономии памяти. Также думали до Java 7.xx.

Помните мы на первой лекции говорили про утечки памяти в Java, что мы можем хранить большой объект в памяти, до которого никогда недоберемся. Типичный пример - работа со строками. Казалось бы хорошая идея хранить substring с запоминанием offset, но в реальности это приводит к утечкам памяти. 

Предствим себе, что мы считали большую строчку. Взяли маленькое подслово, не смотря на это мы храним ссылку на огромный объект, который не будет удален, потому что на него есть ссылка на подслово. Это и есть утечка. Память то экономится, но она течет.

Поэтому в какой версии Java 7.xx от этого отказались, теперь все копируется.

- `int length()` 
- `char charAt(int index)`
- `char[] toCharArray()`
- `substring (int beginIndex)`
- `substring(int beginIndex, int endIndex)`

Мы говорим про ссылочные типы, поэтому оператор == сравнивает ссылки, а не содержимое строки. Строковые литералы кешируются, если в одном месте программы создается строчка "Hello" и в другом месте создаются такая же, то они будут друг другу равны. Но если создать hello через new String от массива char, то они друг другу равны не будут. 

Если нужно нормально сравнить строчки, то equals подходит. Этот метод определен в java.lang.Object, поэтому на вход он принимает Object anObject. В Java потенциально класс может сравниваться не только с себе подобными, а вообще с кем угодно.  

Есть ещё дополнительный метод, который объявлен в String `boolean equalsIgnoreCase(String anotherSting)`. Так как перегрузки операторов всё ещё нет, то используем `int compareTo(String anotherString)` `int compareToIgnoreCase`

Популярные методы:
- boolean startsWith(String str)
- boolean endsWith(String str)
- int indexOf(String str)	// первое вхождение
- int lastIndexOf(String str)

Эти методы все возвращает строчку, они не модифицирующие, а возвращают новую строчку.
- String trim()
- String replace(char oldChar, char newChar)
- String toLowerCase()
- String toUpperCase()

Специфика строк! Конкатенация строк. У строк есть единственный перегруженный оператор, исключение в джава. Это - '+'. Джава предлагает три способа конкатенации строк. 

Способ первый - `String concat(String str)`. Берет строчку на вход, приклеивает к нашей и возвращает результат.

Оператор + (работает, как String Builder)
`String helloWorld = "Hello" + "World!";`

StringBuilder
```java
StringBuilder buf = new StringBuilder();
buf.append("Hello");
buf.append("world");
buf.append('!');
String result = buf.toString();
``` 

Чтобы понять зачем нужен stringBuilder, давайте рассмотрим такой пример:
(наверно на доске был написан похожий пример)

```java
String arr[] = ["aba", "caba", "baba"];
String res = "a";
for (String str : arr) {
	res = res.concat(str);
}
```

Код плох тем, что он работает за квадрат. Чтобы к одной строке прибавить другую нужно выделить память, туда скопировать исходную и добавленную. В итоге сумма блин строк. Альтернатива этому StringBuilder. Ведь это просто список, куда складыаются какие-то строчки, а потом память один раз выделяется и туда за один раз все записывается. Поэтому суммарно в таком случае линия.   

Тааааак воооот. Плюсик - это синтаксический сахар на StringBuilder. Если написать s1 = s2 + s3; То создается StringBuilder, туда кладется две строчки, после делается toString. Не очень понятно зачем в таком виде это делать, но ситуация проясняется если сделать множественную конкатенацию, например s1 = s2 + s3 + .. + sn (цепочка из плюсиков). Когда нужно что использовать?

Очевидно, что StringBuilder нужно использовать в циклах. concat явно лучше не использовать, потому что у "плюсика" есть ещё один плюсик. В целом он работает как StringBuilder, но оптимизирует работу. Понятно, если мы будем складывать строковые литералы, при компиляции можно провести оптимизацию ..

TODO: оптимизации +

 Регулярные выражения
 
 - Регулярные выражения поодерживаются в стандартной библиотеке Java
 
 - boolean matches(String regex) // строка подходит под регулярное выражение
 - String[] split(String regex) // разбивает строку по регулярному выражению
 - String replaceAll(String regex, String replacement)
 - String replaceFirst(String regex, String replacement)
 
 ```java
 Sring str = "a, b, c,d, e";
 String[] items = str.split(", *"); //в исходной строку найдутся все вхождения регулярного выражения, они будут удалены и в этих местах появится разделение. Звездочка (0 или много) строит у пробела
 // items -> "a", "b", "c", "d", "e"
 ```
 
"\\( ([^)]* ) \\)"
  ^  ^  ^   ^  ^
 (1)(2)(3) (2)(1)

1 - символ скобки, он отделяется \, чтобы отличкать символ от логической скобки. Так как мы в Java и не хотим экранированный символ, то \\.
2 - логичская скобка (группа)
3 - [^)] все кроме закрывающей скобки возьми в группу (п.с. открывающую скобку уже взяли в (1)).
Итого берем все, что есть в скобке (раскрываем скобки).

String str = "(aa)(bb)(ccc)";
String result = str.replaceAll(regex, "$1") // $1 - взять то, что выделилось в группе

Классы и ООП

Как выглядит класс? 

/* modifiers */ class Example {
	/* class content: filed and methods */
}

Пока мы знает про public. Он в файле единственный. Из других пакетов мы можем использовать только публичные классы. Зачем нужны не публичные классы? Есть служебные классы, которыми пользуется публичный класс пакета. Важный момент - они не являются приватными, они не являются публичными. (разные вещи)

У каждого поля можно прописать модификатор доступа

class Example {
	/* modifiers */ int number;
	/* modifiers */ String test = "hello";
}

Тут в отличие от плюсов модификатор пишется у каждого поля. Поля инициализируются значениями по умолчанию. Для примитивных типов - нули, для бул - false, для ссылок - null. Можно и явно прописать инициализацию. 

Когда создается объект, память будет занулена, а потом уже что-то будет записываться.

class Example {
	int number;
	/* modifiers */ int getNumber() {
		return number;
	}
}

Возможна перегрузка методов (несколько одноименных с разными параметрами). (статический полиморфизм) 

Статический Полиморфизм: - это когда решение решить, какой метод выполнить, определяется во время компиляции. Примером этого может быть перегрузка метода.

Динамический Полиморфизм: - это когда решение выбрать, какой метод выполнить, устанавливается во время выполнения. Примером этого может быть переопределение метода.

class Example {
	int number;
	/* modifiers */ Example(int number) {
		this.number = number;
	}
}

Если не объявлен ни один конструктор, автоматически содаетчя конструктор по умолчанию (без параметров). В плюсах много конструторов по умолчанию, а в джаве один! 

В Java нет деструкторов, сбор сумора автоматический. Есть похожий метод finalize (будет вызван при удалении объекта), который можно перегружать с Object, но пользоваться им не рекомендуется. В тот момент, когда сборщик мусора запускается, находит объект, на который никто не ссылкается, он сначала запускает метод finalize, а потом уходит, он не ждет пока finalize закончит работу. Но, когда сборщик мусора придет к объекту второй раз, он его удалит, поэтому finalize не будет запущен дважды. Но мы также не знаем КОГДА будет запущен finalize, но GC может не прийти. Гарантированно запускать сборщик - не существует. Метод finalize - deprecated.

При необходимости освободить ресурсы заводят обычный метод void close() или void dispose() (поговорим о них позже).

Example e = null;
// e.getNumber() -> NullPointerException (исключительная ситуация)

e = new Example (3);
классы-обертки - boxing, строки - литералы, а все остальное - new.
// e.getNumber() -> 3

e.number = 10;
// e.getNumber() -> 10

- В Java не поддерживается множественное наследование. Почему так? Ромбовидное наследование, но что в нем плохого? Проблема метод - это не проблема, потому что код в джава не скомпилируется, если явно не прописать у какого класса вызывается этот метод (решается на уровне языка, чтобы явно указывать). Проблема с данными! Потому что у родилей есть одинаковые поля и не понятно у какого поля взять данные.
- В реальности в Java множественное наследование заменяется интерфейсами.
- Если не написать ключевое слово extends, то компилятор самостоятельно его напишет, потому все классы неявно наследуюся от Object.

class Derived extends Example {
	// перегрузка конструкторов
	Derived () {
		this(10); // вызов из конструктора другого конструктора
			  // такая команда должна быть первой
	}
	
	Derived (int number) {
		super(number); // вызов родительского конструктора 
	}
}

Ключевое слово this cсылается на другой конструктор в этом же классе. Если используется, то обращение должно к нему быть первой строкой конструктора;

Ключевое слово super вызывает конструктор родительского класса. Если используется, должно обращение к нему быть первой строкой конструктора;

Если конструктор не делает вызов конструктора super класса-предка (с аргументами или без аргументов), компилятор автоматически добавляет код вызова конструктора класса-предка без аргументов;

Родственник классов - интерфейс. Аналогом интерфейсов в плюсах класс с чисто вирутальными методами и без полей. Интерфейс определяет возмодные сообщения, но не их реализацию, а именно возвращаемое значение и сигнатуру. В отличии от классов в интерфейсе не пишутся модификаторы доступа, потому что любые методы, которые написаны в интерфейсе, автоматически имеют модификатор доступа - public.

interface Exampleinterface {
	int getNumber();
}  

Класс может реализовывать несколько интерфейсов
class Example implements ... , .. {
	int getNumber () {
		..
	}
}

abstrcat class Example {...} нельзя создать экземпляр класса
abstract int getNumber(); метод без реализации (класс должен быть абстрактным)

Если сказать аккуратно, то все методы в интерфейсе помимо public имеют модификтаор доступа abstract. Можно создать аналог интерфейса - абстрактный класс. Абстрактный класс - есть хотя бы один асбтрактный метод (в интерфейсе все методы абстрактные). Отличия абстрактного класса от интерфейса:

- множественное наследование от интерфейсов
- нет полей в интерфейсе
- в интерфейсе нет конструторов

Абстрактный класс — это класс, в объявлении которого есть ключевое слово abstract. Его отличие от обычного класса в том, что нельзя создать объект или экземпляр данного класса. Все остальное в абстрактном классе остается таким как и в обычном. У него есть методы. Только абстрактный класс может иметь абстрактные методы — у которых нет реализации, только объявление. Это означает, что абстрактный метод должен быть реализован в классе-наследнике.

Интерфейс это конструкция языка Java, в рамках которой принято описывать абстрактные публичные (abstract public) методы и статические константы (final static). С помощью интерфейса можно указать, что именно должен выполнять класс его реализующий, но не как это делать. Способ реализации выбирает сам класс. Интерфейсы не способны сохранять данные состояния.

Снова поговорим про Object. Метод clone позволяет сделат полную копию объекта. wait, notify, notifyAll (многопоточное программирование). Class<?> getClass() - взять описание класса.

(в java.lang.*)
иерархия: Integer и Double наследуются от Number
	  StringBuilder и StringBuffer (потоко безопасный - хорошо использовать в многопоточности) наследуются от AbstractStringBuilder.

АМ говорил, что интерфейсы - это сигнатуры методов, он врал в двух вещах. В интерфейсе можно написать переменную, но она автоматически получить модификтаоры доступа: public, static, final (константа публичная статическая). Интерфейсе хороший способ глобально хранить константы. 

В интерфейсе можно (начиная с Java 8) писать дефолтнеы реализации (нужно использовать ключевое слово default). Все методы получают модификаторы доступа public и abstract, очевидно, потому что есть default. С public есть проблемы с Java 9, в интерфейсах можно писать private методы (обсудим потом). Статические методы похожи на методы по умолчанию, за исключением того, что мы не можем переопределить их в классах, реализующих интерфейс. Этот функционал помогает нам избежать нежелательных результатов, которые могут появиться в дочерних классах.

```java
interface A {
  static int g() {
    return 1;
  }
}
  
public class Main implements A {
  public static void main(String[] args) {
    System.out.println(A.g());
  }
}
```

Модификаторы
- public - доступ для всх
- protected - доступ в пределах пакета и дочерних классов (в пределах всех классов-наследников нашего класса).
- private -  доступ в пределах класса
- по умолчанию (нет ключевого слова) - доступ в пределах пакета (package private). Дыра в безопасности, потому что любой может полезть в пакет и сказать, что он живет с нами в пакете. Поэтому по этой причине в среднем не рекомендуется быть package private, а всегда указывать модификатор доступа.

Могут использоваться (модификаторы) пред классами, методами и полями.

модификатор final
Можно писать у методов, полей и классов.
- класс нельзя наследовать (нельзя иметь наследников) (бизнес-логика; если много инвариантов у методов и лень писать final у каждого метода, то можно сделать final класс; некоторые классы стандартной библиотеки - final; например класс Integer - final - сломался функционал, который не можут быть описан языком Java; String - может быть переопределен +)
- метод нельзя переопределить в производных классах (методы связаны четко связаны между собой; ломается структура; что-то ломает инвариант; какой-то метод вызывается в конструкторе. он должен быть final, так как до вызова foo мы можем оперировать одними данными, когда следующие могут быть ещё не проинициализированны; бизнес-логика, чтобы программисты-дятлы не сломали что-то)
- поле явялется константным (константа во время компиляции; значение инициализируется в процессе работы, но которое нельзя изменить [аккуратнее со ссылками]).

```java
public class BlankFinal {
	private final int i = 0;		// константа во время компиляции (известно на этапе компиляции) (компилятор в основном хардкодит эти значения везде, где они используются)
	public static final int N = 10;		// константа компиляции
	private final int j;			// константа во время выполнения (должно быть задано во время инициализации)
	
	public BlankFinal(int x) {
		j = x;
	}
}
```

void f() {
	int i; // значение undefined-значение (перменная на стеке)
	i++; // поэтому это не скомпилируется
}

Обязательно инициализировать пременные при объявлении внетри методов! (до её использования)
Классе же все имеет дефолтное значение.

Инициализация полей:
class Test {
	int n = 3;
	int i = foo(n); // можно и так)
	int foo(int num) {
		return 11 * num;
	}
}

Помимо всего этого, конструкторов, для инициализации полей по умолчанию есть секции: обычные и статические. Обычная секция вызывается перед конструктором (когда хотим создать несколько конструкторов, но их общую функциональность хотим вынести).

В Java ленивым образом (не сразу) подгружаются классы. Когда мы запускам программу (класс с методом main), вместе с ним стандартная библиотека. Если при чтении байт-кода обнаружился ещё один класс, то она его начнет искать, загружать. Если не найдет - ошибка.

Статическая секция иницализации - некоторый кусочек кода, который будет выполнятся один раз, где-то близко когда класс загрузят в память. Аналагично со статичекими полями. В каком порядке все работает?  

```java
public class StaticTest {
	static int i;
	int j, h;
	
	static {
		i = 25;
		System.out.println("1");
	}
	
	{
		j = 8;
		h = 3;
		System.out.println("2");
	}
	
	public static void main(String[] args) {
		System.out.println("3");
		StaticTest t = new StaticTest();
	}
}
```

Статическая инициализация будет отложена максимально возможно. Если мы обращаем к переменной времени компиляции, то на статическую секуцию все равно. СТатическая секция стартанет только в том случае, если мы обратимся к потенциальной статической переменной (времени выполнения).

public static final int N = 10; // не запустит статическую секцию
public static final x = foo(); // запустит её

Ислючение
- Исключительная ситуация (произошло что-то плохое)
- Генерирующийся объект

Исключение - событие, возникающие в процессе работы программв и прерывающее её нормальное исполнение

java.lang.NullPointerException
java.lang.ArrayIndexOutOfDoundsException
java.lang.ClassCastException
java.lang.ArithmeticException
java.lang.OutOfMemoryError
java.io.IOException

 Причины ошибок:
 - Ошибки программировния - непроверяемые исключения (программист дурак) (nNullPointerException)
 - Неверное использование API - непроверяемые (чаще) или проверяемые исключения (InvalidArgumentException)
 - Доступ к внешним ресурсам - проверяемые исключения (IOExecption)
 - Системные сбои (VirtualMachineError)
 
 проверяемые ошибки - те на которые можно разумно отреагировать
 непроверяемые - виноват программист
 
 Иерархия исключений:
 
 Throwable, обычно что-то типа *able называется интерфейс, а тут это главный класс.
 
 		    -----------Throwable------------------
 		Exception (программа виновата)		Error (виновата JVM)
 	   -------------------				|
    RuntimeEcxeption	IOException 		  VirtualMachine Error
   	  ^	(все остальные проверяемые)
   	  |
    не проверяемые
 	
java.lang.Throwable

Исключение в Java - полноценный объект
Все искобчения в Java наследуются от класса Thowable

String getMessage() - сообщение об ошибке
Throwable getCause() - причина исключения
StackTraceElement[] getStackTrace() -  
void printStackTrace() - печать стека исполнения

- либо генерируется используемым кодом
- либо генерируем сами

Как с этим все работать? Хотим написать метод, в результате, которого может сгенирироваться какая-то исключительная ситуация. Если произошло что-то плохое, то моэно создать объект нужного исклчения и бросить его (throw). В качестве конструктора берется текст сообщения. thow - генирирует исключительную ситуацию.

```java
public static int parseInt(String s, int radix) throws NumberFormatException {
	if (s == null) {
		throw new NumberFormatException("null");
	}
	
	// ...
}
```

При этом есть два варианта, можно разобраться с исключительной ситуацией в методе. Либо же если нужно кинуть её выше по стеку, то в названии функции нужно написать какие иключения генерирует метод (throws ..., ..) - лучше писать наболее частный тип, а не какой-нибуль Throwable, чтобы точно показать какая ошибка.

При вызове методаа, который бросает проверяемое исключение необходимо
- Либо обработать его (перехватить)
- Либо пробросить дальше *написать throws .. у текущего метода)

```java
public void foo() throws IOException { 
	...
}

public void bar() throws IOException { // проброс исключения
	foo();
}
```

- Оператор throw прерывает нормальное исполнение программы и запускает поиск обраблтчика исключения
- Если исключение проверяемое, метод должен соедержать его в списке throws

Как же обработать исключение? Не всегда же нам его пробрасывать. С помощью конструкции try-catch.
 
```java
System.out.println("Please enter number: ");
int n = 0;
while (true) {
	String s = readUserInput();
	try {
		n = Integer.parseInt(s);
		break;
	} catch (NumberFormatException e) {
		System.out.println("Bad number, try again: ");
	}
}

// если бы мы тут обработали не все исключния, но нужно было остаток записать во throws другой метода
```

При исключении программа сразу начинает бежать по стеку и искать первый try, в котором он ищет соответствующий catch. Если он есть, то супер, иначе ищем следующий try. Пока не найдем обрадотчик или не дойдем до дна стека.

Тип ошибки e - это lca то что написано и что передается. По синтаксису: можно писать много catch, но с Java 7 добавили возможность писать оишбки `IOException | NumberFromatException e`.

Если в коде вызываются методы, бросающие проверяемые исключения, эти исключения надо либо поймать и обработать (catch), либо добавиьб в список thorws.

Стратегии обработк:
- Игнорирование (пустой catch) - ПЛОХО (если исключительная ситуация и ничего не делать - это странно)
- Запись в лог - ТОЖЕ ПЛОХО (ide может написать в catch секции printStackTrace - это side эффект, плохо. Если мы пишем библиотеку и пользователь будет читать все это полотно, то будет неприятно. Если мы не знаем как это обработать, то нужно передавать дальше. Может кто-то обработает, где это логично.)
- Проброс дальше тоже или нового исключения
- Содержательная обработка (например, повтор операции)

Побо́чные эффе́кты (англ. side effects) — любые действия работающей программы, изменяющие среду выполнения.

На этом ничего не заканчивается. Есть ещё одна проблема. Пусть у нас есть код, который должен выполнятся не зависимо от того, что выпало исключение или нет. Работа с ресурсами - отличный пример.

```java
InputStream is = new FileInputStream("a.txt");
try {
	readFromInputStream(is); // как бы мы не поработали с файлом мы должны закрыть его.
} finally { // блок выполнен в любом слкчае, в нем обычно особождают использованные ресурсы
	is.close()
}
```

Проскакивая try и пытаясь найти свой catch по стеку, мы всегда будем заваливаться в finally. Но есть некоторая проблема, нужно сделаь все поаккуратнее. Ведь файлп может и не быть, во время чтения мышь перегрызет провод и все сломается, при закрытии файла мышь может скушать провод снова. Если засунуть все в try, то `is` не будет видна в finally. Поэтому нужно is вынести за try. Можно закрывать файл, когда он не открылся). Для этого есть try with resuorses.

- try with resources добавлен в Java 7
- метод close() будет вызван автоматически, как в finally
- можно перечислить несколько ресурсов через ;
- ресурсы должны реализовать интерфейс java.lang.AutoCloseable

Суть в том, что команде try в качесиве паметра говорим какую переменную нужно создать. Если она создалась, то запускаем код внутри секции. Try with resources сам сделит, чтобы все зарыть, но есть нюанс. 

Рассмотрим try-catch с открытием файла, где и в finally try-catch (самый первый, который АМ демонстрирует). Если файл не открылся, то эта жже ошибка вылазит наружу. Если файл открылся, нормально поработал и не закрылся, то эта ошибка вылезет. Если открыти, сломались при чтении и норм закрылись - тоже ОК. Самое плохое, когда открыти, не считали и не закрылись, так как мы перебьм первое исключение. Давайте с этим поборемся. Именно это и реализовано в try with resources.

В итоге просто записываем исключения в getSupressed, то есть добавляем в "подавленые" исключения те, которые велетели после основного.

Ресурсов может быть несколько. В обратном порядке (относительн открытию) они закрываются. 

Итого:
- ошибки обрабатываются там, где для этого достаточно информации
- не стоит делать управление кода на исключениях, перебор цикла с выходом из массива. Упарвление на исключениях - долго. Мы оставлваемся, начинаем откатываться по стеку, проверки - долго..
- не игнорируем
- записывать в лог
- перехват базовых исключений
```java
try {

} catch (Exception e) { // все исключения будут залетать сюда..
	// что-то полезное
}
```
- Для своиз исключений наследуемся от кого-нибудь (Exception) и перегружаем конструктор (в проверяемые и в не проверяемые)
```java
public class BadMoveException extends Exception {
	public BadMoveException(String message) {
		super(message);
	}
}
```


TODO: как работает getSupperesed()
TODO: рассахаривание try-with-resources

интерфейс:
у интерфейса нет состояния
у интерфейсов есть множественная реализация
конструктора нет
нет реализации (в старых реализаций)

если есть подавленные исключения, то выдать ещё ответ e.getSuppesed().length()

на доске писали

первая лекция
автоматиченские памятью
песочница
кросс-платформеннсть
jit-компиляция

кеширование строковых литералов, кеширование Integer (можно настроить, обычно -128 до 127). если явно писать new, то она не кешируется. кешируется - ссылка на уже созданный объект, для не кеширования вызывать явный new. (отклбчить кеширование)

 4 
 3 - так как константа врени компиляции (не может быть иземенено в результате статической инициализации)
 5
 1
 3 - проходит статическая инициализация, так как x - не константа времени компиляции
 6
 6 - так как вызываем  создаение экземпляра, поэтому статическая инициализация
 2 - родительский конструктор
 3 - родительский конструктор
 5 - Test02 конструктор
 
