from pub_sub import EventedRedis

pub = EventedRedis(port=36379)

pub.publish('ch-1', 'test')
