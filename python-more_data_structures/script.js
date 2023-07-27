"use strict";
function calAge1(birthYear) {
  return 2037 - birthYear;
}

const calAge2 = function (birthYear) {
  return 2037 - birthYear;
};

const calAge3 = (birthYear) => 2037 - birthYear;

console.log(`Age calculated by declaration function is ${calAge1(2000)}`);
console.log(`Age calcualted by expression function is ${calAge2(2000)}`);
console.log("Age calcualted by arrow function is ", calAge3(2000));

function checkDriver(age, haveLicense) {
  if (age > 17 && haveLicense) {
    return `You can drive a car`;
  } else if (age > 17 && !haveLicense) {
    return `Even if your age ${age} is greater than 18 you must have driver license`;
  } else if (haveLicense && age < 18) {
    return `Even if you have driver license your age must be grater than 18`;
  } else {
    return `Your age ${age} is less than the age limit 18 and also you do not have driver license`;
  }
}
console.log(`Dear customer :  ${checkDriver(23, false)}`);
console.log(`Dear customer :  ${checkDriver(16, true)}`);
console.log(`Dear customer :  ${checkDriver(13, false)}`);
console.log(`Dear customer :  ${checkDriver(23, true)}`);
