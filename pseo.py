'''
1.read text file
2.fetch dynamic urls
3.concatenate with static url
4.save complete urls in a list then 
5.do de duplication logic check
6.write the complete url into sitemap.xml using pseo category 
7.add newly madesitemap into index
'''
import xml.etree.ElementTree as ET

urls=[]
with open("input.txt","r") as file:
    for line in file:
        urls.append(line.strip())

static_url="https://fabric.bloomscorp.com/b2b/"
full_urls=[]

for u in urls :
    full_urls.append(static_url+u)
print(full_urls)

#deduplication logic covert into sets and then again convert into list
list(set(full_urls))


#creating pseo category  url into sitemap.xml 

urlset = ET.Element("urlset",{"xmlns":"http://www.sitemaps.org/schemas/sitemap/0.9"})
for url in full_urls:
    pseo_tag=ET.SubElement(urlset,"pseo")
    pseo_tag.text=url

tree=ET.ElementTree(urlset)
tree.write("pseo_sitemap.xml")