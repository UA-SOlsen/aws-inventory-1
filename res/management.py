import boto3
import botocore
import json
import config
import res.utils as utils
import res.glob  as glob

# =======================================================================================================================
#
#  Supported services   : CloudFormation
#  Unsupported services : CloudTrail, CloudWtach, AWS Auto Scaling, Config, OpsWork, Service Catalog, 
#                               Systems Manager, Trusted Advisor, Managed Services
#
# =======================================================================================================================

#  ------------------------------------------------------------------------
#
#    CloudFormation
#
#  ------------------------------------------------------------------------

def get_cloudformation_inventory(oId):
    """
        Returns cloudformation inventory (if the region is avalaible)

        :param oId: ownerId (AWS account)
        :type oId: string

        :return: cloudformation inventory
        :rtype: json

        .. note:: https://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html
    """
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "cloudformation", 
        aws_region = "all", 
        function_name = "describe_stacks", 
        key_get = "Stacks",
        detail_function = "describe_stack_resources", 
        join_key = "StackName", 
        detail_join_key = "StackName", 
        detail_get_key = ""
    )


#
# Hey, doc: we're in a module!
#
if (__name__ == '__main__'):
    print('Module => Do not execute')