# awsclean
awsclean is a simple python utility to cleaning all your aws resources under your aws account within specific version.

Requirement
===========
   * Python3
   * PIP
    - run ``` pip install -r requirement.txt ```
   * Ensure you have your AWS root account credentials and region set up globally
        - Next, set up credentials (in e.g. ``~/.aws/credentials``):

        ```

            [default]
            aws_access_key_id = YOUR_KEY
            aws_secret_access_key = YOUR_SECRET
        ```
        Then, set up a default region (in e.g. ``~/.aws/config``):

       ```

            [default]
            region=us-east-1
        ```

Usage
===========

* Clone the code from `https://github.com/JohnnyNiu/awsclean.git`
* List resources AwsClean will destroying
```
    ./bin/awsclean plan
```

* Destroy AWS resources
```
    ./bin/awsclean destroy
```




Branch Info
===========

   * The devel branch corresponds to the release actively under development.
   * We'd love to have your contributions

Licence
=======
GNU
Click on the [Link](COPYING) to see the full text.
