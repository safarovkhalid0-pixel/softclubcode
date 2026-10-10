console.log(`\nTask 21`);
let number = 49
a2 = Math.sqrt(number)
console.log(Number.isInteger(number));

console.log(`\nTask 22`);
let number1 = 8
a2 = Math.pow(number1)
if (a2 == number1**3)console.log("степень тройки");
else console.log("Не степень тройки");


console.log(`\nTask 23`);
let number6 = 3.2
console.log(`Math.floor: ${Math.floor(number6)}`);
console.log(`Math.ceil: ${Math.ceil(number6)}`);
console.log(`Math.round: ${Math.round(number6)}`);

console.log(`\nTask 24`);
let a = 10
let b = 25
let c = 15
console.log(`Math.max: ${Math.max(a,b,c)}`);
console.log(`Math.min: ${Math.min(a,b,c)}`);


console.log(`\nTask 25`);
let number2 = 6;
if (number2 % 2 === 0 && number2 !== 2) {
  console.log("Составное");
} else {
  console.log("Простое");
}



console.log(`\nTask 26`);
let number8 = 4
let result = false

if (number8 % 2 === 0 & number8%4==0){
    
 console.log("Чётное и делится на 4")
}
else console.log("Чётное и ne делится на 4");
