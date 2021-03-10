import argparse as arg
from provider import CurrencyProvider
from debug import Debug


provider=CurrencyProvider()


parser = arg.ArgumentParser( description='Convert Currency Values at Exchanges')

parser.add_argument('fro',
                       metavar=('from'),
                       
                       type=lambda f:str(f).upper(),
                       # converting argument to upper case

                       help='currency to covert from',
                       choices=provider.symbols
                       )
                        
parser.add_argument('value',
                       metavar='value',
                       type=float,
                       help='value in currency1')
parser.add_argument("to",
                    metavar=("to"),
                    type=lambda f:str(f).upper(),
                    help="Currency to which convert to",
                    choices=provider.symbols)

parser.add_argument("-v","--verbose",
                    action='store_const',
                    const=1,
                    default=0,
                    help="if true, print a descriptive message of what is happening")

args = parser.parse_args()
log=Debug(args.verbose)
provider.loadvalues()


log(f"Converting {provider._name(args.fro)} to {provider._name(args.to)}")

result=provider.data[args.fro]/provider.data[args.to]*args.value

log(f"{args.value} {provider._name(args.fro)} equals {result} {provider._name(args.fro)}" )

print(result)
