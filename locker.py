import requests
base_url = 'https://api.instagram.com/v1/'
app_access_token='---text me on whatsapp---'

# Informtion about the owner of the token
def self_info():
    request_url = (base_url + 'users/self/?access_token=%s') % app_access_token
    print "\n---Loading ----"
    r = requests.get(request_url).json()
    if r['meta']['code'] == 200:
        if len(r['data']):
            print "User Id : %s" % r['data']['id']
            print "Username : %s" % r['data']['username']
            print "Followers : %s" % r['data']['counts']['follows']
            print "Followed by : %s" % r['data']['counts']['followed_by']
        else:
            print "User doesnot exist"
    else:
        print "Error code :", r['meta']['code']

# Get id of a user
def id(username):
    request_url = (base_url + 'users/search?q=%s&access_token=%s')%(username,app_access_token)
    print "\n---Loading---"
    r = requests.get(request_url).json()
    if r['meta']['code']==200:
        if len(r['data']):
            return r['data'][0]['id']
        else:
            print "user doesnot exist"
            return 0
    else:
        print "Error code : %s" % r['meta']['code']

# Get recent posts of an user and return its post id
def user_post(username):
    user_id = id(username)
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    raw = requests.get(request_url).json()
    from urllib import urlretrieve
    i = 1
    id_s = []

    if raw['meta']['code'] == 200:
        if len(raw['data'])!=0:
            from f import filt    # Importing filter
            posts = filt(raw)
            if posts!=0:
                for temp in posts:
                    name = temp['id'] + '.jpg'
                    url = temp['images']['standard_resolution']['url']
                    urlretrieve(url, name)
                    print "Downloaded post (%d): File name :%s" % (i,name)

                    # For portability of displaying on various systems
                    import os
                    try:
                        os.system('display -delay 5 /root/PycharmProjects/how_to/%s' % name)
                    except:
                        break
                    id_s.append(temp['id'])
                    i = i + 1


                id_s.append(raw)  # json data appended in the end of the post id list
                return id_s

            else:
                print "No post found"
                return 0
        else:
            print "User doesnot exist"
            return 0
    else:
        print "Error code :%s" % raw['meta']['code']
        return 0

# List comments of a specific post
def list_comments(post_id):
    request_url = (base_url + 'media/%s/comments/?access_token=%s') % (post_id,app_access_token)
    print "\n---Loading---"
    raw = requests.get(request_url).json()
    if raw['meta']['code']==200:
        if len(raw['data']):
            print "\nComment on post_id :%s\n" % post_id
            for temp in raw['data']:
                print "[%s]  :  [id :%s]"%(temp['text'],temp['id'])
        else:
            print "No comments"
    else:
        print "Error code :%s" % raw['meta']['code']

# Add comment on a particular post
def post_comments(post_id):
    request_url = (base_url + 'media/%s/comments') % post_id
    while True:
        comment = raw_input("\nEnter the comment :")
        if len(comment)>300:
            print "Comment too long. Re-enter"
        else:
            break
    payload = {'access_token':app_access_token,'text':comment}
    raw = requests.post(request_url,payload).json()
    print "\n---Commenting----"
    if raw['meta']['code']==200:
        print "\nComment added "
    else:
        print "Error code :%s" % raw['meta']['code']

# Delete comment of a specific post
def del_comment(post_id):
    i = raw_input("\nEnter the id of the comment to be deleted")

    request_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % (post_id,i,app_access_token)
    print "\n---Deleting comment---"
    raw = requests.delete(request_url).json()
    if raw['meta']['code']==200:
        print "Comment deleted"
    else:
        print "Error code :%s" % raw['meta']['code']

# Recent post liked by a user
def recent_liked(username):
    post_id = user_post(username)
    a = post_id[-1]
    for temp in a['data']:
        if temp!=None and temp['user_has_liked']!=None:
            if temp['user_has_liked'] == True:
                print "File name(recently liked) :%s.jpg" % temp['id']
                return temp['id']
    print "No media liked by the user in the filtered post"

# Get info about a user
def user_info(username):
    user_id = id(username)
    request_url = (base_url + 'users/%s?access_token=%s') % (user_id,app_access_token)
    raw = requests.get(request_url).json()
    if raw['meta']['code']==200:
        if len(raw['data']):
            print "User_id :%s" % raw['data']['id']
            print "Profile_pic :%s" % raw['data']['profile_picture']
            print "Followers :%s" % raw['data']['counts']['follows']
            print "Followed by :%s" % raw['data']['counts']['followed_by']
        else:
            print "User does not exist"
    else:
        print "Error code :%s" % raw['meta']['code']

# Get list of likes on a post,set like on a post and remove like from a post
def user_likes(username):
    post_id = user_post(username)
    # Error handling for invalid inputs
    while True:
        try:
            index = int(raw_input("Select post index[1,2,3...] :"))
            if index>len(post_id):
                print "Invalid post id"
                continue
        except ValueError:
            print "Only nos :"
            continue
        except TypeError:
            print "No post found"
            exit()
        break
    while True:
        request_url = (base_url + 'media/%s/likes/?access_token=%s') % (post_id[index - 1], app_access_token)
        print "1. Get list of users who liked this post"
        print "2. Set a like on the post"
        print "3. Remove the like from the post"
        print "4. Back"
        choice = raw_input("Select :")
        print "\n"
        if choice == '1':
            raw = requests.get(request_url).json()
            if raw['meta']['code'] == 200:
                if len(raw['data']):
                    for temp in raw['data']:
                        print "Username :%s" % temp['username']
                    print "\n"
                else:
                    print "No one liked the post"
            else:
                print "Error code : %s" % raw['meta']['code']
        elif choice == '2':
            req_url = (base_url + 'media/%s/likes') % post_id[index-1]
            payload = {'access_token': app_access_token}
            raw = requests.post(req_url, payload).json()
            if raw['meta']['code'] == 200:
                print "\nPost liked\n"
            else:
                print "Error code :%s" % raw['meta']['code']
        elif choice == '3':
            raw = requests.delete(request_url).json()
            if raw['meta']['code'] == 200:
                print "\nLike removed\n"
            else:
                print "Error code :%s" % raw['meta']['code']
        elif choice== '4':
            break
        else:
            print "Invalid input"

# Fetch recent posts of the owner of the token
def own_post():
    count = int(raw_input("No of posts you want to see ?"))
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % app_access_token
    raw = requests.get(request_url).json()
    id_s = []
    if raw['meta']['code']==200:
        if len(raw['data']):
            for temp in raw['data']:
                if count==0:
                    break

                name = temp['id'] + '.jpg'
                url = temp['images']['standard_resolution']['url']
                from urllib import urlretrieve
                urlretrieve(url, name)                         # Downloading
                print "Downloaded post :%s"%temp['id']
                import os
                os.system('display -delay 5 /root/PycharmProjects/how_to/%s' % name)
                id_s.append(temp['id'])
                count = count - 1
            return id_s

        else:
            print "Post doesnot exist"
    else:
        print "Error code :%s" % raw['meta']['code']


