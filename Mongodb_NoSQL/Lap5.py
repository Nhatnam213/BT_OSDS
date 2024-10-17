from pymongo import MongoClient
from datetime import datetime
#b1.Conact db
client = MongoClient('mongodb://localhost:27017/')
client.drop_database("facebookData1")
db = client['facebookData1'] #chon csdl tiktok

users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']

users_data= [
    { 'user_id': 1, 'name': "Nguyen Van A", 'name': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'name': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'name': "c@gmail.com", 'age': 22 }
]
users_collection.insert_many(users_data)

posts_data= [
    { 'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': datetime(2024,10,1) },
    { 'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': datetime(2024,10,2) },
    { 'post_id': 3, 'user_id': 3, 'content' :"Chúc mọi người một ngày tốt lành!", 'created_at': datetime(2024,10,3) }
]
posts_collection.insert_many(posts_data)

comments_data=[
    { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024,10,1) },
    { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024,10,2) },
    { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024,10,3) }
]
comments_collection.insert_many(comments_data)
# Tim tat ca nguoi dung
# user = users_collection.find()
# for users in user:
#     print(users)

#Xem tat ca bai dang cua nguoi dung voi user_id =1
# com = comments_collection.find({'post_id':1})
# for cm in com:
#     print(cm)
# Xem tất cả bình luận cho bài đăng với post_id = 1
# po = posts_collection.find({'post_id':1})
# for p in po:
#     print(p)
#Truy vấn người dùng có độ tuổi trên 25
# us = users_collection.find({'age': {'$gt':25} })
# for uss in us:
#     print(uss)
#Truy vấn tất cả bài đăng được tạo trong tháng 10
# post= posts_collection.find({'created_at': {'$gte': datetime(2024,10,1), '$lt': datetime(2024,11,1) } })
# for ps in post:
#     print(ps)
#Cập nhật nội dung bài đăng của người dùng với post_id = 1

# posts_collection.update_one({ 'post_id': 1 }, { '$set': { 'content': "Hôm nay thời tiết thật đẹp!" } })
# for poss in posts_collection.find():
#     print(poss)
#Xóa bình luận với comment_id = 2
# comments_collection.delete_one({'comment_id': 2 })
# for cmmmmm in comments_collection.find():
#     print(cmmmmm)
#Xem lại tất cả bài đăng
# pos = posts_collection.find()
# for po in pos:
#     print(po)
#xem lai tat ca binh luan
# bl = comments_collection.find()
# for cmmmm in bl:
#     print(cmmmm)


client.close()
