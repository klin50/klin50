//Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
function fact(n){
  if(n == 0){
    return 0;
  }
  if (n == 1){
    return 1;
  }
    return n*fact(n-1);
}
//TEST CALLS
fact(1)
fact(5)
fact(10)
// (writing here can facilitate EZer copy/pasting into dev console now and later...)


//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
function fib(n){
  if(n == 0){
    return 0;
  }
    if(n == 1){
    return 1;
  }
    return fib(n-1) + fib(n-2);
}
//TEST CALLS
fib(0)
fib(5)
fib(10)
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

//=================================================================
