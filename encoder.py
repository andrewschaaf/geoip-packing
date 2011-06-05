
from subprocess import check_call
from itertools import islice
from util import freqSorted, runSizes, uvarintWrite


runs = list(runSizes())

# size_id_map
size_id_map = {}
sizes = [size for size, cc in runs]
sizes_sorted = [size for size, count in freqSorted(sizes)]
for i in range(len(sizes_sorted)):
  size_id_map[sizes_sorted[i]] = i

# country_name_id_map
countries = list(set(cc for size, cc in runs))
country_name_id_map = {}
for i in range(len(countries)):
  country_name_id_map[countries[i]] = i


with open('geoip-encoded', 'wb') as f:
  
  # sizes_sorted
  uvarintWrite(f, len(sizes_sorted))
  for size in sizes_sorted:
    uvarintWrite(f, size)
  
  # run sizes
  for size, cc in runs:
    uvarintWrite(f, size_id_map[size])
    f.write(chr(country_name_id_map[cc]))


check_call(['bash', '-c', 'cat geoip-encoded | gzip --stdout - > geoip-encoded.gz'])
check_call(['bash', '-c', 'ls -l | grep geoip'])
