* dev env
  * remote repo
* Actions
  * run tests
  * building & release image
  * packaging & release files
* docs
  * explain choices
    * Flask
      * lightweight; familiar
    * black
      * very opinionated, so no thinking; is formatter
    * CI/CD
      * good to automate; want to practice more with Actions
    * OpenAPI
      * familiar; useful
    * why RESTApi over console/frontend/etc
      * familiar
    * Python
      * most experience with Python; good for rapid dev like this project
    * Docker container
      * why at all
        * assumption: deployed to K8s, thus scaleable; plus stateless so easier to scale if demand is high (though unlikely)
      * base image
        * alpine/Python - lightweight, work done for me