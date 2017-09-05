import argparse as ap
import coded_decimals as cdec

parser = ap.ArgumentParser()

parser.add_argument('--digit', action = 'store', dest = 'd', type = int)
parser.add_argument('--bcd', action = 'store_true')
parser.add_argument('--xs3', action = 'store_true')
parser.add_argument('--gray', action = 'store_true')
args = parser.parse_args()

if args.d:
    if args.bcd:
        print cdec.coded_decimals(args.d).BCD()
    if args.xs3:
        print cdec.coded_decimals(args.d).XS3()
    if args.gray:
        print cdec.coded_decimals(args.d).GRAY()
