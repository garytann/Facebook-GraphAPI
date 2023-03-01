from secret import access_token, page_id
import requests
from typing import Dict, Any
import pdb 
import asyncio
import time


graph_url = "https://graph.facebook.com/"
# pdb.set_trace()
# post_req = requests.get(graph_url + f"{page_id}" + "/posts" + f"?access_token={access_token}")
# comment_req = requests.get(graph_url + f"v16.0" + f"/{post_id}" + "/comments" + f"?access_token={access_token}")

# comment_res = post_req.json()

async def get_post_ids() -> list:
    post_req = requests.get(graph_url + f"{page_id}" + "/posts" + f"?access_token={access_token}")
    comment_res = post_req.json()
    post_datas = []
    for data in comment_res['data']:
        # post_id = data['id']
        post_datas.append(data)
        # info.append(data['message'])
        # info.append(data['created_time'])
        # if data['id'] in post_dict:
        #     post_dict[post_id].append(data["message"])
        #     # post_dict["date"].append(data['created_time'])
        # else:
        # post_dict[post_id] = data
            # post_dict["date"] = data['created_time']

    return post_datas

# async def process_request(url : str) -> list:
#     req = requests.get(url)
#     comment_res = req.json()
#     results = []
#     pdb.set_trace()
#     # for data in comment_res['data']:

async def get_comment_ids() -> list:
    post_dict : Dict[Any, Any] = {}
    post_info = []

    post_datas = await get_post_ids()
    # comment_post_datas = []
    for post_data in post_datas:
        post_id = post_data['id']
        comment_info = []

        # pdb.set_trace()
        # reaction_req = await process_request(str(graph_url + f"v16.0" + f"/{post_id}" + "/reactions" + f"?access_token={access_token}"))
        # shares_req = requests.get(graph_url + f"v16.0" + f"/{post_id}" + "/sharedposts" + f"?access_token={access_token}")
        comment_req = requests.get(graph_url + f"v16.0" + f"/{post_id}" + "/comments" + f"?access_token={access_token}")
        comment_res = comment_req.json()
        
        for data in comment_res['data']:
            comment_dict : Dict[Any, Any] = {}
            likes_req = requests.get(graph_url + f"v16.0" + f"/{data['id']}" + "/likes" + f"?access_token={access_token}")
            likes_res = likes_req.json()
            comment_dict = {
                "id": data['id'],
                "comment_hyperlink":f"www.facebook.com/{data['id']}",
                "comment_date":f"{data['created_time']}",
                "content":f"{data['message']}",
                "author_name": f"{data['from']['name']}",
                # "user_hyperlink":f"www.facebook.com/{data['from']['name']}",
                "likes": len(likes_res['data'])
            }
            # comment_id = data['id']
            # author_name = data['from']['name']
            comment_info.append(comment_dict)
            
        import time
        start = time.time()
        sort_by_reaction = sorted(
            comment_info,
            key=lambda e: (e["likes"]),
            reverse=True,
        )
        end = (time.time() - start)
        print(f'time taken {end}')

        post_dict = {
                "id": post_id,
                "official_post_hyperlink": f"www.facebook.com/{post_id}",
                "date": f"{post_data['created_time']}",
                "post_content": f"{post_data['message']}",
                "hot_reply_comment": sort_by_reaction[0]['content'],
                "hot_reply_hyperlink": sort_by_reaction[0]['comment_hyperlink']
            }
        post_info.append(post_dict)
    

    return (post_info,comment_info)

# async def get_post_info():
#     post_info = []
#     post_datas = await get_post_ids()
#     comment_info = await get_comment_ids()
#     sort_by_reaction = sorted(
#                 comment_info,
#                 key=lambda e: (e["likes"]),
#                 reverse=True,
#             )
#     for post_data in post_datas:
#         # post_dict = {
#                 #         "id": post_id,
#                 #         "official_post_hyperlink": f"www.facebook.com/{post_id}",
#                 #         "date": f"{post_data['created_time']}",
#                 #         "post_content": f"{post_data['message']}",
#                 #         "hot_reply_comment": sort_by_reaction[0]['content'],
#                 #         "hot_reply_hyperlink": sort_by_reaction[0]['comment_hyperlink']
#                 #     }
#     # post_info.append(post_dict)

# # out = await get_info()
# print(out)
while (True):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print("Running crawler now...")
    post_result, comment_result = loop.run_until_complete(get_comment_ids())
    print(f'post_result {post_result} + \n + comment_result {comment_result}')
    print("Finished crawling the website. Waiting for the next cycle..")
    time.sleep(5)
