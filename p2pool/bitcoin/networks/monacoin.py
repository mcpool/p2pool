import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex') #pchmessagestart
P2P_PORT = 9401
ADDRESS_VERSION = 50 #pubkey_
RPC_PORT = 9402
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'monacoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 90 # s
SYMBOL = 'MONA'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'monacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Monacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.monacoin'), 'monacoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://mona.explorer.p2pool-stats.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://mona.explorer.p2pool-stats.info/address/' #dummy for now, not supported by explorer
TX_EXPLORER_URL_PREFIX = 'http://mona.explorer.p2pool-stats.info/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
