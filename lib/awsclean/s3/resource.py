import boto3


class S3Clean:
    def __init__(self, client=boto3.resource('s3')):
        self.client = client

    def plan(self):
        print("Listing S3 Buckets:")
        all_buckets = self.client.buckets.all()
        self._ifNoBucket(all_buckets)
        for bucket in all_buckets:
            print(bucket.name)

    def destroy(self):
        # Print out bucket names
        all_buckets = self.client.buckets.all()
        self._ifNoBucket(all_buckets)

        for bucket in all_buckets:
            print("Going to delete bucket: {0}".format(bucket.name));
            self._emptyBucket(bucket)
            bucket.delete()

    def _ifNoBucket(self, all_buckets):
        if (len(list(all_buckets)) == 0):
            print("There is none S3 bucket!")

    def _emptyBucket(self, bucket):
        while True:
            objects_in_bucket = list(bucket.objects.all())
            if (len(objects_in_bucket) == 0):
                return
            else:
                for o in objects_in_bucket:
                    o.delete()


s3clean = S3Clean()
