start_text = """
Author: [incend1ary](https://t.me/incend1ary) \[Aleksei Seliverstov\]
Source code: [GitHub](https://github.com/1ncend1ary/ams_test_task)

/start \- display this message
/help \- get commands help
/coords long lat \- get a map with marked location
Format: 0 <\= long <\= 67, 0 <\= lat <\= 100
"""

commands_text = """
/start \- display the start message
/help \- get this help
/coords long lat \- get a map with marked location
Format: 0 <\= long <\= 67, 0 <\= lat <\= 100
"""

# this scale is caused by the map image
# being 1600 x 1100
min_w, min_h = 0, 0
max_w, max_h = 100, 67
