console.log(`\nTask 1`);
let age = 10;
if (age <= 7) console.log("Дошкольник");
else if (age <= 13) console.log("Ребёнок");
else if (age <= 18) console.log("Подросток");
else console.log("Взрослый");

console.log(`\nTask 2`);
let score = 85;
if (score >= 90) console.log("A");
else if (score >= 75) console.log("B");
else if (score >= 60) console.log("C");
else if (score >= 50) console.log("D");
else console.log("F");

console.log(`\nTask 3`);
let temperature = 30;
if (temperature > 35) console.log("Очень жарко");
else if (temperature > 25) console.log("Жарко");
else if (temperature > 15) console.log("Тепло");
else if (temperature > 5) console.log("Прохладно");
else console.log("Холодно");

console.log(`\nTask 4`);
let number = 16;
let sqrt = Math.sqrt(number);
let isnt = Number.isInteger(sqrt);
if (isnt == true) {
  console.log("Идеальный квадрат");
} else if (isnt) console.log("Не идеальный квадрат");


console.log('\nTask 5');
let a1 = 2;
let b1 = 1;
let c1 = 115;
mx = 0;
mn = 0;

if ((a1 > b1) & (a1 > c1)) {
    if ((c1 < b1) & (c1 < a1)) {
        console.log("max: " + a1);
        console.log("min: " + c1);
    } else if ((b1 < c1) & (b1 < a1)) {
        console.log("max: " + a1);
        console.log("min: " + b1);
    }
} else if ((b1 > a1) & (b1 > c1)) {
    if ((c1 < b1) & (c1 < a1)) {
        console.log("max: " + b1);
        console.log("min: " + c1);
    } else if ((a1 < c1) & (a1 < b1)) {
        console.log("max: " + b1);
        console.log("min: " + a1);
    }
} else if ((c1 > a1) & (c1 > b1)) {
    if ((a1 < b1) & (a1 < c1)) {
        console.log("max: " + c1);
        console.log("min: " + a1);
    } else if ((b1 < c1) & (b1 < a1)) {
        console.log("max: " + c1);
        console.log("min: " + b1);
    }
}


console.log('\nTask 6');
let number2 = 25
number2 = Math.sqrt(number2) 
console.log(Number.isInteger(number2));


console.log('\nTask 7');
let base = 3
let exponent = 4
let number4 = Math.pow(base,exponent) 
console.log(number4);

console.log('\nTask 8');
let number22 = 4;
if (number22 % 2 !== 0) {
  console.log("Простое");
} 
else {
  console.log("Составное");
}



console.log('\nTask 9');
let a =  12
let b = 8
let c = 15
mx = 0;
mn = 0;

if ((a > b) & (a > c)) {
    if ((c < b) & (c1 < a)) {
        console.log("max: " + a);
        
    } else if ((b < c) & (b < a)) {
        console.log("max: " + a);
       
    }
} else if ((b > a) & (b > c)) {
    if ((c < b) & (c < a)) {
        console.log("max: " + b);
        
    } else if ((a < c) & (a < b)) {
        console.log("max: " + b);
        
    }
} else if ((c > a) & (c > b)) {
    if ((a < b) & (a < c)) {
        console.log("max: " + c);
    } else if ((b < c) & (b < a)) {
        console.log("max: " + c);
    
    }
}


console.log(`\nTask 10`);
let number3 = 2;

if (Math.pow(2, 1) === number3) {
  console.log("Степень двойки");
} else {
  console.log("Не степень двойки");
}


console.log(`\nTask 11`);
let number5 = -5

if (number5>0){
    console.log("положительное");
    
}

else if (number5<0){
    console.log("отрицательное");
    
}
else {
    console.log("ноль");
    
}



console.log(`\nTask 12`);
let year = 2024
if (year % 4 == 0 * year % 100 != 0) console.log("Високосный");
else console.log("Не високосный");


console.log(`\nTask 13`);
let x1 = 2
let y1 = 3
let x2 = 5
let y2 = 7
let distance = Math.sqrt(
    Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2)
)
console.log("Расстояние: " + distance);


console.log(`\nTask 14`);
let number6 = 3.7
console.log(`Math.floor: ${Math.floor(number6)}`);
console.log(`Math.ceil: ${Math.ceil(number6)}`);
console.log(`Math.round: ${Math.round(number6)}`);



console.log(`\nTask 15`);
let age5 = 25
if (age5>0 & age5<=12)console.log("Ребёнок");
else if (age5>=13 & age5<=19)console.log("Подросток");
if (age5>=20 & age5<=59)console.log("Взрослый");
if (age5>=60)console.log("Пожилой");


console.log(`\nTask 16`);
let height = 170
if (height>180)console.log("Очень высокий");
else if (height>160)console.log("Высокий");
else if (height>150)console.log("Средний");
else console.log("Низкий");


console.log(`\nTask 17`);
let a3 = 15
let b3 = 15
if ( a3==b3)console.log("Равны");
else console.log("Не равны");


console.log(`\nTask 18`);
let number8 = 0;
let result = false;

if (number8 % 2 === 0) {
  if (number8 > 0) {
    result = true;
  }
}

console.log("Чётное и положительное: " + result);



console.log(`\nTask 19`);
let number1 = 12
if (number%2==0 & number%3==0)console.log("Ба 2 ва 3 тақсим мешавад");
else console.log("Тақсим намешавад");



console.log(`\nTask 20`);
let length = 10
let width = 5
aaa = 2*(length+width)
aaaa = (length*width)
aq = aaaa>100
aqq = aaaa>aaa
console.log(`Площадь: ${aaaa}`);
console.log(`Периметр: ${aaa}`);
console.log(`Площадь > Периметр: ${aq}`);
