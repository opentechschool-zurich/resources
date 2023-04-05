// find palindromic dates in the future in the format dd.mm.yyyy
// 10.10.0101 -> ̈́'10100101'
// 10100101

function isADate(date) {
  let day = parseInt(date.slice(0, 2));
  let month = parseInt(date.slice(2, 4));
  let year = parseInt(date.slice(4, 8));
  if (month > 12) {
    return false;
  }
  if ([11, 4, 6, 9].includes(month)) {
    return day <= 30;
  }
  if (month == 2) {
    return day <= 29;
  }
  return day <= 31;
  // console.log(day, month);
}

// 2023 -> 32.02.2023
for (let i = 2023; i < 10000; i++) { // year
  let candiDate = i.toString();
  candiDate = candiDate.split('').reverse().join('') + candiDate;
  // console.log(candiDate);
  if (!isADate(candiDate)) {
    continue;
  }

  console.log(candiDate);
}

// 04.04.2023 -> 05.04.2023
// 30.04.2023 -> 01.05.2023
// 31.12.2023 -> 01.01.2024
function addOneDay(date) {
  return date;
}

// date = '04.04.2023';
// while (date < '31.12.9999') {
//   date = addOneDay(date);
// }
