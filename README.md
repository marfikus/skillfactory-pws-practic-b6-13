
## Моё решение домашнего задания из модуля B6.13 (веб-сервер)

[albums_server.py](https://github.com/marfikus/skillfactory-pws-practic-b6-13/blob/master/albums_server.py) - собственно сервер, запускается в консоли. Для его функционирования необходимо установить модули *bottle* и *sqlalchemy*.

[albums.py](https://github.com/marfikus/skillfactory-pws-practic-b6-13/blob/master/albums.py) - модуль с методами для работы с базой данных albums.sqlite3. В соответствии с ТЗ позволяет выполнять поиск в базе, проверку на существование записи, проверку ввода и добавление новых записей.

[albums.html](https://github.com/marfikus/skillfactory-pws-practic-b6-13/blob/master/albums.html) - форма для поиска и добавления новых записей. По заданию не требуется, сделал так, для практики)

Соответственно запросы к серверу можно выполнять как через форму, так и из консоли, предварительно установив модуль *httpie* (или как-то аналогично).

Пример GET-запроса (поиск по исполнителю):  
`http http://localhost:8080/albums/"Linkin Park"`

Пример POST-запроса (добавление нового альбома в базу):  
`http -f POST http://localhost:8080/albums artist="Scorpions" genre="Rock" album="Blackout" year=1982`
