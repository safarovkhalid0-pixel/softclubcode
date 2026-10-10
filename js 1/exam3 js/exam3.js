// task 1
console.log(`\nTask 1`);
let fruits = ["яблоко", "банан", "манго",]
let darozi = fruits.length-1
console.log(fruits[0]);
console.log(fruits[darozi]);

// Task 2
console.log(`\nTask 2`);
let numbers = [10, 20, 30, 40, 50]
let cnt = 0
for(let i = 0 ; i<numbers.length;i++){
    cnt++
}
console.log(cnt);



console.log(`\nTask 3`);
let numbers2 = [10, 20, 30]
let k = numbers2.push(40)
console.log(numbers2);


console.log(`\nTask 4`);
let fruits2 = ["яблоко", "банан", "манго", "киви"]
let s = fruits2.pop()
console.log(fruits2);


console.log(`\nTask 5`);
let fruits3 = ["яблоко", "банан", "манго"]
let s2 = fruits3.includes("банан")
if(s2){
    console.log("Банан есть!");
}
else{
    console.log("Банана нет");
    
}


console.log(`\nTask 6`);
let numbers3 = [10, 20, 30, 40, 50]
let s3 = numbers3.indexOf(30)
console.log(s3);




console.log(`\nTask 7`);
let friends = ["Али", "Самир", "Фарангис"]
friends.forEach(function(element){
    console.log("Привет, "+element);
})


console.log(`\nTask 8`);
let numbers4 = [5, 12, 8, 20, 3]
let cnt2 = numbers4[0]
numbers4.forEach(function(element){
   if(cnt2 <= element){
    cnt2 = element
   }
   
})
console.log("Максимум: "+cnt2);



console.log(`\nTask 9`);
let numbers5 = [1, 2, 3, 4, 5, 6]
let summ = 0
numbers5.forEach(function(ele){
    if(ele%2==0){
        summ+=ele
    }
})
console.log("Сумма чётных: "+summ);


console.log(`\nTask 10`);
let numbers6 = [12, 5, 8, 20, 3, 15, 7]
let sum = 0
let average = numbers6.length
let mx = 0
let mn = numbers6[0]
let chotni = 0 
let nichotni = 0 
numbers6.forEach(function(a){
    sum+=a
    if(mx <= a){
        mx = a
    }
    if(mn>=a){
        mn = a
    }
    if(a%2==0){
        chotni++
    }
    if(a%2!=0){
        nichotni++
    }
})
console.log(sum);
console.log(sum/average);
console.log(mx);
console.log(mn);
console.log(chotni);
console.log(nichotni);