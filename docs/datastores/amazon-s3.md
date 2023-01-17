# Amazon S3

## Steps to setup Amazon S3

---

![Screenshot](../assets/datastores/amazon-s3/create-data-store-light.png#only-light){: style="height:450px;width:450px;"}
![Screenshot](../assets/datastores/amazon-s3/create-data-store-dark.png#only-dark){: style="height:450px;width:450px;"}

### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App.
### `URI` <spam id='required'>`required`</spam>

* S3 URI is the unique resource identifier within the context of the S3 protocol. They follow this naming convention : `S3://bucket-name/key-name`.

* How to get the URL of an S3 Object via the AWS Console:
    1. Navigate to the AWS S3 console and click on your bucket's name.
    2. Use the search input to find the object if necessary.
    3. Click on the checkbox next to the object's name.
    4. Click on the Copy URL button.

![Screenshot](../assets/datastores/amazon-s3/get-s3-object-url.png)

### `Access Key` and `Secret Key` <spam id='required'>`required`</spam>

* The keys are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).

* You can manage your Access Keys in AWS Management Console.

* How to get your Access Key ID and Secret Access Key follow next steps:

    1. Open the IAM console.
    2. From the navigation menu, click Users.
    3. Select your IAM user name.
    4. Click User Actions, and then click Manage Access Keys.
    5. Click Create Access Key.
    6. Your keys will look something like this:
        7. Access key ID example: `AKIAIOSFODNN7EXAMPLE`.
        8. Secret access key example: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.
    9. Click Download Credentials, and store the keys in a secure location.

###  `Data Store` S3 permissions <spam id='required'>`required`</spam>

*Note: It's necessary to update the `<bucket/path>` to your specific resource*
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": [
            "s3:Get*",
            "s3:List*",
        ],
        "Effect": "Allow",
        "Resource": "arn:aws:s3:::<bucket/path>/*"
        }
    ]
}
```

### `Enrich Store` S3 permissions <spam id='required'>`required`</spam>
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
          "s3:Get*",
          "s3:Put*",
          "s3:List*",
          "s3:Delete*"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::<bucket/path>/*"
    }
  ]
}
```