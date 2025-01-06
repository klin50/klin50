(define fact (lambda (n))
  (= n 1)
    1
  (* n fact(- n 1)))
(define fib (lambda(n))
  (= n 0)
    0
  (= n 1)
    1
  (+ fib(- n 1) fib(- n 2)))
