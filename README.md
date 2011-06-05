
An exploratory encoding for [Tor Ticket #2506: Design and implement a more compact GeoIP file format](https://trac.torproject.org/projects/tor/ticket/2506)

## Encoding

uvarint: [same as Protobuf's](http://code.google.com/apis/protocolbuffers/docs/encoding.html#varints)

<pre>

write uvarint(run_sizes_by_freq.length)
for size in run_sizes_by_freq
  write uvarint(size)

for size, country in runs:
  write uvarint(size_mapping[size])
  write uint8(country_mapping[country])

</pre>

Note: gaps between runs are considered to be runs with a country code of "".

Note: the <code>(Country or null) &rarr; uint8</code> mapping is not currently included in the encoding. Should it be, or does Tor already have such a mapping?


## Results
<pre>
  317,108 bytes: geoip-encoded
  205,123 bytes: geoip-encoded.gz
3,645,222 bytes: geoip.txt
</pre>

