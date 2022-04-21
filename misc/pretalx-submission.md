## Abstract

While implementing _variations_ of a certain functionality, where series of elements are created or processed one by one, developers sometimes end up creating loop constructs that don't feel right. They notice that they basically implement the same algorithm multiple times and only need to vary on &hellip;

- different loop start or end criteria,
- different element selection criteria, or
- different calls to other code to further process the selected elements.

After having noticed this, they try to factor out the common (algorithmic) part(s) of the loop construct and implement the variations as _conditional code inside the loop construct_. The end result feels even _less_ comfortable; the code becomes more complex, less performant, and more difficult to maintain.

This talk shows a way out of this fish trap: the developer can refactor the heart of their algorithm or processing loop into a **generator function** and implements the required variations as distinct functions or generators consuming the elements of their factored out generator. Many times it even suffices to build a **pipeline** combining the factored out generator with building blocks from the standard library `itertools` module or the `more-itertools` package. After this, the code suddenly looks elegant again! 

As an example, the talk introduces some variations of functionality based on the Fibonacci sequence. For example, one function returning all Fibonacci numbers up to a certain value, and another one returning the n'th ordinal Fibonacci number.

Without refactoring into generator functions, you'd create duplicated code that seems impossible to factor out, containing only minor differences. Once refactored into a generator function using the appropriate `itertools` functions, the code conforms to the DRY (_Don't Repeat Yourself_) criterium again.

This talk helps the developer recognizing this pattern and provides a way of refactoring into more _pythonic_ code.

## Description

Have you ever found yourself coding variations of a loop construct where fragments of the loop code were exactly the same between the variations? Or, in an attempt to factor out these common parts, you ended up with a loop construct containing a lot of conditional code for varying start, stop, or selection criteria?

You might have felt that the end result just didn't look right. Because of the duplicated parts in your code, you noticed that the code didn't conform to the DRY (_Don't Repeat Yourself_) principle. Or, after an attempt to combine the variations into a single loop, with consequently a lot of conditional code, your inner voice told you that the resulting code had become too complex and difficult to maintain.

This talk will show you a way out of this situation. It demonstrates how you can create a **generator function** that implements only the common parts of your loop construct. Subsequently you will learn how you can combine this generator function with distinct hand-crafted functions or building blocks from the standard library `itertools` module or the `more-itertools` package.

As an example, imagine you'd need to implement some varying functionality based on the Fibonacci sequence. This talk shows you how it would look like before and after you've refactored it into a **pipeline of generators**.

After having seen this pattern, you will recognize more quickly when this kind of refactoring helps you to create more maintainable and more Pythonic code.

## Audience

The presentation is for Python developers having a drive to learn more about refactoring patterns and having the ambition to create elegant, maintainable, Pythonic code. Ideally, they have some experience in creating software that shall be maintained not only by theirselves, but also somebody else than the author of the code.

I expect that the attendees will be able to recognize specific loop constructs to be candidate for refactoring into a generator function and distinct other building blocks. These other building blocks can simply be tools from the `itertools` module or `more-itertools` packages, or own-written functions or generators.

## Outline

Introduction (4 minutes)

- Show the imaginary problem: the customer requests some varying functionality, all based om the Fibonacci sequence:
  - `fib_list_to(n)`: _Return list of all Fibonacci numbers less than n_
  - `fib_ordinal(n)`: _Return the n'th Fibonacci number, counting from 0_
  - `fib_first_n(n)`: _Return the first n Fibonacci numbers_
  - `largest_fib_less_than_n(n)`: _Return largest Fibonacci number less than n_
  - `smallest_fib_greater_equal_n(n)`: _Return the smallest Fibonacci number greater than or equal to n_

Implementation (3 minutes)

- Show the traditional implementation of the first two requested variants
- Identify the common parts of the code and the differing parts
- Start reasoning about ways on how to refactor them, in order to prevent code duplication
  - Also about combining both functionalities within the same loop --> resulting in horrendous code

Sidestep and introduce shortly **generator functions** (3 minutes)

- It is a function with one or more `yield` statements
- Explain shortly how you can use such a function, for-loop, or `iter()`, `next()`, `StopIteration`

Implementation of an endless range of Fibonacci numbers (3 minutes)

- Show the implementation of `fib_gen()`, a generator function
- Pay attention on how this ends up as shortest and most "canonical" implementation

Sidestep and introduce the standard library `itertools` module and the `more-itertools` package (5 minutes)

- With extra focus on `dropwhile()`, `islice()`, and `takewhile()` from `itertools`, and
- `first()`, `last()`, and `one()` from `more-itertools`.

Show implementations of the desired functions, ... (6 minutes)

- Refactored into `fib_gen()`, combined with
- the building blocks from `itertools` and `more-itertools`, identified above, and
- `list()`.

Some concluding notes (3 minutes)

- In traditional OO-only programming environments, some of the challenges identified in this talk can be solved by implementing patterns from the GoF book:
  - `Iterator`
  - `Visitor`
  - `Template`.
- However, the proposed solution in this talk seems to be more suitable for Python.

Recap (3 minutes)

- Consider refactoring into generators when you see loops containing a lot of conditional code
- Get acquainted with all the wonderful functions available through `itertools` and `more-itertools`
- Happy control flow refactoring!

(A **spare slide** of a similar problem (3 min extra time)

- Process the outcome of complex model calculations as a series of `namedtuple` instancies that either (depending on the mode of operation)
  - need to be written as lines to a CSV file, or
  - should be collected as batches of a predetermined size that must be written as rows in a database table (`more_itertools.chunked()`)

)

## Category

_Development & Software Engineering Practices_

## EuroPython tweet

Have you ever found yourself coding variations of a loop construct without knowing how to cleanly factor out the common parts? This talk will show you a way out: refactor into generator functions!
