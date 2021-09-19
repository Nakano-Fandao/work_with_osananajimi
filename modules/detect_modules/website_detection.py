import sqlite3
from contextlib import closing
import datetime
import shutil, os

class WebsiteDetection():
    def detect(self, normal_websites):
        print(normal_websites)
        #* ユーザー名を取得
        current_path = os.path.dirname(__file__)
        split_current_path = str(current_path).split("""\\""")
        User_names = split_current_path[2]

        #* 履歴情報をローカルファイルにコピー
        db_dir_path =  "C:/Users/"+User_names+"/AppData/Local/Google/Chrome/User Data/Default"
        shutil.copyfile(db_dir_path+"/History", db_dir_path+"/History_copy")

        #* データベースの指定
        db_path = db_dir_path+"/History_copy"
        filePath = db_dir_path+'/result.txt'

        #* 現在時刻を取得
        now = datetime.datetime.now()

        #* 何秒間分の履歴を取得するか
        period = datetime.timedelta(minutes=1)

        #* データベースから履歴を取得
        with closing(sqlite3.connect(db_path)) as conn:
            c = conn.cursor()
            select_sql = "select visits.id, urls.url, urls.title, visits.visit_time,visits.from_visit from visits inner join urls on visits.url = urls.id"
            with open(filePath, mode='a', encoding='utf-8') as f:
                for row in c.execute(select_sql):
                    history = datetime.datetime.fromtimestamp(row[3]/1000000-11644473600)
                    if now-history < period and any(map(row[1].__contains__, normal_websites)):
                        strLine =row[1] + ', ' + row[2] + ', ' + str(history) + ', '+'\n'
                        print(strLine)
                        print("なにみてんだよ")
                        return "youtube"

                    elif now-history < period and any(map(row[1].__contains__, ("https://jp.pornhub.com/", "https://www.dmm.co.jp/"))):
                        strLine =row[1] + ', ' + row[2] + ', ' + str(history) + ', '+'\n'
                        print(strLine)
                        print("死ねよ豚")
                        return "hentai"
                    else:
                        pass
                f.close()
                print("偉いにぇ！！")
                return "safe"

if __name__ == '__main__':
    website_detection = WebsiteDetection()
    website_detection.detect()
