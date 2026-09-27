from collections import ChainMap
import os, argparse

defaults = {
    'a': 'admin',
    'u': 'junevy'
}

parser = argparse.ArgumentParser()
parser.add_argument('-a')
parser.add_argument('-u')
args = parser.parse_args()

cmd_ln_arg = {k: v for k, v in vars(args).items() if v}
# print(cmd_ln_arg)

# combine into chanin_map
combined = ChainMap(cmd_ln_arg, os.environ, defaults)
print(combined['a'])
print(combined['u'])
