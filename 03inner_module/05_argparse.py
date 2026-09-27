import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='backup',
        description='backup MySql database',
        epilog='Copyright(r), 2023'
    )
 
    # 位置参数不需要 写 - xx，也不需要写名字
    parser.add_argument('outfile')
    parser.add_argument('host', default='localhost')
    parser.add_argument('port', default='502', type=int)
    parser.add_argument('-u', '--username', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-database', required=True)
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz')

    args = parser.parse_args()

    print('parsed args:')
    print(f'outfile= {args.outfile}')
    print(f'host= {args.host}')
    print(f'port={args.port}')
    print(f'username={args.username}')
    print(f'password={args.password}')
    print(f'database={args.database}')

    print(parser)

if __name__ == '__main__':
    main()