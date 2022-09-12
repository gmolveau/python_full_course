# Testing

- "Classical" or Detroit-school TDD
  - from eXtreme Programming (from Detroit)
  - In Detroit-school TDD, a public API is first identified by writing a test against it, then each successive test is written as an example of its use, which drives out additional requirements.
  - At its most simple, its workflow is:
    - 1. Write a failing test
    - 2. Change the implementation to make it pass (or change the message)
    - 3. Refactor
    - 4. Go to Step 1
- "Mockist" or London-school TDD
- Discovery Testing (based on London)

Many comparisons between the two schools of thinking can be summarized as "top-down" versus "bottom-up".

Fake
    A fake is a test double that provides an alternate implementation of a real thing for the purpose of a test.
Stub
    A "stub" is any test double that implements a preconfigured response to being invoked.
Mock
    When the term "mock" or phrase "mock out" is used today, it's typically meant to describe any kind of test double ... but ...
    A mock object asserts that certain invocations are made on itself, and will raise exception as soon as any unexpected interactions take place.
Spy
    A Spy is a test double that records every invocation made against it and can verify certain interactions took place after the fact.

99% of all mocks in use today are not used for the purpose for which 99% of test double libraries were designed: to facilitate isolated test-driven development aimed at arriving at clean designs of small units that interact via pleasant-to-use interfaces.

### Don't mock what you don't own

> Don't mock what you don't own

when this phrase is used, it's spoken from the mindset that the primary value of test doubles is design feedback, wherein any pain in faking something should be responded to not with ever-more-clever test double libraries, but with a redesign of the interaction between the subject and its dependencies.

The prescription implied by "don't mock what you don't own" is to introduce your own shim/wrapper/adapter around it.

### What are __not__ unit tests ?

A test is not a unit test if:

- It talks to the database
- It communicates across the network
- It touches the file system
- It can't run at the same time as any of your other unit tests
- You have to do special things to your environment (such as editing config files) to run it.


### ABC vs typing.Protocol

## Resources

- [](https://github.com/testdouble/contributing-tests/wiki/Don't-mock-what-you-don't-own)
- <https://www.artima.com/weblogs/viewpost.jsp?thread=126923>
- <https://nedbatchelder.com/blog/201206/tldw_stop_mocking_start_testing.html>
