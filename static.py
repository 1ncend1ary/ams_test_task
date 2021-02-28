start_text = r"""
Author: [incend1ary](https://t.me/incend1ary) [Aleksei Seliverstov]
Source code: [GitHub](https://github.com/1ncend1ary/ams_test_task)

/start \- display this message
/help \- get commands help
/coords long lat \- get a map with marked location
Format: integers, 60\.211170 <\= long <\= 60\.220899, 29\.724268 <\= lat <\= 29\.781255
"""

commands_text = r"""
/start \- display the start message
/help \- get this help
/coords long lat \- get a map with marked location
Format: integers, 60\.211170 <\= long <\= 60\.220899, 29\.724268 <\= lat <\= 29\.781255
"""

# this scale is caused by the map image
# being 1600 x 1100
min_w, max_w = 29.724268, 29.781255
min_h, max_h = 60.211170, 60.220899
