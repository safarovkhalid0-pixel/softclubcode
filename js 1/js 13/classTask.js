console.log(`\nTask 1`);
let fruits = ["apple", "banana"]
let d = fruits.push("orange")
console.log(fruits);

console.log(`\nTask 2`);
let fruits2 = ["apple", "banana", "orange"]
let f = fruits2.pop()
console.log(fruits2);



console.log(`\nTask 3`);
let fruits3 = ["banana", "orange"]
let d3 = fruits3.unshift("apple")
console.log(fruits3);



console.log(`\nTask 4`);
let fruits4 = ["apple", "banana", "orange"]
let d4 = fruits4.shift()
console.log(fruits4);


console.log(`\nTask 5`);
let fruits5 = ["apple", "banana", "orange"]
console.log(fruits5.includes("banana"));

console.log(`\nTask 6`);
let fruits6 = ["apple", "banana", "orange"]
console.log(fruits6.indexOf("orange"));

console.log(`\nTask 7`);
let fruits7 = ["apple", "banana", "orange"]
console.log(fruits7.join(" - "));


console.log(`\nTask 8`);
let fruits8 = ["apple", "banana", "orange"]
console.log(fruits8.slice(1, 3));


console.log(`\nTask 9`);
let fruits9 = ["apple", "banana", "orange", 'kiwi']
fruits9.splice(1, 1)
console.log(fruits9);


console.log(`\nTask 10`);
let fruits10 = ["apple", , "orange", ]
fruits10.splice(1, 0, "banana")
console.log(fruits10);


console.log(`\nTask 11`);
let fruits11 = ["apple", "banana", "orange"]
fruits11.forEach(function(fruit) {
    console.log(fruit);
});



console.log(`\nTask 12`);
let numbers = [1, 2, 3, 4, 5];
let res = numbers.map(element => element * 2);
console.log(res);




console.log(`\nTask 13`);
let numbers2 = [3, 8, 12,  5, 20, 7];
let res2 = numbers2.filter(element => element > 10);
console.log(res2);


console.log(`\nTask 14`);
let numbers3 = [5, 12,  8, 20, 3];
let res3 = numbers3.find(element => element > 10);
console.log(res3);


console.log(`\nTask 15`);
let numbers4 = [5, 12,  8, 20, 3];
let res4 = numbers4.findIndex(element => element > 10);
console.log(res4);


console.log(`\nTask 16`);
let numbers5 = [3, 5, 7,  8, 11];
let res5 = numbers5.some(element => element % 2 === 0);
console.log(res5);


console.log(`\nTask 17`);
let numbers6 = [2, 4, 6,  8, 10];
let res6 = numbers6.every(element => element % 2 === 0);
console.log(res6);


console.log(`\nTask 18`);
let numbers7 = [10, 20, 30, 40];
let res7 = numbers7.reduce((total, element) => total + element, 0);
console.log(res7);





console.log(`\nTask 19`);
let numbers9 = [10, 2, 5, 1, 20];
numbers9.sort((a, b) => a - b);
console.log(numbers9);



console.log(`\nTask 20`);
let fruits12 = ["apple", "banana", "orange", "kiwi"];
fruits12.reverse()
console.log(fruits12);



console.log(`\nTask 21`);
let numbers10 = [5, 15, 8, 20, 12];
console.log(numbers10.findLast(element => element > 10));



console.log(`\nTask 22`);
let numbers11 = [5, 15, 8, 20, 12];
console.log(numbers11.findLastIndex(element => element > 10));


console.log(`\nTask 23`);
let numbers12 = [1, [2, 3], [4, 5]];
console.log(numbers12.flat());




console.log(`\nTask 24`);
let numbers13 = [1, 2, 3];
console.log(numbers13.flatMap(element => element * 2));



console.log(`\nTask 25`);
let fruits14 = ["apple", "banana", "orange"];
console.log(Object.keys(fruits14)); 



console.log(`\nTask 26`);
let fruits15 = ["apple", "banana", "orange"];
console.log(Object.values(fruits15)); 




console.log(`\nTask 27`);
let fruits16 = ["apple", "banana", "orange"];
console.log(Object.entries(fruits16)); 



console.log(`\nTask 28`);
let numbers1 = [3, 8, 12, 5, 20, 7, 10];
let cnt = numbers1.filter(element => element > 10);
console.log(cnt.map(element => element * 2));



console.log(`\nTask 29`);
let students = ["Ali", "Madina", "Rustam", "Zarina"];
let v = students.includes("Madina");
if(v){
    console.log(students.indexOf("Madina"));
}
else{
    console.log("Madina не найдена");
}



console.log(`\nTask 30`);
let numbers14 = [10, 5, 20, 15, 30];

let sum = numbers14.filter(num => num > 10).reduce((total, num) => total + num, 0);

console.log(sum);