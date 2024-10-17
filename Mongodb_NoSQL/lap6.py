from pymongo import MongoClient
from datetime import datetime

#b1 conntct db
client = MongoClient('mongodb://localhost:27017/')
client.drop_database("driveManagement")
db = client['driveManagement'] #chon csdl tiktok


files_collection=db['files']

files_data = [
    { 'file_id': 1, 'name': 'Report.pdf', 'size': 2048, 'owner': 'Nguyen Van A', 'created_at': datetime(2024, 1, 10), 'shared': False },
    { 'file_id': 2, 'name': 'Presentation.pptx', 'size': 5120, 'owner': 'Tran Thi B', 'created_at': datetime(2024, 1, 15), 'shared': True },
    { 'file_id': 3, 'name': 'Image.png', 'size': 1024, 'owner': 'Le Van C', 'created_at': datetime(2024, 1, 20), 'shared': False },
    { 'file_id': 4, 'name': 'Spreadsheet.xlsx', 'size': 3072, 'owner': 'Pham Van D', 'created_at': datetime(2024, 1, 25), 'shared': True },
    { 'file_id': 5, 'name': 'Notes.txt', 'size': 512, 'owner': 'Nguyen Thi E', 'created_at': datetime(2024, 1, 30), 'shared': False }

]
files_collection.insert_many(files_data)
# Xem tất cả tệp trong bộ sưu tập 'files'
files_collection.find()
for fl in files_collection.find():
    print(fl)
#Tìm tệp có kích thước lớn hơn 2000KB
sz=files_collection.find({ 'size': { '$gt': 2000 } })
for fl1 in sz:
    print(fl1)
# Đếm tổng số tệp
dem = files_collection.count_documents({})
print(dem)
#Tìm tất cả tệp được chia sẻ
for sh in files_collection.find({'shared': True}):
    print(sh)
#Thống kê số lượng tệp theo chủ sở hữu
for gr in files_collection.aggregate([
    { '$group': { '_id': "$owner", 'count': { '$sum': 1 } } }
]):
    print(gr)
#Cập nhật và xóa thông tin tệp
files_collection.update_one({ 'file_id': 1 }, { '$set': { 'shared': True } })
#Xóa tệp với file_id = 3
files_collection.delete_one({ 'file_id': 3 })
#Tìm tất cả tệp của người dùng có tên là "Nguyen Van A".
for all in files_collection.find({ 'owner': "Nguyen Van A" }):
    print(all)
#Tìm tệp lớn nhất trong bộ sưu tập.
for max in files_collection.find().sort({ 'size': -1 }).limit(1):
    print(max)
#Tìm số lượng tệp có kích thước nhỏ hơn 1000KB.
fmax = files_collection.count_documents({ 'size': {'$lt': 1000 } })
print(fmax)
#Tìm tất cả tệp được tạo trong tháng 1 năm 2024.
for allfile in files_collection.find({
    'created_at': {
        '$gte': datetime(2024,1,1),
        '$lt': datetime(2024,2,1)
    }
}):
    print(allfile)
#Cập nhật tên tệp với `file_id` là 4 thành "New Spreadsheet.xlsx".
files_collection.update_one({ 'file_id': 4 }, { '$set': { 'name': "New Spreadsheet.xlsx" } })
#Xóa tất cả tệp có kích thước nhỏ hơn 1000KB.

files_collection.delete_many({ 'size': { '$lt': 1000 } })

client.close()
