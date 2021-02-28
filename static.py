start_text = r"""
Author: [incend1ary](https://t.me/incend1ary) [Aleksei Seliverstov]
Source code: [GitHub](https://github.com/1ncend1ary/ams_test_task)

/start \- display this message
/help \- get commands help
/coords long lat (or send geolocation) \- get a map with marked location
Format: integers, 60\.211170 <\= lat <\= 60\.220899, 29\.724268 <\= long <\= 29\.781255
This map has been marked up on [georeferencer](https://www.georeferencer.com/maps/37588bfc-98fd-47db-a234-09a80b4e2afd/view#947132469025)
"""

commands_text = r"""
/start \- display the start message
/help \- get this help
/coords long lat (or send geolocation) \- get a map with marked location
Format: integers, 60\.211170 <\= lat <\= 60\.220899, 29\.724268 <\= long <\= 29\.781255
This map has been marked up on [georeferencer](https://www.georeferencer.com/maps/37588bfc-98fd-47db-a234-09a80b4e2afd/view#947132469025)
"""

# this scale is caused by the map image
# being 1600 x 1100
min_w, max_w = 29.724268, 29.781255
min_h, max_h = 60.211170, 60.220899
