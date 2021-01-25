# scrapyd API

Github: [https://github.com/mouday/scrapyd-api](https://github.com/mouday/scrapyd-api)

Gitee: [https://gitee.com/mouday/scrapyd-api](https://gitee.com/mouday/scrapyd-api)

Pypi: [https://pypi.org/project/scrapyd-api](https://pypi.org/project/scrapyd-api)


## 安装
```bash
pip install scrapyd-api
```

## 使用示例
```python
# -*- coding: utf-8 -*-
from pprint import pprint

from scrapyd_api import ScrapydClient

client = ScrapydClient()
pprint(client.daemon_status())
"""
{'finished': 67,
 'node_name': 'localhost',
 'pending': 0,
 'running': 0,
 'status': 'ok',
 'total': 67}
"""
``` 


## 简介

说明，基于`scrapyd 1.2.1`进行调用，如果版本差异大，可能会出现异常


ScrapydAPI对原有的Scrapyd api进行原样返回，有利于二次开发

接口文档：[https://scrapyd.readthedocs.io/en/stable/api.html](https://scrapyd.readthedocs.io/en/stable/api.html)

```bash
class ScrapydAPI:
    add_version
    cancel
    delete_project
    delete_version
    list_jobs
    list_projects
    list_spiders
    list_versions
    schedule
    daemon_status
```

ScrapydClient类继承自 ScrapydAPI，对其进行了扩展和加强

```bash
class ScrapydClient(ScrapydAPI):
    # 加强的数据接口
    daemon_status             # 增加了返回参数 total
    add_version               # 添加version 默认值为当前时间戳 10位
    list_spiders              # 返回值：列表+字符串 改为 列表+字典
    list_projects             # 返回值：列表+字符串 改为 列表+字典
    list_versions             # 返回值：列表+字符串 改为 列表+字典  

    # 扩展的数据接口
    job_status                # 查询任务状态
    list_versions_format      # 格式化版本号为日期时间格式 '%Y-%m-%d %H:%M:%S'
    list_jobs_merge           # 合并后的任务列表
    cancel_all_project_job    # 取消所有项目下的任务
    cancel_all_job            # 取消指定项目下的任务

    # 扩展的日志接口
    logs                      # 获取日志-项目列表
    project_logs              # 获取日志-爬虫列表
    spider_logs               # 获取日志-任务列表
    job_log                   # 获取job日志
    
```