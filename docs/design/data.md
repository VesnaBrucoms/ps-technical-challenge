# Data

This page documents the initial and planned JSON objects that the API responds with. Along with specific
information on the given fields.

## Initial

The initial JSON objects that the API will respond with are as simple as possible. They provide only the
basic user information combined with the associated requested account wide achievement level which comes
under the `overallAchievementLevel` field.

The `overallAchievementLevel` field has 5 possible values: `None`, `Bronze`, `Silver`, `Gold`, `Platinum`.
The `None` value is an additional value to cover the scenario where a user is not eligible for even a
`Bronze`.

Any errors returned from the user API will be captured and bubbled back up to this API's endpoints to
construct a user friendly JSON containing the error details.

### /users/2

#### Expected (200)

```json
{
    "user": {
        "id": 2,
        "name": "Bronze Tester",
        "email": "btester@email.com"
    },
    "overallAchievementLevel": "Bronze"
}
```

#### Error (404, 500)

```json
{
    "message": "Getting user library with ID 2 could not be found",
    "status_code": 404
}
```

### /users

Simply a list of the above object.

```json
[
    {
        "user": {
            "id": 1,
            "name": "None Tester",
            "email": "ntester@email.com"
        },
        "overallAchievementLevel": "None"
    },
    {
        "user": {
            "id": 2,
            "name": "Bronze Tester",
            "email": "btester@email.com"
        },
        "overallAchievementLevel": "Bronze"
    },
    {
        "user": {
            "id": 3,
            "name": "Silver Tester",
            "email": "stester@email.com"
        },
        "overallAchievementLevel": "Silver"
    }
    ...
]
```

#### Error (404, 500)

An error in any one of the user, library, and achievement processes will result in a complete failure
of the process.

```json
{
    "message": "Getting user library with ID 2 could not be found",
    "status_code": 404
}
```

## Planned

If I have the time I will implement these changes.

### /users

As the initial get all users endpoint stands, it fails the entire request if any one user data retrieval
fails. This change would allow for multiple failures to occour without the whole request failing, so as to
still provide some use for the end user (system or person), while also aiding debugging on which specific
users are problematic.

```json
{
    "users": [
        {
            "user": {
                "id": 1,
                "name": "None Tester",
                "email": "ntester@email.com"
            },
            "overallAchievementLevel": "None"
        },
        {
            "user": {
                "id": 2,
                "name": "Bronze Tester",
                "email": "btester@email.com"
            },
            "overallAchievementLevel": "Bronze"
        },
        ...
    ],
    "errors": [
        {
            "message": "Getting user library with ID 3 could not be found",
            "status_code": 404
        },
        ...
    ]
}
```

**Previous page:** [Endpoints](./endpoints.md)

**Next page:** [Key Assumptions](./key-assumptions.md)