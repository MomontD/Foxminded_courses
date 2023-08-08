
//
// document.addEventListener("DOMContentLoaded", function() {
//
//     // Отримати значення order з шаблону layout. В body ми вказуємо data-order="{{ order }}"
//     // Тим самим ми через клас data-order передаємо в js значення order
//     let order = document.querySelector('body').getAttribute('data-order');;
//     // Перетворюємо order на булівське значення
//     order = order === "True"
//
//     // Отримати всі елементи, які мають клас "chaild_conteiner_report_racer_data"
//     let racersList = document.querySelectorAll(".racer_nik_name");
//
//     // Змінити номер racer у кожному блоку відповідно до значення desc
//     for ( let num=0; num < racersList.length; num++ ) {
//
//         let racer = racersList[num];
//
//         let racerNumber = order ? racersList.length - num : num + 1;
//
//         racer.textContent = `${racerNumber}. ${racer.textContent}`;
//
//     }
// });

