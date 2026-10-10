console.log(`\nTask 1`);
let age = 16
if( age >= 18 ) console.log("Метавонад овоз диҳад");
else console.log("Наметавонад овоз диҳад");

console.log(`\nTask 2`);
for(let i = 1 ;i<=10;i++){
    console.log(i);
    
}

console.log(`\nTask 3`);
let i1 = 5
while(i1>=1){
    console.log(i1);
    i1--;
}

console.log(`\nTask 4`);
let cnt = 0
for(let i = 1;i<=20;i++){
    if(i % 2 === 0){
        cnt+=i;
    }
}
console.log("Сумма чётных: "+cnt);


console.log(`\nTask 5`);
let x = 15
let y = 20
let z = 12
let mx = Math.max(x, y, z)
let mn = Math.min(x, y, z)
console.log("Самое большое: "+mx);
console.log("Самое маленькое: "+mn);


console.log(`\nTask 6`);
let number = 16
let sq = Math.sqrt(number)
let is = Number.isInteger(sq)
console.log(is==true ? "Идеальный квадрат":"Не идеальный квадрат");


console.log(`\nTask 7`);
for(let i = 1;i<=30;i++){
    if(i%3==0){
        console.log(i);
        
    }
}

console.log(`\nTask 8`);
let num = 17
let isprime = true
for(let i = 2;i<num;i++){
    if(num%i==0){
        isprime = false;
    }
}
if(isprime){
    console.log("Простое");
}
else{
    console.log("Составное");
}

console.log(`\nTask 9`);
for(let i = 1;i<=20;i++){
    let a = ''
    let b = ''
    let c = ''
    if(i%2==0){
        a = 'четное'
    }
    else{
        a = 'нечетное'
    }
    if(i%5==0){
        c = "делится на 5"
    }
    else{
        c = "не делится на 5"
    }
    if(i%3==0){
        b = "делится на 3"
    }
    else{
        b = "не делится на 3"
    }
    console.log(`${i} - ${a}, ${b}, ${c}`);
}


console.log(`\nTask 10`);
for(let i = 1;i<=30;i++){
    
    if(i%3==0 && i%5==0){
        console.log("FizzBuzz");
    }
    else if(i%5==0){
        console.log("Buzz");
    }
    else if(i%3==0){
        console.log("Fizz");
    }
    else{
        console.log(i);
    }
}