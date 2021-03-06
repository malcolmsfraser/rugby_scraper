import scrapy

class RugbySpider(scrapy.Spider):
    name = '2020results'
    start_urls = ['https://www.superxv.com/results/2020-super-rugby-results/']
    custom_settings = {'FEED_URI' : '2020results.csv'}
    
    def parse(self, response):
        home_team = response.css('td:nth-child(1) a').css('::text').extract()
        home_team_score = response.css(
        	'.fixturestable:nth-child(10) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(7) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(24) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(19) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(4) tr:nth-child(8) td:nth-child(2) , tr:nth-child(7) td:nth-child(2) , tr:nth-child(6) td:nth-child(2) , tr:nth-child(5) td:nth-child(2) , tr:nth-child(4) td:nth-child(2) , tr:nth-child(3) td:nth-child(2) , tr:nth-child(2) td:nth-child(2)'
        	).css('::text').extract()
        away_team = response.css('td:nth-child(4) a').css('::text').extract()
        away_team_score = response.css('tr+ tr td:nth-child(5)').css('::text').extract()
        date = response.css('tr:nth-child(7) td:nth-child(6) , tr:nth-child(8) td:nth-child(6) , tr:nth-child(6) td:nth-child(6) , tr:nth-child(5) td:nth-child(6) , tr:nth-child(4) td:nth-child(6) , tr+ tr td:nth-child(6) div').css('::text').extract()

        for item in zip(date,home_team,home_team_score,away_team,away_team_score,):
            scrapped_info = {
                'Match Date' : item[0],
                'Home Team' : item[1],
                'Home Team Score' : item[2],
                'Away Team' : item[3],
                'Away Team Score' : item[4],
                
                
            }
            yield scrapped_info