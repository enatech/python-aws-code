#!/usr/bin/env python

# Copyright (c) 2015 Nandini Taneja nandini.taneja@gmail.com
# All rights reserved.

import math, os
import boto
import sys
from filechunkio import FileChunkIO

bucket = sys.argv[1]
file = sys.argv[2]

# connect to Amazon S3
conn = boto.connect_s3()
bucket = conn.get_bucket(bucket)

# get the input file path
source_path = file 
source_size = os.stat(source_path).st_size

# create a multipart upload request
mpur = bucket.initiate_multipart_upload(os.path.basename(source_path))

# use a chunk size of 50MB
chunk_size = 52428800
chunk_count = int(math.ceil(source_size / float(chunk_size)))

# send the file parts
print "Start the Multipart upload\n"

for i in range(chunk_count):
	offset = chunk_size * i
	bytes = min(chunk_size, source_size - offset)
	with FileChunkIO(source_path, 'r', offset=offset,
			bytes=bytes) as fp:
		mpur.upload_part_from_file(fp, part_num=i+1)

# finish upload
mpur.complete_upload()

print "End the Multipart upload\n"
# Now list the Bucket and contents

object_in_bucket = bucket.list()
for o in object_in_bucket:
	print o.name
