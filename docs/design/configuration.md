# Configuration

As the intended deployment of this API is within a container, then configuration is done through environment
variables set on the container. There are only three defined:

* `USERS_API_URL` - the URL (format http://server:port/) that the playstation-tech-test-api.jar server can be found at
* `SWAGGER_JSON_PATH` - static location of the `swagger.json` file within the container/computer.
* `LOG_LEVEL` - the API's overall logging level.

A production version of this API would have many more variables to set. Primarily ones relating to security
like passwords, certificates, and secret keys. These would be set either directly in the production deployment
package (in my experience a Helm Chart) that is in a repository locked down to only those who need to know and
set it (previously that was just the dev team).

Or preferably they would exist inside of the container orchestration platform where they cannot be easily retrieved
by the user. Instead the package (Helm Chart) would store the key/cert/etc needed for the container to be granted
the secret (password, cert, etc) by the platform.

For example, in the past I have deployed and made use of Bitnami's `SealedSecret`s (https://github.com/bitnami-labs/sealed-secrets)
to perform the above for passwords and keys and the like. [cert-manager](https://github.com/cert-manager/cert-manager) has
certificates covered.

**Previous page:** [Data](./data.md)

**Next page:** [Key Assumptions](./key-assumptions.md)