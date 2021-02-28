start_text = """
Author: [incend1ary](https://t.me/incend1ary) \[Aleksei Seliverstov\]
Source code: [GitHub](https://github.com/1ncend1ary/ams_test_task)

/start \- display this message
/help \- get commands help
/coords long lat \- get a map with marked location
Format: integers, 0 <\= long <\= 67, 0 <\= lat <\= 100
"""

commands_text = """
/start \- display the start message
/help \- get this help
/coords long lat \- get a map with marked location
Format: integers, 0 <\= long <\= 67, 0 <\= lat <\= 100
"""

# this scale is caused by the map image
# being 1600 x 1100
min_w, max_w = 29.724268, 29.781255
min_h, max_h = 60.211170, 60.220899
