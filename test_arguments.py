

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--workspace', metavar='path', required=True,
                        help='the path to workspace')
    parser.add_argument('--schema', metavar='path', required=True,
                        help='path to schema')
    parser.add_argument('--dem', metavar='path', required=True,
                        help='path to dem')
    args = parser.parse_args()

    print(args.workspace)
    
