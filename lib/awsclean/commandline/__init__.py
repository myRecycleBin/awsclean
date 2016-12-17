print("Start CommandLine parsing...")

import argparse

parser = argparse.ArgumentParser(description="AwsClean will clean AWS resources under your account.")
parser.add_argument('action', choices=['plan','destroy'], help="action that AwsClean will start" )

args = parser.parse_args()