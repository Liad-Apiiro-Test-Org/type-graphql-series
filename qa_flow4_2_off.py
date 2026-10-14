# QA LIM-43609 Flow 4.2 marker: OFF tier target
import Crypto.Hash.MD4


def off_tier_digest(payload):
    return Crypto.Hash.MD4.new(payload).hexdigest()
