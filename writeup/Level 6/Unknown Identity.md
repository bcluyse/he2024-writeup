### Challenge description

I detected an attempt by an unknown identity to access our cloud account. Can you help me find out who it was?

All I have is this string: `AIDATZ2X44NMHZV4BWEMR`

### Solution

Initial thoughts
- The string seems like an identifier of some sort.
- Unknown Identity -> Identity Access Management
	- `AIDATZ2X44NMHZV4BWEMR`
	- `AKIA4A5PYG3WQCQDE2MV`
	- This has the same for as an AWS IAM access key

The following blog post gives a lot more information on the format of the access key: https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489

![[aws_creds.png]]

Using the base32 decoding script provided in this post, this gives the account id: 261640479576

https://261640479576.signin.aws.amazon.com/console/

This URL redirects to a proper sign in page on north-europe-1 so this seems to be a valid AWS account id.

### The final solution

Finally, I found some inspiration at https://hackingthe.cloud/aws/enumeration/enumerate_principal_arn_from_unique_id/. 

- Go to IAM
- Create a role with a Custom Trust Policy

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "AIDATZ2X44NMHZV4BWEMR
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

- Save
- Check afterwards and see that it has transformed.

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::261640479576:user/aGUyMDI0ezE0bV9wcjFuYzFwNGxfdW5jMHYzcjNkIX0="
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

the user name is base64 encoded for the flag:

he2024{14m_pr1nc1p4l_unc0v3r3d!}