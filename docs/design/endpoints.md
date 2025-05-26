# Endpoints

The following endpoints are based on the assumed [use cases](./use-cases.md).

## Primary

### /users

Achieves use cases 2 and 3.

Returns a list of all users with their general user data, plus account wide achievement level.

#### /users?level=platinum

Achieves use case 3.

Can filter all users by achievement level with the `level` request argument. E.g. `level=bronze`.

### /users/{userId}

Achieves use case 1.

Returns single user by given ID with their data, plus account wide achievement level.

## Other

### /docs

API docs page for easier understanding of what's available and possible with this API.

**Previous page:** [Use Cases](./use-cases.md)

**Next page:** [Data](./data.md)