import toml
import random
from utils import run, accounts, sleep, updateAuth, systemAccounts

config = toml.load('./config.toml')

def resign(account, controller):
    updateAuth(account, 'owner', '', controller)
    updateAuth(account, 'active', 'owner', controller)
    sleep(1)
    run(config['cleos']['path'] + 'get account ' + account)

if __name__ == '__main__':
    resign('eosio', 'eosio.prods')
    for a in systemAccounts:
        resign(a, 'eosio')
