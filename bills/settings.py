#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

basedir = '/home/e9t/data/popong/bills'
likms   = 'http://likms.assembly.go.kr/bill/jsp'
ASSEMBLY_ID = 19

NUM_PAGES       = 50            # number of bills in list page (for crawling)
START_BILL      = 1
END_BILL        = 5000          # current max number for 19th assembly: 5000
ID_MULTIPLIER   = 100000        # bill_id's multiplier for ASSEMBLY_IDs

DIR = {
    'meta'         : '%s/meta' % basedir,
    'data'         : '%s/json/%d' % (basedir, ASSEMBLY_ID),
    'list'         : '%s/html/list/%d' % (basedir, ASSEMBLY_ID),
    'summaries'    : '%s/html/summaries/%d' % (basedir, ASSEMBLY_ID),
    'specifics'    : '%s/html/specifics/%d' % (basedir, ASSEMBLY_ID),
    'proposers'    : '%s/html/proposers/%d' % (basedir, ASSEMBLY_ID),
    'withdrawers'  : '%s/html/withdrawers/%d' % (basedir, ASSEMBLY_ID)
}
BASEURL = {
    'list'         : '%s/BillSearchResult.jsp?AGE_FROM=%d&AGE_TO=%d&' % (likms, ASSEMBLY_ID, ASSEMBLY_ID),
    'summary'      : likms + '/SummaryPopup.jsp?bill_id=',
    'specific'     : likms + '/BillDetail.jsp?bill_id=',
    'proposer_list': likms + '/CoactorListPopup.jsp?bill_id=',
    'withdrawers'  : likms + '/ReturnListPopup.jsp?bill_id='
}
X = {
    'columns'      : 'descendant::td',
    'spec_table'   : '//table[@width="940"]',
    'spec_entry'   : 'descendant::tr[@bgcolor="#EAF2ED"]/following-sibling::tr/td/div',
    'spec_status'  : '//td[@background="/bill/WebContents/BillDetail/circle_11.gif"]/text()',
    'spec_timeline': '//td[@bgcolor="#FEFFEF" and not(@id="SUMMARY_CONTENTS")]/table//tr',
    'spec_timeline_statuses'    : 'descendant::td[@width="59"]/node()',
    'spec_timeline_status_infos': 'descendant::td[@style="display:none"]/textarea/text()',
    'spec_title'   : '//td[@height="33" and @class="title_large"]/text()',
    'summary'      : '//span[@class="text6_1"]/text()',
    'proposers'    : '//td[@width="10%" and @height="20"]/text()',
    'table'        : '//table[@width="970"]//table[@width="100%"]//table[@width="100%"]//tr[not(@bgcolor="#DBDBDB")][position()>1]',
    'withdrawers'  : '//td[@width="10%" and @height="20"]/text()'
}

META_DATA       = '%s/na-bills-%d.csv' % (DIR['meta'], ASSEMBLY_ID)
