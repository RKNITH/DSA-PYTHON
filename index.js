//Q:1  SUM OF ALL NATURAL NUMBER


// let n = 100;
// let sum = 0;

// for (let i = 0; i <= n; i++) {
//     sum += i;

// }
// console.log(sum)


// Q: 2 SUM OF DIGITS OF A NUMBER:


// let sum = 0;
// function digitSum(n) {
//     while (n > 0) {
//         sum += n % 10;
//         n = Math.floor(n / 10);
//     }
//     return sum

// }
// console.log(digitSum(1234))


// Q 3: NUMBER OF DIGIT IN A NUMBER

// let n = 1234;
// let b = String(n).length
// console.log(b)


// Q 4: CHECK PALINDROME

// function isPalindrome(n) {
//     let reverseStr = String(n).split('').reverse().join('')
//     return n == reverseStr;
// }
// console.log(isPalindrome(1212))

// Q 5: FIBONACCI SERIES

// function fibonacci(n) {
//     let fibo = [0, 1]

//     for (let i = 2; i <= n; i++) {
//         fibo.push(fibo[fibo.length - 1] + fibo[fibo.length - 2])
//     }
//     return fibo
// }

// console.log(fibonacci(10))

// Q 6: MISSING NUMBER IN THE [0, N]

// let a = [0, 2, 3];
// let n = Math.max(...a);

// let expectedSum = (n * (n + 1)) / 2;

// let actualSum = a.reduce((acc, curr) => acc + curr, 0);

// let missingNum = expectedSum - actualSum;
// console.log(missingNum)

// Q 7 : SORTING ARRAY

// let arr = [1, 3, 2, -7, 8, 5, 0, 4, 5]
// arr.sort()
// console.log(arr)

// Q 8: REVERSE ARRAY

// let a = [1, 3, 2, -7, 8, 5, 0, 4, 5]
// a.reverse()
// console.log(a)










