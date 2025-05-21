# Endpoints

The following endpoints are based on assumed [use cases](./use-cases.md).

## /users

Achieves use cases 2 and 3.

Returns a list of all users with their data, plus account wide achievement level.

Can filter by achievement level with `level` request argument. E.g. `level=bronze`.

## /users/{userId}

Achieves use case 1.

Returns single user by given ID with their data, plus account wide achievement level.