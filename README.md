<h1>Лабораторна робота №1 </h1>
<h3>з дисципліни "Технології розробки серверного ПЗ</h3>
<br>

Інструкції для запуску проекту локально:

На компютері повинен бути інстальований Docker.
1. Зайти в папку проекту, де міститься файл docker-compose.yaml і запустити тут термінал
2. Прописати команду docker-compose up
3. У браузері запустити http://localhost:8080/ або http://127.0.0.1:8080/

Аби перевірити справність через postman, у проекті міститься файл For_Lab1.postman_collection1.json з колекціями 
<ul>
<li>CategoryCollection</li>
<li>UsersCollection</li>
<li>RecordCollection</li>

</ul>

Потрібно підключити environment "Production", щоб працювала змінна LokalURL