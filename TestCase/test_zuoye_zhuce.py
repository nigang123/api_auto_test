from Common import Request, Assert, Tools
import allure
import pytest
phone = Tools.phone_num()
pwd = Tools.random_str_abc(2)+Tools.random_123(4)
rePwd = pwd
userName = Tools.random_str_abc(3)+Tools.random_123(2)
newPwd = pwd+Tools.random_123(1)
oldPwd = pwd
reNewPwd =newPwd
head = {}


request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:1811/'
@allure.feature("注册模块")
class Test_zhuce:
    @allure.story("注册测试")

    def test_zhuce(self):

        req_json = {"phone": phone, 'pwd': pwd, "rePwd":rePwd, "userName": userName,}
        zhuce_resp = request.post_request(url=url + 'user/signup', json=req_json)
        resp_json = zhuce_resp.json()
        assertion.assert_code(zhuce_resp.status_code, 200)
        assertion.assert_in_text(resp_json['respBase'],'成功')

    @allure.story("冻结用户")
    def test_dongjie(self):
        dongjie_resp = request.post_request(url=url + '/user/lock', params={'userName':userName},
                                            headers= {'Content-Type':'application/x-www-form-urlencoded'})

        resp_dict = dongjie_resp.json()
        assertion.assert_code(dongjie_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("解冻用户")
    def test_jiedong(self):
        jiedong_resp = request.post_request(url=url + '/user/unLock', params={'userName': userName},
                                            headers={'Content-Type': 'application/x-www-form-urlencoded'})

        resp_dict = jiedong_resp.json()
        assertion.assert_code(jiedong_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url + 'user/login', json={"pwd":pwd,"userName":userName})
        resp_dict = login_resp.json()
        assertion.assert_code(login_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')


    @allure.story("修改密码")
    def test_xiugai(self):
        xiugai_resp = request.post_request(url=url + '/user/changepwd', json={"newPwd": newPwd, "oldPwd": oldPwd,'reNewPwd':reNewPwd,'userName':userName})
        resp_dict = xiugai_resp.json()
        assertion.assert_code(xiugai_resp.status_code, 200)

        assertion.assert_in_text(resp_dict['respDesc'], '成功')





