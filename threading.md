coroutines
----------

generators "pull" data
coroutines = generators with send()
coroutines "push" data

- concurrency is two lines of customers with only one cashier (lines take turns ordering)
- parallelism is two lines of customers with two cashiers (each line gets its own cashier)

GIL : cpython is single-threaded