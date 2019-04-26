# from Common import Request, Assert, read_excel,login
# import allure
# import pytest
# request = Request.Request()
# assertion = Assert.Assertions()
# url = 'http://192.168.1.137:8080/'
# head = {}
# th_id = 0
# idsList=[]
# excel_list = read_excel.read_excel_list('./document/退货.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())
#
# @allure.feature("退货模块")
# class Test_th:
#     @allure.story("获取退货信息")
#     def test_th(self):
#         get_th_resp = request.get_request(url=url + 'returnReason/list', params={'pageNum':1,'pageSize':5}, headers=head)
#         resp_json = get_th_resp.json()
#         assertion.assert_code(get_th_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'], '成功')
#         json_data = resp_json['data']
#         data_list = json_data['list']
#         item = data_list[0]
#         global th_id
#         th_id = item['id']
#
#     @allure.story("删除退货信息")
#     def test_sc_th(self):
#         post_sc_th_resp = request.post_request(url=url + 'returnReason/delete?ids=' + str(th_id), headers=head)
#         resp_json = post_sc_th_resp.json()
#         assertion.assert_code(post_sc_th_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'], '成功')
#
#     @allure.story("添加退货信息")
#     @pytest.mark.parametrize('name,sort,status,msg',excel_list, ids=idsList)
#     def test_add_th_list(self, name, sort, status,  msg):
#         req_json = {'name': '', 'sort': 0, 'status': 1 }
#         add_th_resp = request.post_request(url=url + 'returnReason/create',
#                                             json=req_json, headers=head)
#         resp_json = add_th_resp.json()
#         assertion.assert_code(add_th_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'], msg)
