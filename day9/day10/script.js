// ===============================
// Day 10 - JavaScript Portfolio
// ===============================


// -------------------------------
// Change Title
// -------------------------------

function changeTitle() {

    document.getElementById("title").innerHTML =
        "Welcome to My Interactive Portfolio 🚀";

}



// -------------------------------
// Change About Section
// -------------------------------

function changeAbout() {

    document.getElementById("aboutText").innerHTML =

        "I enjoy building AI-powered applications, full-stack websites, research projects, and cybersecurity solutions. I love solving real-world problems using technology.";

}



// -------------------------------
// Dark Mode
// -------------------------------

function changeTheme() {

    document.body.classList.toggle("dark");

}



// -------------------------------
// Counter Project
// -------------------------------

let count = 0;

function increaseCounter() {

    count++;

    document.getElementById("counter").innerHTML = count;

}

function decreaseCounter() {

    count--;

    document.getElementById("counter").innerHTML = count;

}

function resetCounter() {

    count = 0;

    document.getElementById("counter").innerHTML = count;

}



// -------------------------------
// Contact Form
// -------------------------------

function showMessage(event) {

    event.preventDefault();

    let name = document.getElementById("name").value;

    alert("Thank you " + name + "! Your message has been received.");

}



// -------------------------------
// Greeting
// -------------------------------

function greeting() {

    let hour = new Date().getHours();

    if (hour < 12) {

        console.log("Good Morning");

    }

    else if (hour < 17) {

        console.log("Good Afternoon");

    }

    else {

        console.log("Good Evening");

    }

}

greeting();



// -------------------------------
// Live Clock
// -------------------------------

function updateClock() {

    let now = new Date();

    console.log(now.toLocaleTimeString());

}

setInterval(updateClock, 1000);



// -------------------------------
// Array Example
// -------------------------------

let skills = [

    "Python",

    "Java",

    "React",

    "JavaScript",

    "SQL"

];

console.log("Skills");

for (let i = 0; i < skills.length; i++) {

    console.log(skills[i]);

}



// -------------------------------
// Object Example
// -------------------------------

let student = {

    name: "Renu",

    cgpa: 7.87,

    department: "CSD"

};

console.log(student.name);



// -------------------------------
// Function with Parameters
// -------------------------------

function greet(name) {

    console.log("Welcome " + name);

}

greet("Renu");



// -------------------------------
// Random Quote Generator
// -------------------------------

let quotes = [

    "Never stop learning.",

    "Dream big and work hard.",

    "Code. Learn. Repeat.",

    "Success comes from consistency.",

    "Believe in yourself."

];

function randomQuote() {

    let random = Math.floor(Math.random() * quotes.length);

    alert(quotes[random]);

}



// -------------------------------
// Change Image
// -------------------------------

function changeImage() {

    document.getElementById("profileImage").style.border =
        "8px solid red";

}



// -------------------------------
// Mouse Event
// -------------------------------

document.getElementById("profileImage")

.addEventListener("mouseover", function () {

    this.style.transform = "scale(1.1)";

});

document.getElementById("profileImage")

.addEventListener("mouseout", function () {

    this.style.transform = "scale(1)";

});



// -------------------------------
// Console Output
// -------------------------------

console.log("JavaScript Loaded Successfully");