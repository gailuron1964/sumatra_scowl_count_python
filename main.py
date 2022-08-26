from sumatra import Client
from env import setup_env

setup_env()
sumatra = Client('console.qa.sumatra.ai')

sumatra.create_branch_from_dir("topology")

sumatra.create_timeline_from_file('attack', 'attack.jsonl')
materialization = sumatra.materialize(timeline='attack')

logins = materialization.get_events("login")
print(logins[['user', 'ip', 'count', 'count_by_ip', 'count_by_ip_user']])
