

a = {'_sa_instance_state': '<sqlalchemy.orm.state.InstanceState object at 0x107a3d9a0>', 'rclone_protocol': 'https', 'id': 2, 'rclone_username': 'user', 'backup_status': None, 'url': 'landslide-bud.ctf.in.pan-net.eu', 'rclone_port': 5572, 'name': 'tas-bud', 'rclone_password': 'password'}
result = {i: a[i] for i in a if i[0] != '_' }
#rewrite this above line in terms of key/value
# result = {key: hash[key] for i in hash if key[0] != '_'}
# {'rclone_protocol': 'https', 'id': 2, 'rclone_username': 'user', 'backup_status': None, 'url': 'landslide-bud.ctf.in.pan-net.eu', 'rclone_port': 5572, 'name': 'tas-bud', 'rclone_password': 'password'}
print(result)

print('')
hash = {'first': 1, 'fruit': 'banana', 'temp_of_Vltava': 5.2, 'languages': ['english', 'spanish', 'hindi']}
print(hash)
result = {i: hash[i] for i in hash if i == 'languages'}
print(result)

print('')
for i in hash:
  print(i, hash[i])

print('')
a = [1,2,3,4]
print([_ for _ in a])

h = {one: 1, two: 2, three: 3}
h.each { |_, value| print value * 100 }


