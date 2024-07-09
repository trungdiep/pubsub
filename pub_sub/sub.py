from pub_sub import EventedRedis


sub = EventedRedis(is_sub=True)

sub.subcribe(['ch-1', 'ch-2'])
