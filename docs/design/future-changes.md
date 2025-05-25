# Future Changes

These are possible changes to the project that could/should be made either as a possible improvement, or
a hypthetical consideration if this was a production project not an interview tech test.

## Async

The existing implementation of the get all users endpoint is naive as it works through each user
sequentially. This initial implementation was chosen partly due my own unfamiliarity with threading
and concurrency (owing to working primarily with containerised micro-services), combined with time
available to implement.

For smaller loads like in this dataset that's fine, but for hypothetical production sizes
it's very inefficient. While this API is intended to run in a containerised environment where it can be
scaled up and down based on load, the naive implementation leads to tighter margins where more instances
need to be spun up to handle a given load than if it was more efficient.

As such one possible change to rectify this is to make use of Python's `asyncio` to calculate many different
user levels more efficiently by allowing other API requests to be sent while waiting for those already sent,
and to proceed with calculating.

### Possible Implementation

The following code snippets are likely to contain errors regarding how an asynchronous implementation
would actually work. Instead they're intended to give a rough idea on where changes would need to be made.

At the very least the functions in the `users` module will be changed to be `async` and awaitable with the
`aiohttp` library. For example:

```python
async def get_user_library(user_id, session):
    endpoint = url + "users/" + str(user_id) + "/library"
    logger.debug("Getting user library from endpoint {}".format(endpoint))

    async with session.get(endpoint) as response:
        r = await response.text()
    if r.status_code == 404:
        msg = "Not found error from users API ID {}".format(user_id)
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)
    elif r.status_code != 200:
        msg = "Error received from users API with ID {}".format(user_id)
        logger.error(msg)
        raise UserDataNotFoundError(msg, r.status_code)

    return r.json()
```

In the `component` module the calling function might be adjusted to be like so:

```python
async def get_user_achievement_level(user_id):
    async with aiohttp.ClientSession() as session:
        library = asyncio.gather(asyncio.create_task(get_user_library(user_id, session)))

    level = ""
    if len(library["ownedGames"]) <= 10:
        level = "None"
    else:
        percentages = await get_user_completed_percentages(
            library["user"]["id"], library["ownedGames"]
        )
        level = calculate_achievement_level(percentages)

    logger.debug("User %s level set to %s", user_id, level)
    return {"user": library["user"], "overallAchievmentLevel": level}
```

### Tests

The following is a batch of basic testing to aid in determining a rough improvement on an `asyncio` implementation.

Naive tests:
1. 0.7312121391296387
2. 0.590329647064209
3. 0.5529520511627197
4. 0.6108663082122803
5. 0.6404235363006592
6. 0.624523401260376
7. 0.5877575874328613
8. 0.6067438125610352
9. 0.6081497669219971
10. 0.6116228103637695

Mean = 0.6164581060409546 seconds

Async tests:
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

Mean =

## Metrication

Some basic metrics would help in understanding where heavier loads exist, and in feeding back to the
container orchestration platform (Kubernetes or some other flavour) to scale up or down.

Some possible metrics to send to something like Prometheus:

* get_all_users_levels_request_count
* get_all_users_levels_filtered_request_count
* get_user_level_request_count
* get_all_users_levels_duration
* get_user_level_duration

For internal monitoring then something Kibana or Grafana would be suitable.