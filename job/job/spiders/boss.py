import scrapy
import logging
from job.items import JobItem

# git@github.com:Thm-lab/Big-data-service-platform-for-professional-ability.git
class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    prefix_url = 'https://www.zhipin.com'
    start_urls = ['http://www.zhipin.com/']

    def __init__(self, name=None, **kwargs):
        self.keyword_list = ['数据分析', 'java工程师', '前端开发', '数据库开发', '律师', '前台', '家政', '架构师', '爬虫']
        self.now_keyword_index = 0
        self.url = 'https://www.zhipin.com/web/geek/job?query={keyword}&city={city}&page={pageNo}'
        self.now_page = 1
        self.fail_count = 0
        temps = [
            'lastCity=101270100; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=c843f3ee-3a64-4dcc-b0bf-48177684fa34; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656726422; wd_guid=2549f028-f6cf-40dc-9c1a-056bc8dd39ad; historyState=state; _bl_uid=64ldw5t33qk8U061b0q9jnvvIg9e; wt2=DAm6_KxehzgZXwi2JTgeuiJZb-_dg7x4eyR5i1crL6pcu_D3j5_jdkGHlmhXY_Xp7kKXEHGwiJaR1iqQJzRIChg~~; wbg=0; acw_tc=0b32974616568249774502511e010d7668a5afb22d0fd9aa38b392817021c4; __l=r=https://www.baidu.com/other.php?sc.0600000-R26gd0oAcI5NneYCIF4gpK6x9_OQTaPpn4WQfxTyx3AvXBDYeeJXZf7NBTE-r0DmLpNeYhArfHFhziOKWokFDcGOku_Cn8NSR7O9FJu78_6fMXJt1OCdO1BCMvVVTOXdowl3x0kdfQIys654n1C51S8LKlxh3Jusx6oKmkRDCo0_9xexiSuTvF_VvyG08scsWFQu4kjGsxYao9pjsasE.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1TsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujdBULP10ZFWIWYs0ZNzU7qGujYkPHnvrj64P1fs0Addgv-b5HDYPWcsnWD10AdxpyfqnHDvnWn1PHn0UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dcfbD0TA-b5Hc30APGujYznWm0mLFW5HnsnjDk&dt=1656726418&wd=boss&tpl=tpl_12826_27888_0&l=1536889740&us=linkVersion%3D1%26compPath%3D10036.0-10032.0%26label%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkType%3D%26linkText%3DBOSS%25E7%259B%25B4%25E8%2581%2598%25E2%2580%2594%25E2%2580%2594%25E6%2589%25BE%25E5%25B7%25A5%25E4%25BD%259C%25EF%25BC%258C%25E4%25B8%258ABOSS%25E7%259B%25B4%25E8%2581%2598%25EF%25BC%258C&l=/www.zhipin.com/web/geek/job?query=&city=101270100&position=100120&s=3&g=/www.zhipin.com/chengdu/?sid=sem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; geek_zp_token=V1RN4hF-b92F1vVtRvyhsQKy2y5TnfxCo~; __zp_stoken__=05e7dGkkUfmxNGh4VBhA4NhpVWQh3dXpVYiAGb2h8bgxLAGh2PXYhAGonAFhXejchLUx+A1Z7WRk6fhc8HXo9MngUBhIOUExcSmRqcyMOamBwKzo7RFMJKBVfdnp1FBhqb3VMfSQAVGRtOkU=; __c=1656726422; __a=37250023.1656726422..1656726422.23.1.23.23; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1656825755',
            'lastCity=101270100; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=c843f3ee-3a64-4dcc-b0bf-48177684fa34; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656726422; wd_guid=2549f028-f6cf-40dc-9c1a-056bc8dd39ad; historyState=state; _bl_uid=64ldw5t33qk8U061b0q9jnvvIg9e; wt2=DAm6_KxehzgZXwi2JTgeuiJZb-_dg7x4eyR5i1crL6pcu_D3j5_jdkGHlmhXY_Xp7kKXEHGwiJaR1iqQJzRIChg~~; wbg=0; acw_tc=0b32974616568249774502511e010d7668a5afb22d0fd9aa38b392817021c4; __zp_stoken__=05e7dGkkUfmxNGh4VBhA4NhpVWQh3dXpVYiAGb2h8bgxLAGh2PXYhAGonAFhXejchLUx+A1Z7WRk6fhc8HXo9MngUBhIOUExcSmRqcyMOamBwKzo7RFMJKBVfdnp1FBhqb3VMfSQAVGRtOkU=; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1656825755; __c=1656726422; __l=r=https://www.baidu.com/other.php?sc.0600000-R26gd0oAcI5NneYCIF4gpK6x9_OQTaPpn4WQfxTyx3AvXBDYeeJXZf7NBTE-r0DmLpNeYhArfHFhziOKWokFDcGOku_Cn8NSR7O9FJu78_6fMXJt1OCdO1BCMvVVTOXdowl3x0kdfQIys654n1C51S8LKlxh3Jusx6oKmkRDCo0_9xexiSuTvF_VvyG08scsWFQu4kjGsxYao9pjsasE.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1TsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujdBULP10ZFWIWYs0ZNzU7qGujYkPHnvrj64P1fs0Addgv-b5HDYPWcsnWD10AdxpyfqnHDvnWn1PHn0UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dcfbD0TA-b5Hc30APGujYznWm0mLFW5HnsnjDk&dt=1656726418&wd=boss&tpl=tpl_12826_27888_0&l=1536889740&us=linkVersion%3D1%26compPath%3D10036.0-10032.0%26label%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkType%3D%26linkText%3DBOSS%25E7%259B%25B4%25E8%2581%2598%25E2%2580%2594%25E2%2580%2594%25E6%2589%25BE%25E5%25B7%25A5%25E4%25BD%259C%25EF%25BC%258C%25E4%25B8%258ABOSS%25E7%259B%25B4%25E8%2581%2598%25EF%25BC%258C&l=/www.zhipin.com/web/geek/job?query=&city=101270100&position=100120&s=3&g=/www.zhipin.com/chengdu/?sid=sem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; __a=37250023.1656726422..1656726422.24.1.24.24; geek_zp_token=V1RN4hF-b92F1vVtRvyhsQKy207z_RzSg~',
            'lastCity=101270100; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=c843f3ee-3a64-4dcc-b0bf-48177684fa34; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656726422; wd_guid=2549f028-f6cf-40dc-9c1a-056bc8dd39ad; historyState=state; _bl_uid=64ldw5t33qk8U061b0q9jnvvIg9e; wt2=DAm6_KxehzgZXwi2JTgeuiJZb-_dg7x4eyR5i1crL6pcu_D3j5_jdkGHlmhXY_Xp7kKXEHGwiJaR1iqQJzRIChg~~; wbg=0; acw_tc=0b32974616568249774502511e010d7668a5afb22d0fd9aa38b392817021c4; __zp_stoken__=05e7dGkkUfmxNGh4VBhA4NhpVWQh3dXpVYiAGb2h8bgxLAGh2PXYhAGonAFhXejchLUx+A1Z7WRk6fhc8HXo9MngUBhIOUExcSmRqcyMOamBwKzo7RFMJKBVfdnp1FBhqb3VMfSQAVGRtOkU=; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1656825755; __c=1656726422; __l=r=https://www.baidu.com/other.php?sc.0600000-R26gd0oAcI5NneYCIF4gpK6x9_OQTaPpn4WQfxTyx3AvXBDYeeJXZf7NBTE-r0DmLpNeYhArfHFhziOKWokFDcGOku_Cn8NSR7O9FJu78_6fMXJt1OCdO1BCMvVVTOXdowl3x0kdfQIys654n1C51S8LKlxh3Jusx6oKmkRDCo0_9xexiSuTvF_VvyG08scsWFQu4kjGsxYao9pjsasE.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1TsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujdBULP10ZFWIWYs0ZNzU7qGujYkPHnvrj64P1fs0Addgv-b5HDYPWcsnWD10AdxpyfqnHDvnWn1PHn0UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dcfbD0TA-b5Hc30APGujYznWm0mLFW5HnsnjDk&dt=1656726418&wd=boss&tpl=tpl_12826_27888_0&l=1536889740&us=linkVersion%3D1%26compPath%3D10036.0-10032.0%26label%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkType%3D%26linkText%3DBOSS%25E7%259B%25B4%25E8%2581%2598%25E2%2580%2594%25E2%2580%2594%25E6%2589%25BE%25E5%25B7%25A5%25E4%25BD%259C%25EF%25BC%258C%25E4%25B8%258ABOSS%25E7%259B%25B4%25E8%2581%2598%25EF%25BC%258C&l=/www.zhipin.com/web/geek/job?query=&city=101270100&position=100120&s=3&g=/www.zhipin.com/chengdu/?sid=sem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; __a=37250023.1656726422..1656726422.25.1.25.25; geek_zp_token=V1RN4hF-b92F1vVtRvyhsQKy216zrRwyw~']
        self.cookies = []
        for temp in temps:
            self.cookies.append({data.split('=')[0]: data.split('=')[-1] for data in temp.split('; ')})
        self.cookie_index = 0
        super().__init__(name, **kwargs)

    def start_requests(self):
        yield scrapy.Request(
            self.url.format(pageNo=self.now_page, keyword=self.keyword_list[self.now_keyword_index], city=101270100),
            callback=self.parse,
            cookies=self.cookies[self.cookie_index])

    def parse(self, response):
        global degree
        global company_persion
        html = open('page.html', 'wb')
        html.write(response.body)
        html.close()

        item = JobItem()
        # if bool(response.xpath("//div[@class='job-list']")) == False:
        #     logging.info('cookie已失效')
        #     self.fail_count = self.fail_count + 1
        #     if self.fail_count < 3:
        #         # 重试
        #         logging.info('更换cookie重试')
        #         self.cookie_index = (self.cookie_index + 1) % len(self.cookies)
        #         yield scrapy.Request(
        #             self.url.format(pageNo=1, keyword=self.keyword_list[self.now_keyword_index]), )
        #         return
        #     else:
        #         logging.info('cookie全部过期')
        #         return
        # for info in response.xpath("//div[@class='job-list']/ul//li"):
        for info in response.xpath("//ul[@class='job-list-box']/li"):
            url = self.prefix_url + ''.join(info.xpath(".//div[@class='job-card-body clearfix']/a/@href").extract())
            jobs = ''.join(info.xpath(".//span[@class='job-name']/text()").extract())
            work_address = info.xpath(".//span[@class='job-area']/text()").get()
            scalary = info.xpath(".//span[@class='salary']/text()").get()
            tag_list = info.xpath(".//div[@class='job-card-body clearfix']//ul[@class='tag-list']")
            experiences = tag_list.xpath(".//li[1]/text()").get()
            degree = tag_list.xpath(".//li[2]/text()").get()
            company = ''.join(info.xpath(".//h3[@class='company-name']/a/text()").extract())
            # company_tag_list = info.xpath("//div[@class='company-info']//ul[@class='company-tag-list']/li")
            # if len(company_tag_list == 3):
            #     financing_condition = info.xpath("//div[@class='company-info']//ul[@class='company-tag-list']/li[2]/text()").get()
            #     company_persion = info.xpath("//div[@class='company-info']//ul[@class='company-tag-list']/li[3]/text()").get()
            # else:
            #     financing_condition = info.xpath("//div[@class='company-info']//ul[@class='company-tag-list']/li[2]/text()").get()
            #     company_persion = ''
            item['url'] = url
            item['jobs'] = jobs
            item['work_address'] = work_address
            item['scalary'] = scalary
            item['experiences'] = experiences
            item['degree'] = degree
            item['company'] = company
            # item['financing_condition'] = financing_condition
            # item['company_persion'] = company_persion
            yield item
        try:
            self.now_page = self.now_page + 1
            next_url = self.url.format(pageNo=self.now_page, city=101270100,
                                       keyword=self.keyword_list[self.now_keyword_index])
            if self.now_page == 11:
                logging.info("爬取关键词{keyword}完毕，爬取下一关键词或退出".format(keyword=self.keyword_list[self.now_keyword_index]))
                if not self.now_keyword_index == len(self.keyword_list) - 1:
                    self.now_keyword_index = self.now_keyword_index + 1
                    self.fail_count = 0
                    self.now_page = 1
                    yield scrapy.Request(
                        self.url.format(pageNo=self.now_page, city=101270100,
                                        keyword=self.keyword_list[self.now_keyword_index]))
                else:
                    return
            else:
                logging.info("下一页地址：{}".format(next_url))
                self.fail_count = 0
                yield scrapy.Request(next_url)

        except Exception as e:
            logging.info('爬虫异常，退出爬虫...{}'.format(e))
            return
