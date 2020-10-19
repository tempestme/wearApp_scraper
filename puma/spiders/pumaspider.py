import scrapy


class PumaSpider(scrapy.Spider):
    name = "puma"
    start_urls = ['https://ru.puma.com/skidki/muzhchiny/obuv.html']

    def parse(self, response):
        product = response.css(".image-sv01").extract() #this is card, and we gonna scrap data from each card




        title = response.css(".product-item__name::text")[0].extract()
        saleprice = response.css("#product-price-253492 > span.price::text").extract()  # WITHOUT SALE
        oldprice = response.css("#old-price-253492 > span.price::text").extract()  # SALE

        yield 'product is ' + product
        yield 'old price is ' + oldprice
        yield 'sale price is ' + saleprice

        # old-price-228008 > span

# catalog > div.grid-w.products-grid > div > div:nth-child(14) > div > div.product-item__details > div.product-item__info > div.product-item__name-w > a

# div - data-block
# xpath =  /html/body/script[46]/text()
# <span class="old-price sly-old-price no-display">  <span class="price-container price-final_price tax weee"> <span class="price-label">Regular Price</span>  <span id="old-price-228008" data-price-amount="4490" data-price-type="oldPrice" class="price-wrapper "><span class="price">4&nbsp;490,00&nbsp;₽</span></span>  </span> </span>


# //*[@id="old-price-228008"]/span/text
