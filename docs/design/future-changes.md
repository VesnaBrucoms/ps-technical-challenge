# Future Changes

## Async

The existing implementation of the get all users endpoint is naive as it works through each user
sequentially. This initial implementation was chosen partly due my own unfamiliarity with threading
(owing to working primarily with containerised micro-services), combined with time available to implement.

For smaller loads like in this dataset that's fine, but for hypothetical production sizes
it's very inefficient. While this API is intended to run in a containerised environment where it can be
scaled up and down based on load, the naive implementation leads to tighter margins where more instances
need to be spun up to handle a given load than if it was more efficient.

As such one possible change to rectify this is to make use of Python's `async` to calculate many different
user levels in parallel to each other.

## Metrication

aa