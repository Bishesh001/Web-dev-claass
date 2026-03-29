// // Arrays in JavaScript
// //  array manupulation
// let arr = [1, 2, 3, 4, 5];
// // push method
// arr.push(8,5,6);
// arr.splice(1,0,7);
// arr.unshift(0);
// // console.log(arr);
// // // adding two arrays
// let arr1 = [ "horse", "Mouse", "Laxmanbadar" ];
// let arr2 = [ "Kashyap", "Dibya", "Annoconda", "Bigd" ];
// let arr3 = arr1.concat(arr2);
// // console.log(arr3);
// let arr1 = [ "horse", "Mouse", "Laxmanbadar" ];
// arr1.forEach((aryy) => {
// console.log(aryy);
// });?
// // adding 5 to each element of the array
// let arr1 = [ 1,2,3,4,5 ];
// let num = arr1.forEach((aryy) => {
//     console.log(aryy + 5)}
// );

// //  Dom
// const boss = document.getElementById("boss");
// boss.innerHTML = "Laxmanbadar is the boss of all bosses";
// console.log (boss);

const boxes  = document.getElementsByClassName('box');
for (let i = 0; i < boxes.length; i++) {
if (i === 0) {
    boxes[i].innerHTML = "This is the first box";
}
}
console.log(boxes);









