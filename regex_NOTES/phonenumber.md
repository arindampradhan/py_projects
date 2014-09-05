Number types :
==============

• 800-555-1212 phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
• 800 555 1212
• 800.555.1212
• (800) 555-1212
• 1-800-555-1212
• 800-555-1212-1234 phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
• 800-555-1212x1234 phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
	|----solving for the special characters in between the numbers.
• 800-555-1212 ext. 1234 phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
• work 1-(800) 555.1212 #1234 phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
	|----1- is not required for the area code so we eliminate \D* at beginning


^ start
$ end 
\d{3 digits} 
\D non digits
+ one or more 
* 0 or more








