# Main network and testnet3 definitions

# momo src/chainparams.cpp
params = {
    'momo_main': {
        'pubkey_address': 30, #L120
        'script_address': 16, #L122
        'genesis_hash': '00000f79a81b6318e0f36dc486adf4bb5bb1fa34025d69b991893c42978c2027' #L110
    },
    'momo_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000f79a81b6318e0f36dc486adf4bb5bb1fa34025d69b991893c42978c2027' #L210
    }
}
