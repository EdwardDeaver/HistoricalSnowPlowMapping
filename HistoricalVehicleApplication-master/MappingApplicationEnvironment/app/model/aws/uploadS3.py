import boto3
import os
s3 = boto3.client('s3')
response = s3.list_buckets()

def returnAllBuckets():
	return s3.list_buckets()


#size = os.path.getsize('tmp.txt')
#print (size)
def uploadToS3Bucket(filename, bucketName, location):
	#s3.upload_file("tmp.txt", "mappingapplicationtestbucket", "temp.txt")
	try:
		s3.upload_file(filename, bucketName, location)
	except:
		return False
	else:
		return True
	
