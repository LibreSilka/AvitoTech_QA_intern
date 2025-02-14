# AvitoTech_QA-trainee

Здравствуйте! Меня зовут Никита!<br> 
Ниже описание структуры тестового задания и подготовка окружение для запуска автотестов.

### Структура проекта тестового задания
Файл [Task_1.md](./Task_1.md) является решением первого задания.  
К нему в директории [Task_1_screenshots](./Task_1_screenshots) хранятся скрины.  

Файл [TESTCASES.md](./TESTCASES.md) содержит тест-кейсы и краткий Use_Cases ко второму заданию.  
В файле [BUGS.md](./BUGS.md) составлены баг-репорты, выявленные в результате выполнения автотестов.  

Файлы с автотестами расположены в корневом каталоге. 

---

## Задание №1

В задании требуется перечислить баги со скриншота. Судя по низкому качеству фото, принято решение 
не сравнивать верску с продом, а также дополнительный функционал, присутствующий на текущей версии прода.
Подробнее можно ознакомиться в файле [Task_1.md](./Task_1.md)

---

## Задание №2

Задание выполнено в связке `Python + Pytest + Selenium`.  

В [тест-кейсах](./TESTCASES.md) проверяется работа критического функционала сервиса размещения объявлений
для десктопной версии.  


---

### Инструкция по запуску тестов
1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
    ```
    git clone https://github.com/LibreSilka/AvitoTech_QA_intern
    ```

2. Убедитесь, что на Вашем компьютере установлен Python. В командной строке/терминале выполните команду
    ```
    python -v
    ```  

    Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала.  
    >В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python


3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду
   ```
   cd /здесь укажите путь до директории с проектом
   ```


4. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду  
   ```
   pip install -r requirements.txt
   ```
   если она не выполняется, то попробуйте
   ```
   pip3 install -r requirements.txt
   ```
   

5. Запустите тесты, выполнив команду  
   ```
   pytest test_advertisements.py
   ```