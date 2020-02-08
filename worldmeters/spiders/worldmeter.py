
import scrapy
import logging

class WorldmeterSpider(scrapy.Spider):
    name = 'worldmeter'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()    

            yield response.follow(url=link, callback=self.parse_country,meta={'country_name':name})

    def parse_country(self,response):
        name = response.request.meta["country_name"]

        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")        
        
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td/strong/text()").get()
            Yearly_precentage_of_Change = row.xpath(".//td[3]/text()").get()
            Yearly_Change = row.xpath(".//td[4]/text()").get()
            Migrants_net = row.xpath(".//td[5]/text()").get()
            Median_Age = row.xpath(".//td[6]/text()").get()
            Fertility_Rate = row.xpath(".//td[7]/text()").get()
            Density_Per_Km_square = row.xpath(".//td[8]/text()").get()
            Urban_Pop_percentage = row.xpath(".//td[9]/text()").get()
            Urban_Population = row.xpath(".//td[10]/text()").get()
            Countrys_Share_of_World_Pop = row.xpath(".//td[11]/text()").get()
            World_Population = row.xpath(".//td[12]/text()").get()
            China_Global_Rank = row.xpath(".//td[13]/text()").get()

            yield{
                'country_name':name,
                'year':year,
                'population':population,
                'Yearly_precentage_of_Change': Yearly_precentage_of_Change,
                'Yearly_Change': Yearly_Change,
                'Migrants_net': Migrants_net,
                'Median_Age': Median_Age,
                'Fertility_Rate': Fertility_Rate,
                'Density_Per_Km_square': Density_Per_Km_square,
                'Urban_Pop_percentage': Urban_Pop_percentage,
                'Urban_Population': Urban_Population,
                'Countrys_Share_of_World_Pop': Countrys_Share_of_World_Pop,
                'World_Population': World_Population,
                'China_Global_Rank': China_Global_Rank

            }
