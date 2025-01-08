
/*
    Team Me and Me Alone: Kevin Lin
    SoftDev pd5
    K28 -- Manipulating the DOM
    2025-01-07t
    Time: 0.5 hour
*/


//send diagnostic output to console (basically a print statement)
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree
var removeItem = function(n)
{
    //Gets all elements with the specified tag and returns an array
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
function fib(n){
  if(n == 0){
    return 0;
  }
    if(n == 1){
    return 1;
  }
    return fib(n-1) + fib(n-2);
}
// FAC
function fact(n){
  if(n == 0){
    return 0;
  }
  if (n == 1){
    return 1;
  }
    return n*fact(n-1);
}
// GCD
function gcd(a, b){
    var max = Math.max(a,b);
    if(a == 0 || b == 0){
        return 0;
    }
    for(var i = Math.floor(max/2); i > 0; i --){
        if(a%i == 0 && b%i == 0){
            return i;
        }
    }
    return 1;
}


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return retVal;
};


