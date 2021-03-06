# davidScrapy

This repo is a Workshop for Scrapy Python library usage. This project makes the scraping process for the books catalog, forms, emails and comments for the actual [Packthub](https://packtpub.com) website outputted to a JSON file (refer to `books.json`)

## Pre-Requisites

A full Python3 virtualenv setup.

## Installation

Just run the `pip install -r requirements.txt`

## Using Scrapy

`scrapy startproject [name]` for me will be `basic_crawler`
`scrapy crawl [name]`

All the logic is wrote on the `spiders/spider.py`. This is the spider (crawler) class which contains the iteration logic and regex pattern for detecting elements across the site. You will need to verify the DOM structure of the page in order to perfectly collect the desired information.

Internally, Scrapy handles the `Item` class which represents the fields that will be scraped on the site and also uses the `Selector` class that will map the HTTP response.

## Pentesting Approach

On a Basic Web Penetration testing, the scraping actions are present on the `Mapping` phase, it's very helpful for:

  - build a map or catalog to the app resources or capabilities
  - checking entry points
  - resources with parameters as inputs (forms and directories)
  - perform by crawler aka spiders (scraping tasks) - extracting data from the website

The mapping phrase include techniques such as:

  1. Crawling (Spiders)
  2. Using a proxy to identify links that were generated by JS and the crawler/spider missed (dynamic resources)
  3. Check on how to discover non linked resources by brute force attacks (dictionary attacks)

## Credits
  - [David Lares](https://twitter.com/davidlares3)

## Licence

  - [MIT](https://opensource.org/licenses/MIT)
