# Recursion

## 1. Introduction to Recursion
* A function is called recursive if it calls itself.

#### Let's consider this example problem
    def fun1():
        print("fun1 is called")

    def fun2():
        print("Before fun() 1")
        fun1()
        print("After fun() 1")

    print("Before fun2()")
    fun2()
    print("After fun2()")

#### The output of the code will be:

    Before fun2()
    Before fun() 1
    fun1 is called
    After fun() 1
    After fun2()

#### Execution flow of the program.

    A[Start] --> B{print("Before fun2()")}
    B --> C{fun2()}
    C --> D{print("Before fun() 1")}
    # Here fun2() stops execution and wait for fun1() to complete its execution
    D --> E{fun1()}
    E --> F{print("fun1 is called")}
    F --> G{print("After fun() 1")}
    G --> H{print("After fun2()")}
    H --> I[End]

* So the last function which is called finishes it's execution first and the first function finishes it's execution in the end. 
* That means callers finished it's execution once the called function has finished and caller waits for the called function to finish so that the caller can begin from the next line.
----------------------------------------------------------------
----------------------------------------------------------------
* Now we learnt how function calls works, Let's see how recursive functions work.
* A Function is called recursive if the function calls itself directly or indirectly.

#### Direct Recursion
    def fun1():
        ........
        ........
        fun1()
        ........
        ........

#### InDirect Recursion
    def fun1():
        ........
        ........
        fun2()
        ........
        ........

    def fun2():
        ........
        ........
        fun1()
        ........
        ........

* Direct recursion is the most common recursion. We don't see the indirect recursion much.

#### Example of a simple recursive function

    def fun():
        print("Recursion is fun")
        fun()

    fun()
* This is an infinite loop recursion so we will get an Recursion error: Maximum recursion depth limit exceeds. As python has limit on the number of function calls in python that limit exceeds after certain time and leads to error.
####
    def fun(count):
        if count == 0:
            return
        print("Recursion is fun.")
        fun(count-1)
    
    fun(5)

* The condition that we add `count == 0 return`. This condition is caled base case.
* When you write a recursive function you mainly reduce the problem into smaller problem. You keep on reducing the problem into smaller problems and there would be some cases where you cannot reduce it further and those cases have to be handled explicitly and those cases are called **bases cases**
* You always must write a base case so that your problems always stops at a certain point or else you will get an error or some other problem.

### Typical Structure of a Recursive function.

    def fun(.....):
        Base case
        .......................
        .......................
        Recursive call(i.e. call to fun(....))
        with atleast one change to parameter so
        that call aproaches toward base case
        .......................
        .......................

* When we do a recursive call inside a function we do this with some different parameters in such a way that these parameters reduce your problem size and they approach towards the base case. If your calling initially `n=10` and your base case is `n=0` your recursive calls should be made in such a way that you approach toward 0. For example `-1` or `//2` then you will have 10, 5, 2, 1, 0. So you need to approach one of the base cases if there are multiple, that's what the recursive call should be.
* You can have global variables which are changed inside the function and you can have conditions on those global variables but the typical recursive function changes the parameters such a way they approach a base case.

----------------------------------------------------------------
----------------------------------------------------------------

## 2. Applications of Recursion

* Recursion is one of the core topics in programming. Any program that can be programmed using iteration can also be programmed using recursion and vice versa. So if we can use both then where do we use Recursion.?

* Many standar algorithmic techniques are basically Recursive in nature.
    * Dynamic Programming
    * Backtracking
    * Divide and Conquer (Binary search, Quick sort and Merge sort)

* Many problems are inherently recursive  in nature
    * Tower of Hanoi, 
    * DFS based traversals(DFS of Graph and Inorder/Preorder/Postorder traversals of tree)

* All these things can also be solved using iterations as they have same expressive power and many times if you have a equivalent iterative code, iterative code causes less overhead. If you write recurive binary serach it will take BigO(logn) auxilary space but if you write iterative binary search it will take BigO(1) auxilary space.
* One more problem with recursion is function call overhead but still recursion is used because of ease of implementation.
* Recursive thinking is necessary skill for programmers. If you have a solution of sub problem how do you use the solution of sub problem to solve the bigger problems. Many times we write recursive code to solve the problem and then we convert it into iterative code to reduce the overhead.

----------------------------------------------------------------
----------------------------------------------------------------

## 3. Writing base cases in Recursion
* Many times when we write a recursive solution we can easily get the recursion part, the recursive calls or recursive formula but becomes difficult to write down the base cases.

####
    # Problem 01: Factorial n where n >= 0

    def factorial(num):
        if num == 0:
            return 1
        return num*factorial(num-1)

    # Problem 02: N-th fibonacci number n where n >= 0

    def fibonacci(num):
        if num == 1 or num == 0:
            return 1
        return fibonacci(num-1) + fibonacci(num -2)

* We must be sure when we write a base case that we handle all the limit values and we also handle every recursion. We need to figure out where all recursions are ending.

## 4. Tail Recursion

* A function is called tail recursive if the recursive call is the last thing done by the function.

####  tail recursive
    def fun(n):
        if n<=0:
            return
        print(n, end=" ")
        fun(n-1)

#### not tail recursive
    def fun_1(n):
        if n<=0:
            return
        fun_1(n-1)
        print(n, end=" ")

    def fact(n):
        if n==0:
            return 1
        return n*fact(n-1)

* The result of the recursive call shouldn't be used by the caller again to become tail recursive. When you say tail recursive it means there is no line executed in the caller, caller has to just make a recursive call and once the recursive call is over caller also finishes.

* A function which is tail recursive is optimized by the modern compiers and it's good to have tail recursive functions.
* tail call elmination
* In python you can always change a tail recursive function to a loop

####
    def fun(n):
        if n<=0:
            return
        print(n, end=" ")
        fun(n-1)

    def fun(n):
        while n!=0:
            print(n, end=" ")
            n = n-1

#### Examples of standard algorithms that are tail recursive
* Quick sort
* Postorder Tree Traversal.

* These algos are faster than other because they go through tail call elmination. You can optimize these in python using while near if and change the parameter at the bottom instead of function call.

* A very important point: If you want to get a last digit of a number divide modulo it by 10.

* palindrome is something that is same from front and back. So if you want to check if a number is palindrome or not you can convert it into string and check if the string is same from front and back.