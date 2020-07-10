# AWS Lambda Test Internet Connectivity

This repo contains a simple Lambda functions used to test internet connectivity.

## Getting Started

This repo makes use of the serverless framework to package and deploy all functions.

### Prerequisites

Serverless Framework

```
Follow official installation instruction at https://www.serverless.com/framework/docs/providers/aws/guide/installation/
```

Serverless Plugins

```
npm install serverless-python-requirements
```

AWS Credentials to use with serverless

```
The serverless framework will read credentials from ~/.aws/credentials not from ~/.aws/config
Hence, you will have to place the required profiles in ~/.aws/credentials file
```

### Configuration

Inside ```serverless.yml``` you'll find 
- Profiles required to deploy the functions
- IAM role used described in ```iamRoleStatements```
- Supporting resources in ```resources``` like security groups and buckets
- VPC configuration


Inside ```requirements.txt``` you'll find 
- All libraries and dependencies for the functions to run


## Deployment

After configuring the environment deploy as follows, using required aws profile and stage name.

```
AWS_PROFILE=<my-profile> SLS_DEBUG=* serverless deploy -v
```
