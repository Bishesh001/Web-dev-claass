// from here add 3 in even number and 7 in odd numer

let num = [1, 2, 3, 4, 5];
let newNum = [];

for(let i = 0; i < num.length; i++) {
    if(num[i] % 2 === 0) {
        newNum.push(num[i] + 3);  // Even numbers
    } else {
        newNum.push(num[i] + 7);  // Odd numbers
    }
}

console.log(newNum);  // [8, 5, 10, 7, 12];