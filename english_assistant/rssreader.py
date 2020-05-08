import feedparser

TEST_FEED_YH_URL = 'http://www.chinadaily.com.cn/rss/cndy_rss.xml'


class rss_moduel():
    rss_map = {}

    def __init__(self):
        self.url = 'http://www.chinadaily.com.cn/rss/cndy_rss.xml'
        self.rss_map = {}
        self.rss_map[self.url] = ""

    def add_rss_source(self, feedurl: str):
        self.rss_map[feedurl] = ""

    def get_rss_source(self) -> str:  # 将新增rss与显示rss放在一起，用户在添加rss源后立刻显示rss内容
        feedurl = self.url
        try:
            data = feedparser.parse(feedurl)
        except Exception:
            print("rss open error")
        self.rss_map[feedurl] = data
        message = ''
        for entry in data.entries:
            message += '' + entry.title + '\n' + entry.link + '\n\n'
        return message

    def del_rss_source(self, feedurl):  # 删除rss
        self.rss_map.pop(feedurl)

    def alter_rss_source(self, feedurl: str, new_feedurl: str):  # 修改rss
        self.del_rss_source(feedurl)
        self.add_rss_source(new_feedurl)

    def get_all_rss_link(self):
        return self.rss_map.keys()


if __name__ == '__main__':
    r1 = rss_moduel()
    print(r1.get_rss_source())
    # r1.alter_rss_source(TEST_FEED_YH_URL)
    # print(r1.rss_map)
    # r1.del_rss_source(TEST_FEED_YH_URL)
    # print(r1.rss_map)
    # del r1
