Примитивы синхронизации - что-то хитрое, более чем блокировка.
- Semaphore
Блокировка с множественным количеством разрешений. Пока не все разрешения будут забраны, то можно брать. Пример с парковкой, если место есть, то машину пускают, иначе машина блокируется до тех пор пока машина не уедет. Зачем такая штука нужна? (машина может просить два парковочных места) Когда у нас есть ограниченное количество ресурсов, распределяемое между потоками. У нас есть ограниченная память и мощные потоки, которые не поместяться все в память. Семафор занимается распределением ресурсов (дает доступ, лобо блокирует). Вырожденный пример с контролем количества потоков в мире ограниченного количества ядер, когда поток хочет новые потоки и просит их (разрешение) у семафора. 

Семафоры в Java:
Semaphore(n, fair?) - число разрешений и честность (получает тот, кто дольше всех ждет).
Методы:
acquire - получить разрешение
release - отдать разрешение
tryQuire
reducePermits(n) - уменьшить кол-во разрешений
drainPermits - забрать все разрешения

- Барьери 
Барьер - одноразовый и многоразовый (в джава многоразовый=циклический). В чем суть? Представим, что есть лошадки и они стали и побежали. На старт поставили барьер, пока все не добегут барьер не сломается. Циклический барьер - синхронизация действий (например в играх).

.await() - прибыли к баьеру
reset - возвращает барьер в исходное состояние
.isBroken() - 

- Защелки
Дверь с защелкой в n-сантиметров. Можно либо ждать, либо сдвинуть на единицу. Защелку можно превратить в Барьер (длина - nПотоков, двигаем на 1). Но защелка - это одноразовый барье, открыв не закроем. Потоки, которые двигают и жду - не обязательно одни и тоже. Зачем это нужно? (в игре набор сессии в количестве игроков) Инициализация, каждый поток, который проводит инициализацию, пусть в конце поток подвинет защелку. Progress bar например..

Fork/Join



