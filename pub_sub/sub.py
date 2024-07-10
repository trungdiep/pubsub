from pub_sub import EventedRedis


sub = EventedRedis(port=36379, is_sub=True)

sub.subcribe(['ch-1', 'ch-2'])

sub.handle()
