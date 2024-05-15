// Отримує всі елементи HTML (теги) з ім'ям класу ".buy"
const listButtons = document.querySelectorAll('.buy')
// Задаємо цикл що перебирає всі кнопки із списку listButtons
for (let count = 0; count < listButtons.length; count++) {
    // Беремо із списку кнопку і записуємо до змінної button
    let button = listButtons[count]
    // До кнопки додаємо функцію що перевіряє подію "click" по цій кнопці
    button.addEventListener(
        type = 'click', // подія click
        // функція як параметр що буде виконуватись коли користувач натисне на кнопку
        listener = function (event) {
            // Якщо записів до cookie раніше не проводились то даємо перший запис
            if (document.cookie == ''){
                // Ми створюємо файл cookie  з назвою products та додаємо динамічно значення натиснутої кнопки
                document.cookie = `products = ${button.id}; path = / `
            }
            else{
                // Отримуємо попередньо записані дані в cookie (products)
                product_id = document.cookie.split('=')[1]
                // перезаписуємо cookie додаючи значення нової натиснутої кнопки
                document.cookie = `products = ${product_id} ${button.id}; path = / `
            }
        }
    )
}