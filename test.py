tag_list = ['น้ำตก','ธรรมชาติ','เขา']
date_list = [
    {
        'name':'บทความการเที่ยงเที่ยว1',
        'author':'Kong1',
        'tags':tag_list
    },
    {
        'name':'บทความการเที่ยงเที่ยว2',
        'author':'Kong2',
        'tags':tag_list
    }
]
# for i in range(len(date_list)):
#     print('name',date_list[i]['name'])
#     print('author',date_list[i]['author'])
#     print('tags')
#     for x in range(len(date_list[i]['tags'])):
#         print(date_list[i]['tags'][x])
for i in date_list:
    print(i['name'])
    print(i['author'])
    print('tags')
    for x in i['tags']:
        print(x)