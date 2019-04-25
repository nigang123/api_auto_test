from Common import Request, Assert, read_excel
import allure
import pytest
yhq_id = 0
idsList=[]

request = Request.Request()
assertion = Assert.Assertions()

excel_list = read_excel.read_excel_list('../document/优惠券.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:8080/'
head = {}
@allure.feature("优惠券模块")
class Test_yhq:
    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url + 'admin/login',
                                          json={"username": "admin", "password": "123456"})

        resp_text = login_resp.text
        print(type(resp_text))

        resp_dict = login_resp.json()

        print(type(resp_dict))

        assertion.assert_code(login_resp.status_code, 200)

        assertion.assert_in_text(resp_dict['message'], '成功')

        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head = {'Authorization': tokenHead + token}

    @allure.story("添加优惠券")
    @pytest.mark.parametrize('amount,minPoint,name,publishCount,msg',excel_list, ids=idsList)
    def test_add_yhq_list(self,amount,minPoint,name,publishCount,msg):
        req_json = {"type":0,"name":name,"platform":0,"amount":amount,"perLimit":1,"minPoint":minPoint,"startTime":'',"endTime":'',"useType":0,"note":'',"publishCount":publishCount,"productRelationList":[],"productCategoryRelationList":[]}
        add_yhq_resp = request.post_request(url=url + 'coupon/create',
                                            json=req_json, headers=head)
        resp_json = add_yhq_resp.json()
        assertion.assert_code(add_yhq_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], msg)

    @allure.story("获取优惠券信息")
    def test_yhq(self):
        param = {'pageNum': 1, 'pageSize':10}
        get_yhq_resp = request.get_request(url=url + 'coupon/list', params=param, headers=head)
        resp_json = get_yhq_resp.json()
        assertion.assert_code(get_yhq_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global yhq_id
        yhq_id = item['id']

    @allure.story("删除优惠券信息")
    def test_del_yhq(self):

        post_yhq_resp = request.post_request(url=url + 'coupon/delete/'+str(yhq_id), headers=head)
        resp_json = post_yhq_resp.json()
        assertion.assert_code(post_yhq_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
