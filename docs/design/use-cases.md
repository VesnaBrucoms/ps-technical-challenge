# Use Cases

I can think of at least three use cases for this service:

1. Retrieve achievement level for one user
2. Retrieve achievement levels for all users
3. Retrieve all users of a specific level

Use case 1 covers a scenario like needing to check or view that one specific user's level. Such as the end
user themselves accessing the relevant page.

Use case 2 covers another backend service requiring all user levels to perform additional functions. Perhaps
for something like internal metrication or stats for interested end users.

Use case 3 is similar to case 2, but for situations where a service only needs all users of a particular
level. Such as the above example of end user viewable stats.

## Additional Use Cases

If additional use cases come to mind during further implementation then they will be documented here.

### Non PS Games Filter

A fourth use case might be to exclude non-PlayStation titles from a user's library when calculating their
account wide achievement level.

As a key assumption is that they only exist to fill out the dataset (see [relevant page](./key-assumptions.md#non-playstation-games)),
this will be implemented as an optional filter on both endpoints.

**Previous page:** [Overview](./overview.md)

**Next page:** [Endpoints](./endpoints.md)