#!/bin/bash

export AWS_ACCESS_KEY_ID=************************
export AWS_SECRET_ACCESS_KEY=**********************
aws s3 ls



aws s3 cp cat0.jpg s3://staticweb-2514

aws s3 cp cat1.jpg s3://staticweb-2514

aws s3 cp cat2.jpg s3://staticweb-2514

aws s3 cp index.html s3://staticweb-2514


