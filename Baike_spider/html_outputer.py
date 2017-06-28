'''
Created on 2017年6月28日

@author: wyq
'''
import csv
import codecs

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)

    
    def output_html(self):
        fout = open("output.html","w", encoding="utf-8")
        
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data["url"])
            fout.write("<td>%s</td>"%data["title"])
            fout.write("<td>%s</td>"%data["summary"])
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()

    
    def output_excel(self):
#         csvfile = open("1.csv", "wb")
#         csvfile.write(codecs.BOM_UTF8)
#         writer = csv.writer(csvfile)
#         for data in self.datas:
#             writer.writerow([data["url"], data["title"], data["summary"]])
#         
#         csvfile.close()
#         with open("test.csv", "w", newline="", encoding="utf-8") as csvfile:
        with codecs.open("test1.csv", "w+", "utf_8_sig") as csvfile:
#             csvfile.write(codecs.BOM_UTF8)
            cfile = csv.writer(csvfile, dialect="excel")
            for data in self.datas:
                cfile.writerow([data["url"], data["title"], data["summary"]])
            
    
    
    
    
    



