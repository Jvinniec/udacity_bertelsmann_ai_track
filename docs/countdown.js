// This code was adapted from:
// https://www.w3schools.com/howto/howto_js_countdown.asp

// Set the date we're counting down to
var startDate     = new Date("Nov 20, 2019 10:00:00 PST").getTime();
var countDownDate = new Date("Mar 5, 2020 00:00:00 PST").getTime();
var totalTime     = countDownDate - startDate;

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  let distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  let days = Math.floor(distance / (1000 * 60 * 60 * 24));
  let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((distance % (1000 * 60)) / 1000);

  let completed = 100*(1-distance/totalTime);

  // Display the result in the element with id="demo"
  let msg = days + "d " + hours + "h " + minutes + "m " + seconds + "s";
  document.getElementById("demo").innerHTML = msg;

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "IT'S OVER!";
  }
}, 1000);