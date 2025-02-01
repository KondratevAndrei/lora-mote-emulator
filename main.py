import sys
import json
from src import main
from src.cli import define_parser

VALID_PORTS = (2, 5)
JSN_FIELDS_VS_PORTS = {2: ('vx', 'vy', 'vz', 't', 'flags')}
args = define_parser().parse_args()

if args.command == 'app':
    try:
        data = json.loads(args.msg)
    except json.decoder.JSONDecodeError as e:
        print('json invalid:', e)
        sys.exit()

    if args.fport not in VALID_PORTS:
        print(f'invalid ports, ports parameters must be in {str(VALID_PORTS)}')
        sys.exit()


    if not all(key in data for key in JSN_FIELDS_VS_PORTS[args.fport]):
        print(f'json must consist all keys: {str(JSN_FIELDS_VS_PORTS[args.fport])}', )
        sys.exit()

if args.command in ('join', 'app'):
    old_argv = sys.argv
    sys.argv = [old_argv[0], "pull"]
    main()
    sys.argv = old_argv

main()
