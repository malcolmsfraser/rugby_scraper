import scrapy
#from ..items import SuperRugbyItem

class RugbySpider(scrapy.Spider):
    name = 'rugby'
    start_urls = ['https://www.superxv.com/results/2020-super-rugby-results/',
    'https://www.superxv.com/results/2018-super-rugby-results/']
    
    def parse(self, response):
        #items = SuperRugbyItem()

        home_team = response.css('td:nth-child(1) a').css('::text').extract()
        home_team_score = response.css(
        	'.fixturestable:nth-child(10) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(7) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(24) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(19) tr:nth-child(8) td:nth-child(2) , .fixturestable:nth-child(4) tr:nth-child(8) td:nth-child(2) , tr:nth-child(7) td:nth-child(2) , tr:nth-child(6) td:nth-child(2) , tr:nth-child(5) td:nth-child(2) , tr:nth-child(4) td:nth-child(2) , tr:nth-child(3) td:nth-child(2) , tr:nth-child(2) td:nth-child(2)'
        	).css('::text').extract()
        away_team = response.css('td:nth-child(4) a').css('::text').extract()
        away_team_score = response.css('tr+ tr td:nth-child(5)').css('::text').extract()
        date = response.css('tr:nth-child(7) td:nth-child(6) , tr:nth-child(8) td:nth-child(6) , tr:nth-child(6) td:nth-child(6) , tr:nth-child(5) td:nth-child(6) , tr:nth-child(4) td:nth-child(6) , tr+ tr td:nth-child(6) div').css('::text').extract()

        for item in zip(home_team,home_team_score,away_team,away_team_score,date):
        	scrapped_info = {
        	'Home Team' : item[0],
        	'Home Team Score' : item[1],
        	'Away Team' : item[2],
        	'Away Team Score' : item[3],
        	'Match Date' : item[4],
        	}
        	yield scrapped_info


        # items['home_team'] = home_team
        # items['home_team_score'] = home_team_score
        # items['away_team'] = away_team
        # items['away_team_score'] = away_team_score

        #yield items

        # with open('2020results.html', 'a') as page:
        # 	page.write(items)
        # 	page.close()

        