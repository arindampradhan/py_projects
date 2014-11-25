from bs4 import BeautifulSoup
import requests
import re
import urlparse

# URL = "http://www.producthunt.com/"	

# page = requests.get(URL).text 

# soup = BeautifulSoup(page)

# posts_html = soup.find('div',id="posts-wrapper").find('div',class_="posts")

# days = posts_html.find_all('div',class_=re.compile(r'(day|day today)'))




# DAY SCRAPING
# ============
# d = []

# for day in days:
# 	# print day.find('time')
# 	d.append(day.find('time')['datetime'])
	

# print d

# # PRODUCT SCRAPING
# ===================

# post = posts_html.find_all('li',class_=re.compile(r'(post hidden-post|post)'))

# upvotes = []
# urls = []
# names = []
# descriptions = []
# dates = []
# users = []
# ids =[]

# for product in post:
# 	upvote = int(product.find('span', class_="vote-count").string)
# 	date = product.find_parent("div",class_=re.compile(r'(day today|day)')).time['datetime']
# 	prod = product.find('div',class_="url")
# 	url  = prod.a['href']
# 	url = urlparse.urljoin(URL,url)
# 	name = prod.a.string
# 	description = prod.find('span', class_="post-tagline description").string
# 	user = product.find('div', class_="user-hover-card").h3.string
# 	id = product.find('a', class_="view-discussion")['data-id']
# 	# appending
# 	upvotes.append(upvote)
# 	urls.append(url)
# 	names.append(name)
# 	descriptions.append(description)
# 	users.append(user)
# 	ids.append(id)
# 	dates.append(date)


# print ids















# ## DISCUSSON SCRAPER
# # ==================
# # url at -> URL + posts + id + ?model=true

# ## GETTING COMMENTS 

# ex_url = "http://www.producthunt.com/posts/archively?modal=true"

# c_page = requests.get(ex_url).text

# c_soup = BeautifulSoup(c_page)

# c_soup.find('div',class_="post_show")

# post_show = c_soup.find('div',class_="post-show")


# ## comment group id = who started comment = class_ = comment =/= comment child(child do not have the same comment)

# num_comment = post_show.find('h2', class_="subhead")

# c_upvotes = []
# c_ids = []
# c_flags = [] # true if comment id == parent id
# c_users= []
# c_comments = []

# comment_html = post_show.find_all('div',class_= re.compile(r'^(comment|comment child)$'))

# #regex for comment extraction compile outside for faster for loop
# regex = re.compile(r"<a.*?</a>", re.IGNORECASE)
# reg_div = re.compile(r"(?s)<div(?: [^>]*)?>(.*?)<\/div>")

# for comment in comment_html:
# 	c_upvote = comment.find('span',class_="vote-count").string
# 	c_id = comment['data-comment-id']
# 	p_id = comment.find_parent('div',class_="comment-thread")['data-parent-id'] # parent id
# 	c_flag = (c_id == p_id)
# 	#getting comment using regex
# 	c_comment = str(comment.find('div',class_="actual-comment"))
# 	c_comment = str(regex.sub("",c_comment))
# 	c_comment = str(reg_div.findall(c_comment)[0])
# 	c_user = comment.find('h2', class_="comment-user-name").a.string
# 	# appending
# 	c_upvotes.append(c_upvote)	
# 	c_ids.append(c_id)
# 	c_flags.append(c_flag)
# 	c_users.append(c_user)
# 	c_comments.append(c_comment)



# print len(c_comments)
# # print len(c_upvotes)
# # print len(c_ids)
# # print len(c_users)





# USER SCRAPING
# http://www.producthunt.com/ashbhoopathy or http://www.producthunt.com/3

# TAG_RE = re.compile(r'<[^>]+>')
# def remove_tags(text):
#     return TAG_RE.sub('', text)



# u_url = "http://www.producthunt.com/3"
# u_page = requests.get(u_url).text
# u_soup = BeautifulSoup(u_page)
# u_soup = u_soup.find('div',class_="main-content")




# user = u_soup.find("h1",class_="page-header--title")
# user_text =  remove_tags(str(user))


# user_id = int(user_text.split("#")[1])
# user_name = user_text.split("#")[0]



# nav = u_soup.find('nav',class_="page-header--navigation")
# upvote_u = nav.find_all('strong')

# u_num_upvote = int(upvote_u[0].string)
# u_num_submit = int(upvote_u[1].string)
# u_num_made = int(upvote_u[2].string)
# u_num_followers = int(upvote_u[3].string)
# u_num_following = int(upvote_u[4].string)





# All info about his statistics

# def get_vote_id(url):
# 	# applicable
# 	# http://www.producthunt.com/ashbhoopathy ## == upvoted
# 	# http://www.producthunt.com/ashbhoopathy/posts ## == submitted
# 	# http://www.producthunt.com/ashbhoopathy/products ## == products
# 	# per page 50
# 	# num_page * 50 + this code

# 	page_count=1
# 	data_ids = []
# 	while 1:
# 		current_page = requests.get(url+"?page="+str(page_count)).text
# 		soup  = BeautifulSoup(current_page)
# 		post_group = soup.find('ul',class_="posts-group")
# 		post_list = post_group.find_all('li',class_="post")
# 		for pst in post_list:
# 			data_id = pst.find('div',class_="upvote")['data-vote-id']
# 			data_ids.append(data_id)
# 		page_count = page_count+1
# 		if len(soup.find_all('li', class_="post")) is 0:
# 			break
# 		# t = t-1
# 		# if t < 1:break
# 	return data_ids


# def follow_id(url):	
# 	# http://www.producthunt.com/ashbhoopathy/followers ## == followers
# 	# http://www.producthunt.com/ashbhoopathy/followings ## == following
# 	# per page 50
# 	page_count=1
# 	follow_ids = []
# 	while 1:
# 		current_page = requests.get(url+"?page="+str(page_count)).text
# 		soup  = BeautifulSoup(current_page)
# 		follow_group = soup.find_all("li", class_="people--person")
		
# 		for follow in follow_group:
# 			follow_id = follow.find('div', class_="user-hover-card").find('a', class_="button")['data-follow-id']
# 			follow_ids.append(follow_id)
# 		page_count = page_count+1
# 		if len(soup.find('ul', class_="people").find_all('li',class_='people--person'))  == 0:
# 			break
# 	return follow_ids

