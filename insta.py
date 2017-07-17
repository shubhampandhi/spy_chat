# imports
import requests
from locker import own_post,recent_liked,self_info,user_info,user_likes,user_post,del_comment,list_comments,post_comments

# Credentials
app_access_token='---please text me on whatsapp to get the token----'
base_url = 'https://api.instagram.com/v1/'

while True:
    scan = raw_input("\n1. Self information\n2. Other user information\n3. Hash_tag popularity\n4. Exit")
    if scan == '1':
        print "\n------My info :-------\n"
        self_info()
        print "\n----My posts :------\n"
        own_post()
    elif scan == '2':
        user = raw_input("\nEnter username :")
        while True:
            choice = raw_input("\n1. User_info \n2. Like\n3. Comment\n4. Posts \n5. Back")

            if choice == '1':
                print "\n---User info of %s :--\n" % user
                user_info(user)
            elif choice == '2':
                user_likes(user)
            elif choice == '3':
                post_id = user_post(user)

                # Error handling for invalid inputs
                while True:
                    try:
                        index = int(raw_input("Select downloaded post index[1,2,3..] :"))
                        if index>len(post_id):
                            print "Invalid post index no.[1 to %d]" % len(post_id)
                            continue
                    except ValueError:
                        print "Only nos from 1 to %d" % len(post_id)
                        continue
                    except TypeError:
                        print "No posts found"
                        exit()
                    break
                while True:
                    scan = raw_input("\n1. List comments\n2. Add comments\n3. Delete comments\n4. Back")
                    if scan == '1':
                        list_comments(post_id[index - 1])
                    elif scan == '2':
                        post_comments(post_id[index - 1])
                    elif scan == '3':
                        del_comment(post_id[index - 1])
                    elif scan == '4':
                        break
                    else:
                        print "Invalid input"

            elif choice == '4':
                while True:
                    scan = raw_input("\n1. See posts\n2. Recent post\n3. Back")
                    if scan == '1':
                        user_post(user)
                    elif scan == '2':
                        recent_liked(user)
                    elif scan == '3':
                        break
                    else:
                        print "Invalid input"
            elif choice == '5':
                break
            else:
                print "Invalid input"
    elif scan == '3':
        from tag import hash_tag_popularity
        hash_tag_popularity()
    elif scan == '4':
        break
    else:
        print "Have a good day"
        break

