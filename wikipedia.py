import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    start_urls = [
        'https://es.wikipedia.org/wiki/Parque_nacional_de_Yellowstone',
        # 'https://es.wikipedia.org/wiki/Persona_5',
    ]

    def parse(self, response):
        for row in response.xpath('//table[contains(@class, "infobox")]/tbody/tr'):

            # Parsear Propiedad: Localidad, etc
            headerText = row.xpath('./th/text()').get()
            headerLink = row.xpath('./th/a/text()').get()
            header = headerText if headerText != None else headerLink
            
            # Parsear link
            linkRaw = row.xpath('./td//a/@href').get()
            if linkRaw != None and linkRaw.startswith('/'):
                link = (response.url + linkRaw)
            else:
                link = linkRaw

            yield {
                'header': header,
                'content': row.xpath('./td//a/text()').get(),
                'link': link,
            }
