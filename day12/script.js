//creating an object

let student = {
    name : "Renu",
    department : "CSE",
    cgpa : 8,
    city : "kottayam"

    };
console.log(student.name);
console.log(student.department);
console.log(student.cgpa);
console.log(student.city);

//update property

student.cgpa = 7.8;

console.log("updated cgpa:");
console.log(student.cgpa);

//add property

student.college = "geck";
console.log(student);

//object deconstructing

const {
    name,
    department,
    cgpa,
    city,
    college,
} = student;
console.log("after deconstructing");
console.log(name);
console.log(department);
console.log(cgpa);
console.log(city);
console.log(college);

// function 

//without parameters

function welcome() {
    console.log("welcome to javascript");

}

welcome();
welcome();
//function with parameters

function greet(person) {
    console.log("hello" + person);
}

greet("renu");
greet("anu");

// returning value
function add(a,b) {
    return a+b;
}
let result = add(10,20);
console.log("addition:");
console.log(result);

//square function
function square(number) {
    return number*number;
}
console.log(square(5));
console.log(square(10));

function isEven(number) {
    return number%2==0;
}

console.log(isEven(8));
console.log(isEven(7));

//arrow function

const greetArrow = (person) => {
    return "hello" + person;

};

console.log(greetArrow("renu"));
console.log(greetArrow("anu"));


const addArrow = (a,b) => {
    return a+b;
};

console.log(addArrow(20,20));
const multiply = (a,b) => a*b;
console.log(multiply(4,2));

const evenArrow = (number)=>number%2===0;

console.log(evenArrow(20));

console.log(evenArrow(17));


function subtract(a,b){

    return a-b;

}

const subtractArrow=(a,b)=>a-b;

console.log(subtract(20,10));

console.log(subtractArrow(20,10));