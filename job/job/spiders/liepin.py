import scrapy


class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = []
    for i in range(0, 9):
        # https://www.liepin.com/zhaopin/?headId=db21748a3299f8ecb750c47fbe4b13f5&ckId=vqnx0znmrh52ekbd6dzylbf9oghba7g9&oldCkId=db21748a3299f8ecb750c47fbe4b13f5&fkId=fc7104c8cc08f0692338687c81a6b226&skId=fc7104c8cc08f0692338687c81a6b226&sfrom=search_job_pc&currentPage=2&scene=page
        # https://www.liepin.com/zhaopin/?sfrom=search_job_pc&currentPage=0&scene=page
        url = 'https://www.liepin.com/zhaopin/?sfrom=search_job_pc&currentPage=' + str(i) + '&scene=page'
        start_urls.append(url)

    def parse(self, response):
        html = open('page.html', 'wb')
        html.write(response.body)
        html.close()

        job_list = response.xpath('/html/body/div/div/section[1]/div/ul/li')
        for job in job_list:
            job_name = job.xpath('div/div/div[1]/div/a[1]/div[1]/div/div[1]/text()').get()
            job_salary = job.xpath('div/div/div[1]/div/a[1]/div[1]/span[@class="job-salary"]/text()').get()
            job_location = job.xpath('div/div/div[1]/div/a[1]/div[1]/div/div[2]/span[@class="ellipsis-1"]/text()').get()
            job_company = job.xpath(
                'div/div/div[1]/div//div[@class="job-detail-company-box"]/div/span[@class="company-name ellipsis-1"]/text()').get()
            # [company_industry, company_stage, company_size]
            job_company_detail = [job.xpath(
                'div/div/div[1]/div//div[@class="job-detail-company-box"]/div/div[@class="company-tags-box ellipsis-1"]/span[1]/text()').get(),
                                  job.xpath(
                                      'div/div/div[1]/div//div[@class="job-detail-company-box"]/div/div[@class="company-tags-box ellipsis-1"]/span[2]/text()').get(),
                                  job.xpath(
                                      'div/div/div[1]/div//div[@class="job-detail-company-box"]/div/div[@class="company-tags-box ellipsis-1"]/span[3]/text()').get()]
            job_tag_list = job.xpath(
                'div/div/div[1]/div/a[1]/div[@class="job-labels-box"]/span')
            job_tag = []
            for tag in job_tag_list:
                job_tag.append(tag.xpath('./text()').extract_first())

            print(
                'job name: ' + job_name + '  ' + 'job salary: ' + job_salary + '  ' + 'job location: ' + job_location + '  ' + 'job company: ' + job_company + '  ' + 'job detail avaliable info number: ' + str(
                    len(
                        job_company_detail)) + '  ' + 'job tag: ' + ' '.join(job_tag))

