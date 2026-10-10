// 1
let sumEN = [1,2,3,4,5,6]
let darozi = sumEN.length
let summ = 0
function sum(){
    for(let i = 0 ; i<darozi;i++){
        if(sumEN[i]%2==0){
            summ+=sumEN[i]
        }
        else{
            continue
        }
    }
    return summ
}
console.log(sum());


// 1
function greetUser(name) {
  return `Hello, ${name}!`;
}

console.log(greetUser("ali"));


// 2
function isEven(num) {
  return num % 2 === 0;
}
console.log(isEven(8));


// 3
function getFullName(name2, surname) {
  return `${name2} ${surname}`;
}
console.log(getFullName("Muhammad", "ALi")); 


// 4
function countPositives(numbers) {
  let count = 0;
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > 0) {
      count++;
    }
  }
  return count;
}
console.log(countPositives([1, -2, 3, -4, 5]));

// 5
function findLongestWord(Words) {
  let longest = "";
  for (let i = 0; i < Words.length; i++) {
    if (Words[i].length > longest.length) {
      longest = Words[i];
    }
  }
  return longest;
}
console.log(findLongestWord(["cat", "elephant", "dog","school"]));

// 6
function calculateTotal(numbers2) {
  let total = 0;
  for (let i = 0; i < numbers2.length; i++) {
    if(numbers2[i]>0){
        total += numbers2[i];
    }
  }
  return total;
}
console.log(calculateTotal([10, -5, 7, -2, 8]));

// 7
function getAdults(users) {
  return users.filter(user => user.age >= 18);
}
console.log(getAdults([
  { name: "ali", age: 17 },
  { name: "sara", age: 20 },
  { name: "olim", age: 18 }
]));

// 8
function countVowels(text) {
  const vowels = "aeiouAEIOU";
  let count = 0;
  for (let i = 0; i < text.length; i++) {
    if (vowels.includes(text[i])) {
      count++;
    }
  }
  return count;
}
console.log(countVowels("JavaScript"));

