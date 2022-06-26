import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

with open('my_text_file.txt', 'w') as f:
    f.write('ArticleID|CreatedDate|MeSH|IsMajor\n')

for pubmed_article in root.findall('PubmedArticle'):
    ArticleID = pubmed_article.find('MedlineCitation').find('PMID').text
    year = pubmed_article.find('MedlineCitation').find('DateCreated').find('Year').text
    month = pubmed_article.find('MedlineCitation').find('DateCreated').find('Month').text
    day = pubmed_article.find('MedlineCitation').find('DateCreated').find('Day').text
    CreatedDate = year + month + day

    for mesh_heading in pubmed_article.find('MedlineCitation').find('MeshHeadingList').findall('MeshHeading'):
        MeSH = mesh_heading.find('DescriptorName').text
        IsMajor = mesh_heading.find('DescriptorName').get('MajorTopicYN')
        line_to_write = ArticleID + '|' + CreatedDate + '|' + MeSH + '|' + IsMajor + '\n'
        
        with open('my_text_file.txt', 'a') as f:
            f.write(line_to_write)