
const listButtons = document.querySelectorAll('.buy')
// 
const listButtonsEditTitle = document.querySelectorAll('.edit-title')
const listTitles = document.querySelectorAll(".title")
// 
const listButtonsEditPrice = document.querySelectorAll('.edit-price')
const listPrices = document.querySelectorAll(".cost-original")
// 
const listButtonsEditDiscount = document.querySelectorAll('.edit-discount')
const listDiscounts = document.querySelectorAll(".discount")
// 
const listTotalPrice = document.querySelectorAll(".total-cost")
for (let count = 0; count < listButtonsEditTitle.length; count++) {
    let button = listButtonsEditTitle[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            listTitles[count].textContent = prompt("Укажіть нову назву для товару")
        }
    )
}

for (let count = 0; count < listButtonsEditPrice.length; count++) {
    let button = listButtonsEditPrice[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            listPrices[count].textContent = prompt("Укажіть нову ціну для товару") + ' грн'
        }
    )
}

for (let count = 0; count < listButtonsEditDiscount.length; count++) {
    let button = listButtonsEditDiscount[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            listDiscounts[count].textContent = "Знижка " + prompt("Укажіть нову знижку для товару") + "%"
        }
    )
}

// for (let count = 0; count < listTotalPrice.length; count++) {
//     let pTotalPrice = listDiscounts[count]
//     let p1 = listPrices[count]
//     let new_text_total_price = pTotalPrice.textContent.split(" ")[1].split("%")[0]
//     // alert(new_text_total_price)
//     let new_text_total_price1 = p1.textContent.split(" грн")[0]
//     new_text_total_price1 = new_text_total_price1.split(" ")
//     let new_text = `${new_text_total_price1[0]}${new_text_total_price1[1]}`
//     let new_text1 = Number(new_text)
//     let new_cost = new_text1 / 100 * new_text_total_price 
//     // alert(Number(new_cost))
//     let new_total_cost = new_text - new_cost + " грн"
//     // alert(new_total_cost)
//     let p_Total_price_text = listTotalPrice[count]
//     p_Total_price_text.textContent = new_total_cost
// }

for (let count = 0; count < listButtons.length; count++) {
    let button = listButtons[count]
    button.addEventListener(
        type = 'click',
        listener = function (event) {
            if (document.cookie == ''){
                document.cookie = `products = ${button.id}; path = / `
            }
            else{
                product_id = document.cookie.split('=')[1]
            }
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