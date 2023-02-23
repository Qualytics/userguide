# Amazon S3

## Steps to setup Amazon S3

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/amazon-s3/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/amazon-s3/create-datastore-dark.png#only-dark){: style="width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and skipping the configuration of an Enrichment Datastore.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](/userguide/enrichment/create-enrichment-datastore/)

!!! note 
    It is important to associate an `Enrichment Datastore` with your new Datastore

    - The `Enrichment Datastore` will allow Qualytics to record `enrichment data`, copies of the source `anomalous data` and additional `metadata` for your `Datastore`

## Configuring an Enrichment Datastore

- If you have an `Enrichment Datastore` already setup, you can link it by enable to use an existing Enrichment Datastore:

    ![Screenshot](../assets/enrichment/amazon-s3/associate-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/amazon-s3/associate-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

- If you don't have an `Enrichment Datastore`, you can create one at the same page:

    ![Screenshot](../assets/enrichment/amazon-s3/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/amazon-s3/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

---
## Fields
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

###  `Datastore` S3 permissions <spam id='required'>`required`</spam>

*Note: It's necessary to update the `<bucket/path>` to your specific resource*
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:Get*"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket>/*",
                "arn:aws:s3:::<bucket>"
            ]
        }
    ]
}
```

### `Enrich Datastore` S3 permissions <spam id='required'>`required`</spam>
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket>/*",
                "arn:aws:s3:::<bucket>"
            ]
        }
    ]
}
```