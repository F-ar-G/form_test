# form_test


📌 Описание

Этот проект представляет собой автоматизированный тест для проверки работы формы на сайте practice-automation.com. Тест выполняет следующие действия:
 Вводит данные в текстовые поля (Имя, Пароль, Email)
 Выбирает чекбоксы (Milk, Coffee)
 Отмечает радиокнопку (Yellow)
 Выбирает значение в выпадающем списке (Yes)
 Подсчитывает элементы списка и находит самый длинный
 Нажимает кнопку "Submit" и проверяет алерт с подтверждением

## 📌 Установка

1. Установите Python (если еще не установлен).
2. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/F-ar-G/form_test.git
   cd form_test
3. Установите зависимости:
   pip install -r requirements.txt
4. Убедитесь, что у вас установлен ChromeDriver и он совместим с вашей версией Chrome.

📌 Запуск тестов

Запуск всех тестов:
   pytest form_test/

Запуск с подробным логом:
   pytest -v


