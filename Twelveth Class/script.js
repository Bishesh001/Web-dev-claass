// take the actual date and alert message "Today is dayName" using switch statement

const dateInput = document.getElementById('date');
const displayDateBtn = document.getElementById('display-date');
// console.log(new Date());
// Get the day number (0 = Sunday, 6 = Saturday)
function alertDay() {
    const today = new Date(dateInput.value);
    const dayNumber = today.getDay();
    let dayName;
    // Determine the day name using switch
    switch (dayNumber) {
        case 0:
            dayName = "Sunday";
            break;
        case 1:
            dayName = "Monday";
            break;
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        case 6:
            dayName = "Saturday";
            break;
        default:
            dayName = "Unknown"; 
    }
    return dayName;
}
// trigger when user clicks on the button
displayDateBtn.addEventListener('click',()=>{
    alert("Today is "+alertDay())
});