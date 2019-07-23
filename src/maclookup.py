import os, sys
import argparse

from macaddress import MacAddress

def add_args(parser):

    parser.add_argument('--apiKey',
                        required=True,
                        action='store',
                        help="Your personal API Key to access macaddress.io")

    parser.add_argument('-mac', '--macaddress',
                        required=True,
                        action='store',
                        help="Mac address that needs to be looked up")

    parser.add_argument('-o', '--output',
                        action='store',
                        default='json',
                        help='Format of the response')

def process(args):
        
    # import pdb;pdb.set_trace()
   
    macobj = MacAddress(apikey=args.apiKey)

    response = macobj.get_oui(macaddress=args.macaddress, output=args.output)

    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments for Macaddress loopup")
    add_args(parser)
    
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    print(process(args))
